"""Assistant local : règles explicables + régression apprise sur les pesées."""

from datetime import date, datetime, timezone
from .domain import forecast, gmq, feed_conversion


def analyze(store, animal, today=None, now=None):
    today = today or date.today()
    now = now or datetime.now(timezone.utc)
    settings = store.settings()
    weights = store.weights(animal["id"])
    rate = gmq(weights)
    ratio = feed_conversion(weights, store.feeds(animal["id"]))
    messages = []
    if rate is None:
        messages.append(
            "DONNÉES : deux pesées à des dates distinctes sont nécessaires au GMQ."
        )
    elif rate < float(settings["gmq_min"]):
        messages.append(
            f"GMQ BAS : {rate:.0f} g/j < seuil de démonstration {settings['gmq_min']} g/j. "
            "Vérifier la pesée, les observations et l'accès à l'alimentation avec le responsable."
        )
    if weights and weights[-1].kg < weights[0].kg:
        messages.append(
            "PERTE DE POIDS : faire confirmer la mesure et demander une évaluation professionnelle."
        )
    stale = not weights or (today - weights[-1].day).days > int(
        settings["weight_max_days"]
    )
    if stale:
        messages.append(
            "PESÉES ANCIENNES OU ABSENTES : actualiser les données avant toute projection."
        )
    sensor = store.latest_sensor(animal["barn"])
    if sensor is None:
        messages.append("CAPTEUR ABSENT : aucune donnée pour ce bâtiment.")
    elif (
        now - datetime.fromisoformat(sensor["measured_at"])
    ).total_seconds() > 60 * int(settings["sensor_max_minutes"]):
        messages.append(
            "CAPTEUR ANCIEN : dernière mesure > 30 minutes ; contrôler la connexion."
        )
    elif sensor["temperature"] > float(settings["temp_max"]):
        messages.append(
            f"TEMPÉRATURE : {sensor['temperature']:.1f} °C, supérieure au seuil configuré "
            f"({settings['temp_max']} °C). Contrôler le capteur et les conditions du bâtiment."
        )
    prediction = None if stale else forecast(weights)
    if prediction and prediction["kg"] <= 0:
        prediction = None
        messages.append("PROJECTION INVALIDE : la droite produit un poids non positif.")
    if not messages:
        messages.append(
            "Aucun seuil configuré franchi ; ce résultat ne constitue pas un bilan sanitaire."
        )
    return {"gmq": rate, "ic": ratio, "prediction": prediction, "messages": messages}


def answer(store, animal, question):
    """Routage d'intentions explicite. Aucun LLM, aucune API, aucune clé."""
    report = analyze(store, animal)
    q = question.casefold()
    intro = f"Analyse locale de {animal['tag']} — règles et régression linéaire\n"
    lines = []
    if any(word in q for word in ["temps", "tâche", "tache", "planning"]):
        tasks = store.tasks()
        lines.append(
            f"Tâches terminées : {sum(t['done'] for t in tasks)}/{len(tasks)}."
        )
        lines.append(
            f"Temps enregistré : {sum(t['seconds'] for t in tasks)/60:.1f} min."
        )
        lines.append(
            "Prioriser les contrôles liés aux alertes, puis les tâches planifiées."
        )
    else:
        lines.extend(report["messages"])
        if report["gmq"] is not None:
            lines.append(
                f"GMQ observé : {report['gmq']:.1f} g/j, de la première à la dernière pesée."
            )
        lines.append(
            "IC indisponible : saisir tous les jours de consommation et obtenir un gain positif."
            if report["ic"] is None
            else f"Indice de consommation : {report['ic']:.2f} kg/kg."
        )
        prediction = report["prediction"]
        if prediction:
            lines.append(
                f"Projection à 7 jours après la dernière pesée : {prediction['kg']:.2f} kg "
                f"(n={prediction['n']}, RMSE d'ajustement={prediction['rmse']:.2f} kg)."
            )
            lines.append(
                "Hypothèse : tendance linéaire inchangée. Pas de validation externe ni d'intervalle de confiance."
            )
        else:
            lines.append(
                "Projection indisponible : au moins 3 pesées récentes et un résultat plausible sont nécessaires."
            )
    lines.append(
        "Seuils pédagogiques à adapter à l'espèce et au stade. Validation humaine requise ; aucune action automatique."
    )
    return intro + "\n\n".join(lines)
