"""Génère les illustrations SVG originales du cours, sans dépendance externe."""

from pathlib import Path
from html import escape
import textwrap

ROOT = Path(__file__).resolve().parents[1]
# Ordre des cartes : haut gauche/droite, milieu gauche/droite, bas gauche/droite.
SCHEMAS = [
    (
        "01-fondamentaux",
        "Du besoin au programme",
        "Formaliser avant de traduire en Python",
        [
            ("Besoin métier", "Suivre des masses et leur évolution"),
            ("Contrat", "Entrées : kg, dates ; sortie : g/j"),
            ("Algorithme", "Parcours fini ; somme et compteur"),
            ("Représentation", "int, float, str, bool, None"),
            ("Trace manuelle", "Invariant : somme des k valeurs lues"),
            ("Vérification", "Exemple connu, cas vide et unités"),
        ],
        [(0, 1), (0, 2), (1, 3), (2, 4), (3, 5), (4, 5)],
        "Un programme correct relie une intention, un contrat et une preuve par les cas.",
    ),
    (
        "02-controle",
        "Décider et parcourir",
        "Une absence de mesure n’est pas une mesure égale à zéro",
        [
            ("Collection", "Liste de mesures, une visite par élément"),
            ("Valeur absente ?", "Tester explicitement is None"),
            ("Compteur de rejets", "Tracer les mesures non disponibles"),
            ("Valeur disponible", "Comparer au seuil configuré"),
            ("Données exploitables", "Conserver zéro ; unités inchangées"),
            ("Alertes", "Compter par bâtiment avec un dict"),
        ],
        [(0, 1), (1, 2), (1, 3), (3, 4), (3, 5)],
        "Les branches « absence » et « seuil dépassé » répondent à deux problèmes distincts.",
    ),
    (
        "03-fonctions",
        "Le contrat d’une fonction",
        "Entrées validées, résultat explicite, effets maîtrisés",
        [
            ("Appelant", "Console, interface ou test"),
            ("Paramètres", "Poids positifs, dates distinctes"),
            ("Validation", "Valeurs finies ; durée positive"),
            ("Exception", "ValueError vers l’appelant"),
            ("Calcul pur", "Gain kg × 1 000 / jours"),
            ("Valeur retournée", "GMQ en g/j, éventuellement négatif"),
        ],
        [(0, 1), (1, 2), (2, 3), (2, 4), (4, 5)],
        "Le calcul ne dépend ni de Qt ni du mode de stockage.",
    ),
    (
        "04-poo",
        "Modèle objet et responsabilités",
        "Composition conceptuelle : un animal possède plusieurs pesées",
        [
            ("Animal", "identifiant : str ; bâtiment : str"),
            ("Pesée [0..*]", "jour : date ; poids_kg : float"),
            ("Service KPI", "gmq(historique) → float ou None"),
            ("Dépôt de données", "Clé étrangère vers Animal"),
            ("Vue utilisateur", "Présente les résultats calculés"),
            ("Validation", "Une date par animal ; poids fini"),
        ],
        [(0, 1), (1, 3), (1, 2), (2, 4), (3, 5)],
        "La multiplicité est matérialisée par SQLite ; les calculs restent des fonctions pures.",
    ),
    (
        "05-qualite",
        "Importer sans état partiel",
        "Toutes les lignes sont validées avant l’écriture",
        [
            ("Fichier CSV", "Taille limitée, colonnes attendues"),
            ("Validation du lot", "Dates, unités, bornes et types"),
            ("Erreur de format", "Refuser avant toute insertion"),
            ("Transaction SQL", "Paramètres liés et contraintes"),
            ("Rollback", "Une erreur annule tout le lot"),
            ("Commit", "Toutes les lignes deviennent persistantes"),
        ],
        [(0, 1), (1, 2), (1, 3), (3, 4), (3, 5)],
        "Transaction ≠ sauvegarde : une copie restaurable reste nécessaire.",
    ),
    (
        "06-data",
        "De la donnée brute à l’analyse",
        "Préserver la provenance et les effectifs",
        [
            ("Sources brutes", "CSV, SQL ou capteurs"),
            ("Validation", "Types, unités, dates, doublons"),
            ("Zone de rejets", "Motif documenté ; pas de zéro inventé"),
            ("NumPy / Pandas", "Tableau homogène ou DataFrame"),
            ("Agrégats", "Par animal, date et bâtiment"),
            ("Passage à l’échelle", "Chunks, SQL ; distribution si nécessaire"),
        ],
        [(0, 1), (1, 2), (1, 3), (3, 4), (3, 5)],
        "La moyenne des observations et la moyenne par animal peuvent différer.",
    ),
    (
        "07-visualisation",
        "Construire un graphique interprétable",
        "Le choix visuel découle de la question",
        [
            ("Question", "Évolution, distribution ou relation ?"),
            ("Données validées", "Unités, effectifs et provenance"),
            ("Temps", "Courbe avec intervalles réels"),
            ("Groupes", "Points, boîtes ou histogrammes"),
            ("Matplotlib / Seaborn", "Figure, axes, légende, échelle"),
            ("Lecture critique", "Pas de causalité déduite d’une corrélation"),
        ],
        [(0, 1), (1, 2), (1, 3), (2, 4), (3, 5), (4, 5)],
        "Conserver les observations et expliciter toute agrégation.",
    ),
    (
        "08-ml",
        "Apprendre puis évaluer",
        "Séparation par temps ou par animal selon la question",
        [
            ("Dataset et cible", "Variables disponibles à la décision"),
            ("Découpage", "Train, validation, test réservé"),
            ("Entraînement", "Prétraitement + modèle dans Pipeline"),
            ("Test indépendant", "Même métrique que la baseline"),
            ("Modèle choisi", "Sélection via validation uniquement"),
            ("Inférence", "Nouvelles entrées ; surveillance de dérive"),
        ],
        [(0, 1), (1, 2), (1, 3), (2, 4), (4, 5), (3, 5)],
        "Le test évalue un modèle déjà choisi ; il ne sert pas à ajuster les paramètres.",
    ),
    (
        "09-deep-learning",
        "Le cycle d’optimisation",
        "PyTorch explicite la boucle ; Keras l’orchestre",
        [
            ("Batch de tenseurs", "Forme : observations × caractéristiques"),
            ("Passe avant", "Couches, activations et prédiction"),
            ("Optimiseur", "Mise à jour des poids selon gradients"),
            ("Perte", "Écart entre prédiction et cible"),
            ("Paramètres mis à jour", "Prochaine itération d’entraînement"),
            ("Rétropropagation", "Dérivées de la perte par autodifférentiation"),
        ],
        [(0, 1), (1, 3), (3, 5), (5, 2), (2, 4), (4, 0)],
        "À l’inférence, les poids restent fixes et les gradients ne sont pas nécessaires.",
    ),
    (
        "10-cyber",
        "Protéger et valider un message",
        "Confidentialité, intégrité et plausibilité sont distinctes",
        [
            ("Paquet local Scapy", "Couches IP / UDP / charge utile"),
            ("Message reçu", "Octets à traiter comme non fiables"),
            ("Protection cryptographique", "Clé protégée ; token authentifié"),
            ("Validation métier", "Bornes, fraîcheur et unité"),
            ("Rejet documenté", "Altération, format ou mesure invalide"),
            ("Stockage accepté", "SQL paramétré, transaction"),
        ],
        [(0, 1), (1, 2), (2, 3), (2, 4), (3, 4), (3, 5)],
        "Une signature ou un chiffrement valide ne prouve pas que le capteur mesure juste.",
    ),
    (
        "11-web",
        "Architecture d’un service Web",
        "Extension pédagogique distincte du client Qt local",
        [
            ("Client", "Interface ou passerelle IoT"),
            ("HTTP / JSON", "Contrat, identité, idempotence"),
            ("Contrôleur", "FastAPI, Flask ou Django"),
            ("Validation", "Types, droits et limites"),
            ("Service métier", "Calcul et règles réutilisables"),
            ("Persistance", "Transactions, contraintes et journal"),
        ],
        [(0, 1), (1, 3), (3, 2), (2, 4), (4, 5)],
        "Le framework transporte la demande ; le métier ne dépend pas du framework.",
    ),
    (
        "12-iot",
        "Du capteur à l’interface",
        "Deux sources possibles, un contrat d’entrée commun",
        [
            ("ESP32 / MicroPython", "DHT22 : température et humidité"),
            ("Passerelle", "Identité, unité, horodatage avec fuseau"),
            ("Raspberry Pi / GPIO", "Linux, CPython, entrée de contact"),
            ("Transport", "CSV livré ; HTTPS/MQTT en extension"),
            ("PyQt5", "Courbe, fraîcheur et alertes"),
            ("SQLite", "Validation puis stockage atomique"),
        ],
        [(0, 1), (2, 1), (1, 3), (3, 5), (5, 4)],
        "Une mesure conserve son heure d’acquisition, même après retransmission.",
    ),
    (
        "13-sciences",
        "Simuler un système physique",
        "Les unités relient l’équation au phénomène",
        [
            ("Hypothèses physiques", "Paramètres et état initial"),
            ("Modèles", "Oscillateur amorti ; circuit RC"),
            ("Solveur SciPy", "Équations différentielles, tolérances"),
            ("Signal mesuré", "Échantillonnage et bruit"),
            ("Validation", "Solution RC exacte, énergie, unités"),
            ("Filtrage", "Hors ligne ≠ temps réel causal"),
        ],
        [(0, 1), (1, 2), (1, 3), (2, 4), (3, 5), (5, 4)],
        "Une solution numérique précise peut rester fondée sur un modèle inadapté.",
    ),
    (
        "14-projet",
        "Élevage connecté — architecture livrée",
        "Application locale, une base par projet",
        [
            ("Interface PyQt5", "Animaux, tâches, capteurs, paramètres"),
            ("Entrées IoT", "Simulation ou import CSV validé"),
            ("Services de stockage", "Animaux, pesées, aliments, sessions"),
            ("SQLite", "Données et paramètres persistants"),
            ("Services KPI", "GMQ, IC, temps ; gestion des absences"),
            ("Assistant local", "Règles + régression OLS ; validation humaine"),
        ],
        [(0, 2), (1, 3), (2, 3), (3, 4), (4, 5), (0, 1)],
        "Aucun pilotage automatique ; les extensions Web et matériel restent séparées du socle.",
    ),
]


