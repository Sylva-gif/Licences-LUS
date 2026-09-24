"""SQLite paramétré, transactions et validation aux frontières."""

import csv
import sqlite3
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from .domain import Weight, number


def utcnow():
    return datetime.now(timezone.utc)


def stamp(value):
    value = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    if value.tzinfo is None:
        raise ValueError("Horodatage : fuseau obligatoire, par exemple +00:00.")
    if value > utcnow() + timedelta(minutes=5):
        raise ValueError("Mesure future refusée (tolérance horloge : 5 minutes).")
    return value.astimezone(timezone.utc).isoformat()


def past_day(value):
    day = date.fromisoformat(str(value))
    if day > date.today():
        raise ValueError("La date ne peut pas être future.")
    return day.isoformat()


def text(value, label, limit=120):
    value = str(value).strip()
    if not value or len(value) > limit:
        raise ValueError(f"{label} : entre 1 et {limit} caractères.")
    return value


class Store:
    def __init__(self, path):
        if str(path) != ":memory:":
            Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(path))
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys=ON")
        self.conn.executescript("""
        CREATE TABLE IF NOT EXISTS animals (
          id INTEGER PRIMARY KEY, tag TEXT NOT NULL UNIQUE,
          species TEXT NOT NULL, barn TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS weights (
          animal_id INTEGER REFERENCES animals(id), day TEXT NOT NULL,
          kg REAL NOT NULL CHECK(kg>0), PRIMARY KEY(animal_id,day));
        CREATE TABLE IF NOT EXISTS feed (
          animal_id INTEGER REFERENCES animals(id), day TEXT NOT NULL,
          kg REAL NOT NULL CHECK(kg>=0), PRIMARY KEY(animal_id,day));
        CREATE TABLE IF NOT EXISTS tasks (
          id INTEGER PRIMARY KEY, title TEXT NOT NULL,
          planned_minutes REAL NOT NULL CHECK(planned_minutes>0),
          done INTEGER NOT NULL DEFAULT 0 CHECK(done IN (0,1)));
        CREATE TABLE IF NOT EXISTS sessions (
          id INTEGER PRIMARY KEY, task_id INTEGER REFERENCES tasks(id),
          started_at TEXT NOT NULL, seconds REAL NOT NULL CHECK(seconds>=0));
        CREATE TABLE IF NOT EXISTS sensors (
          id INTEGER PRIMARY KEY, barn TEXT NOT NULL, measured_at TEXT NOT NULL,
          temperature REAL NOT NULL, humidity REAL NOT NULL,
          source TEXT NOT NULL, UNIQUE(barn,measured_at));
        CREATE TABLE IF NOT EXISTS settings (key TEXT PRIMARY KEY, value TEXT NOT NULL);
        """)
        defaults = {
            "project": "Projet pédagogique — atelier bovin",
            "gmq_min": "500",
            "temp_max": "30",
            "sensor_max_minutes": "30",
            "weight_max_days": "7",
        }
        with self.conn:
            self.conn.executemany(
                "INSERT OR IGNORE INTO settings VALUES (?,?)", defaults.items()
            )

    def settings(self):
        return dict(self.conn.execute("SELECT key,value FROM settings"))

    def save_settings(self, project, gmq_min, temp_max):
        data = {
            "project": text(project, "Projet"),
            "gmq_min": str(number(gmq_min, "Seuil GMQ", -10000, 10000)),
            "temp_max": str(number(temp_max, "Température", -50, 70)),
        }
        with self.conn:
            self.conn.executemany(
                "UPDATE settings SET value=? WHERE key=?",
                [(v, k) for k, v in data.items()],
            )

    def animals(self):
        return self.conn.execute("SELECT * FROM animals ORDER BY tag").fetchall()

    def add_animal(self, tag, species, barn):
        with self.conn:
            return self.conn.execute(
                "INSERT INTO animals(tag,species,barn) VALUES (?,?,?)",
                (
                    text(tag, "Identifiant"),
                    text(species, "Espèce"),
                    text(barn, "Bâtiment"),
                ),
            ).lastrowid

    def weights(self, animal_id):
        return [
            Weight(date.fromisoformat(r[0]), r[1])
            for r in self.conn.execute(
                "SELECT day,kg FROM weights WHERE animal_id=? ORDER BY day",
                (animal_id,),
            )
        ]

    def feeds(self, animal_id):
        return {
            date.fromisoformat(r[0]): r[1]
            for r in self.conn.execute(
                "SELECT day,kg FROM feed WHERE animal_id=? ORDER BY day", (animal_id,)
            )
        }

    def add_weight(self, animal_id, day, kg):
        with self.conn:
            self.conn.execute(
                "INSERT INTO weights VALUES (?,?,?)",
                (animal_id, past_day(day), number(kg, "Poids", 0.01, 5000)),
            )

    def add_feed(self, animal_id, day, kg):
        with self.conn:
            self.conn.execute(
                "INSERT INTO feed VALUES (?,?,?)",
                (animal_id, past_day(day), number(kg, "Aliment", 0, 500)),
            )

    def tasks(self):
        return self.conn.execute("""SELECT t.*, COALESCE(SUM(s.seconds),0) AS seconds
            FROM tasks t LEFT JOIN sessions s ON s.task_id=t.id
            GROUP BY t.id ORDER BY t.id""").fetchall()

    def add_task(self, title, minutes):
        with self.conn:
            return self.conn.execute(
                "INSERT INTO tasks(title,planned_minutes) VALUES (?,?)",
                (text(title, "Tâche"), number(minutes, "Durée prévue", 1, 100000)),
            ).lastrowid

    def finish_task(self, task_id):
        with self.conn:
            self.conn.execute("UPDATE tasks SET done=1 WHERE id=?", (task_id,))

    def add_session(self, task_id, started_at, seconds):
        with self.conn:
            self.conn.execute(
                "INSERT INTO sessions(task_id,started_at,seconds) VALUES (?,?,?)",
                (task_id, stamp(started_at), number(seconds, "Durée", 0, 604800)),
            )

    def add_sensor(self, barn, measured_at, temperature, humidity, source="simulation"):
        values = (
            text(barn, "Bâtiment"),
            stamp(measured_at),
            number(temperature, "Température", -50, 70),
            number(humidity, "Humidité", 0, 100),
            text(source, "Source"),
        )
        with self.conn:
            self.conn.execute(
                """INSERT INTO sensors
                (barn,measured_at,temperature,humidity,source) VALUES (?,?,?,?,?)""",
                values,
            )

    def sensors(self):
        return self.conn.execute(
            "SELECT * FROM sensors ORDER BY measured_at DESC LIMIT 200"
        ).fetchall()

    def latest_sensor(self, barn):
        return self.conn.execute(
            "SELECT * FROM sensors WHERE barn=? ORDER BY measured_at DESC LIMIT 1",
            (barn,),
        ).fetchone()

    def import_sensors(self, path):
        """CSV <= 2 Mo, validation totale avant écriture ; doublons refusés."""
        if Path(path).stat().st_size > 2_000_000:
            raise ValueError("CSV trop volumineux (maximum 2 Mo).")
        rows = []
        with open(path, newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != ["barn", "measured_at", "temperature", "humidity"]:
                raise ValueError("Colonnes : barn,measured_at,temperature,humidity")
            for index, row in enumerate(reader, 2):
                try:
                    rows.append(
                        (
                            text(row["barn"], "Bâtiment"),
                            stamp(row["measured_at"]),
                            number(row["temperature"], "Température", -50, 70),
                            number(row["humidity"], "Humidité", 0, 100),
                            "CSV",
                        )
                    )
                except (ValueError, TypeError) as exc:
                    raise ValueError(f"Ligne {index} : {exc}") from exc
        with self.conn:
            self.conn.executemany(
                """INSERT INTO sensors
                (barn,measured_at,temperature,humidity,source) VALUES (?,?,?,?,?)""",
                rows,
            )
        return len(rows)

    def export_weights(self, path):
        def safe_cell(value):
            value = str(value)
            return (
                "'" + value
                if value.startswith(("=", "+", "-", "@", "\t", "\r"))
                else value
            )

        with open(path, "w", newline="", encoding="utf-8-sig") as handle:
            writer = csv.writer(handle)
            writer.writerow(["animal", "espece", "batiment", "date", "poids_kg"])
            for row in self.conn.execute(
                """SELECT a.tag,a.species,a.barn,w.day,w.kg
                FROM weights w JOIN animals a ON w.animal_id=a.id ORDER BY a.tag,w.day"""
            ):
                writer.writerow([safe_cell(v) for v in row])

    def demo(self):
        if self.animals():
            return False
        today = date.today()
        for tag, start, gain in [
            ("BOV-001", 180, 0.8),
            ("BOV-002", 160, 0.25),
            ("BOV-003", 195, -0.1),
        ]:
            animal = self.add_animal(tag, "Bovin", "Atelier A")
            for offset in [0, 7, 14, 21]:
                self.add_weight(
                    animal,
                    (today - timedelta(days=21 - offset)).isoformat(),
                    start + gain * offset,
                )
            for offset in range(21):
                self.add_feed(
                    animal, (today - timedelta(days=21 - offset)).isoformat(), 4
                )
        self.add_task("Contrôle des abreuvoirs", 30)
        self.add_task("Pesée hebdomadaire", 60)
        self.add_sensor("Atelier A", utcnow().isoformat(), 31, 62)
        return True

    def close(self):
        self.conn.close()
