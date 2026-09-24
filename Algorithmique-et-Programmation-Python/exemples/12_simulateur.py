"""Génère un CSV de mesures synthétiques pour import dans le projet."""

import csv, random
from datetime import datetime, timedelta, timezone
from pathlib import Path

rng = random.Random(7)
out = Path(__file__).parent / "sorties"
out.mkdir(exist_ok=True)
path = out / "capteurs-simules.csv"
now = datetime.now(timezone.utc)
with path.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.writer(handle)
    writer.writerow(["barn", "measured_at", "temperature", "humidity"])
    for i in range(6):
        writer.writerow(
            [
                "Atelier A",
                (now - timedelta(minutes=5 * (5 - i))).isoformat(),
                round(rng.uniform(22, 33), 1),
                round(rng.uniform(45, 75), 1),
            ]
        )
print(path)
