"""La deuxième insertion invalide annule aussi la première."""

import sqlite3

db = sqlite3.connect(":memory:")
try:
    db.execute(
        "CREATE TABLE mesure(id INTEGER PRIMARY KEY, humidite REAL CHECK(humidite BETWEEN 0 AND 100))"
    )
    try:
        with db:
            db.executemany("INSERT INTO mesure(humidite) VALUES (?)", [(60,), (101,)])
    except sqlite3.IntegrityError:
        print("Lot rejeté, transaction annulée")
    assert db.execute("SELECT COUNT(*) FROM mesure").fetchone()[0] == 0
finally:
    db.close()
