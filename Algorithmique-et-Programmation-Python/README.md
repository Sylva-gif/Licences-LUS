# Algorithmique et Programmation Python

**Filière : Sylva-gif / Licences-LUS — parcours universitaire et technique.**

Ce module part de l'algorithme et de la syntaxe Python pour construire une application de bureau d'élevage connecté. Les notions sont reliées à des situations de données, d'IA, de cybersécurité, de Web, d'IoT et de sciences de l'ingénieur. Chaque chapitre comporte objectifs, cours, code, TP, critères de réussite, références et illustration finale.

## Accès rapide

- [Syllabus : compétences, progression, volumes et évaluation](SYLLABUS.md)
- [Projet PyQt5 prêt à lancer : Élevage connecté](projet-elevage/README.md)
- [Énoncé, jalons et grille du projet](PROJET.md)
- [Installation des exemples et environnements](exemples/README.md)
- [Corrections commentées des exercices](CORRIGES.md)
- [Références officielles](REFERENCES.md)
- [Résultats de vérification et limites](VERIFICATION.md)

## Cours

| Chapitre | Question directrice | Mise en pratique |
|---|---|---|
| [01 — Algorithmes, variables et types](chapitres/01-fondamentaux.md) | Comment transformer un besoin en calcul vérifiable ? | Conversion kg → g, contrats et complexité |
| [02 — Conditions, boucles et collections](chapitres/02-controle.md) | Comment traiter un ensemble de mesures ? | Filtrer, agréger et rechercher |
| [03 — Fonctions et modularité](chapitres/03-fonctions.md) | Comment décomposer et réutiliser ? | GMQ pur, paramètres et exceptions |
| [04 — Objets et UML](chapitres/04-poo.md) | Comment représenter le domaine métier ? | Animal, pesée, composition et interfaces |
| [05 — Fichiers, SQL et qualité](chapitres/05-qualite.md) | Comment conserver des données fiables ? | CSV, SQLite, tests et transactions |
| [06 — NumPy, Pandas et Big Data](chapitres/06-data.md) | Comment exploiter une table de données ? | Validation, agrégation et lecture par blocs |
| [07 — Analyse et visualisation](chapitres/07-visualisation.md) | Comment produire un graphique honnête ? | Courbes, distributions et Matplotlib/Seaborn |
| [08 — Machine Learning](chapitres/08-ml.md) | Comment apprendre sans fuite de données ? | Pipeline scikit-learn, baseline et MAE |
| [09 — PyTorch et TensorFlow](chapitres/09-deep-learning.md) | Comment entraîner un réseau de neurones ? | Tenseurs, gradients, perte et inférence |
| [10 — Python et cybersécurité](chapitres/10-cyber.md) | Comment analyser et protéger les échanges ? | Paquets Scapy locaux et Cryptography |
| [11 — FastAPI, Flask et Django](chapitres/11-web.md) | Comment exposer un service ? | Contrat JSON, validation et séparation des couches |
| [12 — IoT et embarqué](chapitres/12-iot.md) | Comment relier le capteur au logiciel ? | MicroPython, GPIO Raspberry Pi, simulation |
| [13 — Mécanique, électronique et SciPy](chapitres/13-sciences.md) | Comment simuler un phénomène physique ? | Oscillateur, circuit RC et filtrage |
| [14 — Architecture PyQt5 et intégration](chapitres/14-projet.md) | Comment livrer une application cohérente ? | Signaux, stockage, KPI, temps et assistant IA |

## Méthode de travail

Lire un chapitre, exécuter son exemple, modifier une hypothèse, réaliser le TP puis comparer avec la correction. Conserver les résultats dans son propre carnet d'expériences. Pour le projet, travailler par incréments testables ; les données de démonstration permettent de comparer les sorties attendues sans matériel ni service payant.

Les figures SVG sont originales, exactes et lisibles sur GitHub. Les liens des chapitres donnent accès aux mêmes fichiers vectoriels pour les supports de cours. Le module n'exige pas de génération d'images à chaque lecture.

## Utiliser un assistant de programmation de façon contrôlée

Pour chaque exercice, préparer d'abord le contrat et deux exemples numériques. Demander ensuite à l'assistant : « Explique le raisonnement et les cas limites ; propose une implémentation Python 3.12 sans dépendance superflue ; donne un test indépendant ; indique ce qui reste incertain. » Lire le code, l'exécuter et justifier toute modification. Un test réussi n'est pas une preuve de validité scientifique d'un modèle.

[Retour au dépôt](../README.md)