def render(name, title, subtitle, nodes, edges, footer):
    coords = [(60, 190), (660, 190), (60, 420), (660, 420), (60, 650), (660, 650)]
    width, height = 520, 150
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1240" height="940" viewBox="0 0 1240 940" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(title)}</title><desc id="desc">{escape(subtitle+". "+footer)}</desc>',
        '<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#438295"/></marker></defs>',
        '<rect width="1240" height="940" fill="#eef4f8"/>',
        '<rect width="1240" height="150" fill="#112b43"/>',
        '<text x="60" y="38" font-family="DejaVu Sans,sans-serif" font-size="15" fill="#65d6bd">LICENCES-LUS • ALGORITHMIQUE ET PROGRAMMATION PYTHON</text>',
        f'<text x="60" y="85" font-family="DejaVu Sans,sans-serif" font-size="32" font-weight="bold" fill="white">{escape(title)}</text>',
        f'<text x="60" y="121" font-family="DejaVu Sans,sans-serif" font-size="19" fill="#d4e3ee">{escape(subtitle)}</text>',
    ]
    for a, b in edges:
        ax, ay = coords[a]
        bx, by = coords[b]
        if ax == bx and abs(ay - by) > 230:
            margin = ax - 25 if ax == 60 else ax + width + 25
            side = ax if ax == 60 else ax + width
            svg.append(
                f'<path d="M{side},{ay+height/2} H{margin} V{by+height/2} H{side}" stroke="#438295" stroke-width="2.5" fill="none" marker-end="url(#arrow)"/>'
            )
            continue
        if ax == bx:
            x1 = x2 = ax + width / 2
            y1 = ay + (height if by > ay else 0)
            y2 = by + (0 if by > ay else height)
        elif ay == by:
            x1 = ax + (width if bx > ax else 0)
            x2 = bx + (0 if bx > ax else width)
            y1 = y2 = ay + height / 2
        else:
            x1 = ax + (width if bx > ax else 0)
            x2 = bx + (0 if bx > ax else width)
            y1 = ay + height / 2
            y2 = by + height / 2
        svg.append(
            f'<path d="M{x1},{y1} L{x2},{y2}" stroke="#438295" stroke-width="2.5" fill="none" marker-end="url(#arrow)"/>'
        )
    for index, ((x, y), (label, detail)) in enumerate(zip(coords, nodes)):
        svg.extend(
            [
                f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="14" fill="white" stroke="#ccdbe5"/>',
                f'<rect x="{x}" y="{y}" width="7" height="{height}" rx="3" fill="#00897b"/>',
                f'<text x="{x+25}" y="{y+42}" font-family="DejaVu Sans,sans-serif" font-size="23" font-weight="bold" fill="#16354d">{escape(label)}</text>',
            ]
        )
        for line, text in enumerate(textwrap.wrap(detail, 43)):
            svg.append(
                f'<text x="{x+25}" y="{y+81+line*27}" font-family="DejaVu Sans,sans-serif" font-size="19" fill="#41576b">{escape(text)}</text>'
            )
    for index, line in enumerate(textwrap.wrap(footer, 102)):
        svg.append(
            f'<text x="60" y="{858+index*27}" font-family="DejaVu Sans,sans-serif" font-size="19" fill="#16354d">{escape(line)}</text>'
        )
    svg.append("</svg>")
    return "\n".join(svg) + "\n"


if __name__ == "__main__":
    folder = ROOT / "images"
    folder.mkdir(exist_ok=True)
    for diagram in SCHEMAS:
        (folder / (diagram[0] + ".svg")).write_text(render(*diagram), encoding="utf-8")
    print(f"{len(SCHEMAS)} schémas SVG générés dans {folder}")
