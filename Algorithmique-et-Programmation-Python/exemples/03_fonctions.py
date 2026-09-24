"""Fonction pure avec valeurs attendues indépendantes."""

from math import isfinite, isclose


def gmq_simple(depart_kg, arrivee_kg, jours):
    if not all(isfinite(p) and p > 0 for p in (depart_kg, arrivee_kg)):
        raise ValueError("Poids positifs et finis requis")
    if isinstance(jours, bool) or not isinstance(jours, int) or jours <= 0:
        raise ValueError("Durée entière strictement positive requise")
    return (arrivee_kg - depart_kg) * 1000 / jours


assert isclose(gmq_simple(180, 185.6, 7), 800)
assert isclose(gmq_simple(180, 179.3, 7), -100)
try:
    gmq_simple(180, 185, 0)
except ValueError as error:
    print("Erreur attendue :", error)
else:
    raise AssertionError("Durée nulle non rejetée")
print("GMQ :", round(gmq_simple(180, 185.6, 7)), "g/j")
