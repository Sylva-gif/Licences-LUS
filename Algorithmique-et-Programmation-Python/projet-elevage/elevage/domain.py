"""Calculs purs : unités explicites et données manquantes conservées."""

from dataclasses import dataclass
from datetime import date
from math import isfinite, sqrt


def number(value, label, minimum=0, maximum=1_000_000):
    result = float(value)
    if not isfinite(result) or not minimum <= result <= maximum:
        raise ValueError(f"{label} : valeur attendue entre {minimum} et {maximum}.")
    return result


@dataclass(frozen=True)
class Weight:
    day: date
    kg: float


def ordered(weights):
    result = sorted(weights, key=lambda w: w.day)
    if len({w.day for w in result}) != len(result):
        raise ValueError("Une seule pesée par animal et par jour.")
    for w in result:
        number(w.kg, "Poids", 0.01, 5000)
    return result


def gmq(weights):
    """Gain moyen quotidien, en g/j, entre première et dernière pesées."""
    values = ordered(weights)
    if len(values) < 2:
        return None
    first, last = values[0], values[-1]
    return 1000 * (last.kg - first.kg) / (last.day - first.day).days


def feed_conversion(weights, feed):
    """kg d'aliment / kg de gain sur [première pesée, dernière pesée[.

    feed : dictionnaire date -> consommation journalière en kg.
    Toute journée manquante ou tout gain non positif rend l'IC indisponible.
    """
    from datetime import timedelta

    values = ordered(weights)
    if len(values) < 2:
        return None
    first, last = values[0], values[-1]
    gain = last.kg - first.kg
    days = [first.day + timedelta(days=i) for i in range((last.day - first.day).days)]
    if gain <= 0 or any(day not in feed for day in days):
        return None
    total = sum(number(feed[day], "Aliment") for day in days)
    return total / gain


def forecast(weights, horizon=7):
    """Régression linéaire OLS, sans dépendance : poids = intercept + pente * jour.

    Le RMSE retourné est une erreur d'ajustement, pas une erreur de test.
    """
    values = ordered(weights)
    if len(values) < 3:
        return None
    horizon = number(horizon, "Horizon", 1, 30)
    xs = [(w.day - values[0].day).days for w in values]
    ys = [w.kg for w in values]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    denominator = sum((x - mx) ** 2 for x in xs)
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / denominator
    intercept = my - slope * mx
    rmse = sqrt(
        sum((y - (intercept + slope * x)) ** 2 for x, y in zip(xs, ys)) / len(xs)
    )
    return {
        "kg": intercept + slope * (xs[-1] + horizon),
        "slope": slope,
        "rmse": rmse,
        "n": len(xs),
        "horizon": horizon,
    }
