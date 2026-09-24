import csv
import os
import sqlite3
import tempfile
import unittest
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from elevage.domain import Weight, gmq, feed_conversion, forecast
from elevage.storage import Store, utcnow
from elevage.assistant import analyze, answer


class DomainTests(unittest.TestCase):
    def setUp(self):
        self.day = date(2026, 1, 1)
        self.weights = [
            Weight(self.day, 100),
            Weight(self.day + timedelta(days=10), 108),
        ]

    def test_units_and_sorting(self):
        self.assertAlmostEqual(gmq(self.weights[::-1]), 800)

    def test_missing_and_duplicate_days(self):
        self.assertIsNone(gmq([]))
        self.assertIsNone(gmq(self.weights[:1]))
        with self.assertRaises(ValueError):
            gmq([self.weights[0]] * 2)

    def test_nonfinite_and_negative(self):
        for kg in [float("nan"), float("inf"), -1, 0]:
            with self.assertRaises(ValueError):
                gmq([Weight(self.day, kg)])

    def test_ic_requires_complete_aligned_days(self):
        food = {self.day + timedelta(days=i): 2 for i in range(10)}
        self.assertAlmostEqual(feed_conversion(self.weights, food), 2.5)
        food[self.day + timedelta(days=10)] = 999
        self.assertAlmostEqual(feed_conversion(self.weights, food), 2.5)
        del food[self.day]
        self.assertIsNone(feed_conversion(self.weights, food))

    def test_weight_loss_not_hidden(self):
        weights = [Weight(self.day, 100), Weight(self.day + timedelta(days=1), 99)]
        self.assertEqual(gmq(weights), -1000)
        self.assertIsNone(feed_conversion(weights, {self.day: 2}))

    def test_regression_known_line(self):
        values = [
            Weight(self.day + timedelta(days=i), 100 + 0.8 * i) for i in [0, 5, 10]
        ]
        result = forecast(values)
        self.assertAlmostEqual(result["kg"], 113.6)
        self.assertAlmostEqual(result["slope"], 0.8)
        self.assertAlmostEqual(result["rmse"], 0)
        self.assertIsNone(forecast(values[:2]))


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.path = Path(self.temp.name) / "test.sqlite3"
        self.store = Store(self.path)
        self.a = self.store.add_animal("A", "Bovin", "B1")

    def tearDown(self):
        self.store.close()
        self.temp.cleanup()

    def test_persistence_and_unique_weight(self):
        self.store.add_weight(self.a, "2026-01-01", 100)
        with self.assertRaises(sqlite3.IntegrityError):
            self.store.add_weight(self.a, "2026-01-01", 101)
        with self.assertRaises(ValueError):
            self.store.add_weight(self.a, "2999-01-01", 100)
        second = Store(self.path)
        try:
            self.assertEqual(second.weights(self.a)[0].kg, 100)
        finally:
            second.close()

    def test_foreign_keys_and_sql_data(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.store.add_weight(999, "2026-01-01", 100)
        self.store.add_animal("'; DROP TABLE animals;--", "Bovin", "B1")
        self.assertEqual(len(self.store.animals()), 2)

    def csv_file(self, rows):
        path = Path(self.temp.name) / "sensors.csv"
        with path.open("w", newline="", encoding="utf-8") as handle:
            w = csv.writer(handle)
            w.writerow(["barn", "measured_at", "temperature", "humidity"])
            w.writerows(rows)
        return path

    def test_import_atomic_validation(self):
        path = self.csv_file(
            [
                ["B1", "2026-01-01T12:00:00Z", 20, 60],
                ["B1", "2026-01-01T13:00:00Z", 20, 101],
            ]
        )
        with self.assertRaises(ValueError):
            self.store.import_sensors(path)
        self.assertEqual(len(self.store.sensors()), 0)

    def test_import_atomic_duplicate(self):
        row = ["B1", "2026-01-01T12:00:00Z", 20, 60]
        with self.assertRaises(sqlite3.IntegrityError):
            self.store.import_sensors(self.csv_file([row, row]))
        self.assertEqual(len(self.store.sensors()), 0)

    def test_import_success_and_timezone(self):
        path = self.csv_file([["B1", "2026-01-01T12:00:00+01:00", 20, 60]])
        self.assertEqual(self.store.import_sensors(path), 1)
        self.assertIn("11:00:00+00:00", self.store.sensors()[0]["measured_at"])
        with self.assertRaises(ValueError):
            self.store.add_sensor("B1", "2026-01-01T12:00:00", 20, 60)

    def test_time_and_task(self):
        task = self.store.add_task("Pesée", 30)
        self.store.add_session(task, utcnow().isoformat(), 90)
        self.store.add_session(task, utcnow().isoformat(), 30)
        self.store.finish_task(task)
        self.assertEqual(self.store.tasks()[0]["seconds"], 120)
        self.assertEqual(self.store.tasks()[0]["done"], 1)

    def test_csv_formula_escaped(self):
        animal = self.store.add_animal("=1+1", "Bovin", "B1")
        self.store.add_weight(animal, "2026-01-01", 100)
        path = Path(self.temp.name) / "export.csv"
        self.store.export_weights(path)
        self.assertIn("'=1+1", path.read_text(encoding="utf-8-sig"))

    def test_stale_sensor_is_not_heat_diagnosis(self):
        self.store.add_sensor("B1", "2026-01-01T00:00:00Z", 40, 60)
        data = analyze(
            self.store,
            self.store.animals()[0],
            now=datetime(2026, 1, 2, tzinfo=timezone.utc),
        )
        self.assertTrue(any("CAPTEUR ANCIEN" in m for m in data["messages"]))
        self.assertFalse(any(m.startswith("TEMPÉRATURE") for m in data["messages"]))

    def test_demo_end_to_end(self):
        demo = Store(":memory:")
        try:
            self.assertTrue(demo.demo())
            self.assertFalse(demo.demo())
            a = demo.animals()[0]
            report = analyze(demo, a)
            self.assertAlmostEqual(report["gmq"], 800)
            self.assertAlmostEqual(report["ic"], 5)
            self.assertIsNotNone(report["prediction"])
            self.assertIn("Projection", answer(demo, a, "croissance"))
            self.assertIn("Temps enregistré", answer(demo, a, "temps"))
        finally:
            demo.close()


class QtTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
        from PyQt5.QtWidgets import QApplication

        cls.app = QApplication.instance() or QApplication([])

    def test_ui_workflow_and_close_saves_timer(self):
        from elevage.ui import Window

        store = Store(":memory:")
        store.demo()
        try:
            window = Window(store)
            window.show()
            self.app.processEvents()
            window.ask()
            self.assertIn("Projection", window.response.toPlainText())
            window.start_task()
            self.assertIsNotNone(window.running)
            window.close()
            self.app.processEvents()
            self.assertIsNone(window.running)
            self.assertEqual(
                store.conn.execute("SELECT COUNT(*) FROM sessions").fetchone()[0], 1
            )
            window.deleteLater()
        finally:
            store.close()


if __name__ == "__main__":
    unittest.main()
