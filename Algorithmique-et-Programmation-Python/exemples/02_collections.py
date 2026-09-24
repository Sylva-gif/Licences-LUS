"""Parcours unique, absence séparée de zéro."""

mesures = [("A", 31), ("B", 22), ("A", 33), ("B", None)]
alertes, absences = {}, 0
for batiment, valeur in mesures:
    if valeur is None:
        absences += 1
    elif valeur > 30:
        alertes[batiment] = alertes.get(batiment, 0) + 1
assert alertes == {"A": 2} and absences == 1
print(alertes, "Absences :", absences)
