# Syllabus universitaire et technique

## 1. Identification

**Intitulé :** Algorithmique et Programmation Python. **Public :** licence, parcours informatique/data/systèmes et reconversion technique encadrée. **Positionnement :** socle algorithmique puis initiation appliquée aux frameworks. La maîtrise professionnelle de chacun des domaines demande des modules complémentaires.

**Volume proposé : 84 h encadrées** (28 h cours, 28 h travaux dirigés, 28 h travaux pratiques), soit 14 séances de 6 h, plus **42 h de travail personnel** dont 24 h de projet. Il s'agit d'une proposition pédagogique ; les crédits et la validation institutionnelle relèvent de l'établissement.

**Prérequis :** utiliser un système de fichiers, installer un logiciel, calculer proportions et moyennes, lire un graphique. Aucun prérequis Python. Pour les chapitres IA/sciences : rappels de vecteurs, dérivées et probabilité ; un tutorat de remise à niveau est prévu.

## 2. Compétences observables

| Code | À l'issue du module, l'étudiant peut… | Preuve attendue |
|---|---|---|
| C1 | Formaliser entrées, sorties, invariants et coût d'un algorithme | Pseudocode, trace manuelle, justification O(n) |
| C2 | Écrire fonctions, collections et classes avec erreurs contrôlées | Programme Python relu et tests de cas limites |
| C3 | Lire, valider, stocker et visualiser des mesures | Import atomique, requêtes SQL, graphique légendé |
| C4 | Choisir un outil Python adapté au domaine | Comparatif justifié et exemple minimal |
| C5 | Entraîner/évaluer un modèle simple sans contamination du test | Découpage documenté, baseline et métrique |
| C6 | Intégrer interface, stockage, calcul et événements | Application PyQt5 fonctionnelle et persistante |
| C7 | Évaluer limites, reproductibilité et sûreté d'un logiciel | Rapport de tests, limites, documentation opérateur |

## 3. Progression et résultats de séance

Chaque ligne représente **2 h CM + 2 h TD + 2 h TP**. Les références exactes et le code sont dans les chapitres associés depuis le [sommaire](README.md).

| Séance | Contenu essentiel | Livrable de TP | Compétences |
|---|---|---|---|
| 1 | Problème, pseudocode, variables, types, expressions | Calcul de masse documenté | C1, C2 |
| 2 | if/elif/else, for/while, list/dict/set, complexité | Filtrage et agrégation de mesures | C1, C2 |
| 3 | Fonctions, portée, paramètres, modules, exceptions | Fonction GMQ et jeu de tests manuel | C2 |
| 4 | Classes, dataclasses, composition, UML, polymorphisme | Modèle Animal/Pesée | C2, C6 |
| 5 | CSV/JSON, SQLite, transactions, unittest, Git | Dépôt local avec import robuste | C2, C3, C7 |
| 6 | ndarray, DataFrame, jointures, manquants, chunks | Pipeline tabulaire reproductible | C3, C4 |
| 7 | Descriptif, distributions, Matplotlib et Seaborn | Deux figures commentées | C3, C7 |
| 8 | Régression, classification, train/test, Pipeline | Modèle scikit-learn évalué | C4, C5 |
| 9 | Réseau dense, tensors, autograd, entraînement | Démonstration PyTorch/TensorFlow | C4, C5 |
| 10 | Paquets, chiffrement authentifié, secrets | Analyse hors ligne et token Fernet | C4, C7 |
| 11 | HTTP, JSON, FastAPI, Flask, Django, ORM | API locale validant une mesure | C3, C4, C6 |
| 12 | Microcontrôleur, Linux embarqué, GPIO, passerelle | Contrat capteur et import CSV | C4, C6, C7 |
| 13 | SciPy, ODE, filtrage, échantillonnage | Simulation RC et oscillateur | C3, C4, C7 |
| 14 | PyQt5, événements, stockage, KPI, intégration | Démonstration du projet couplé | C1–C7 |

Le projet commence dès la séance 3 : le calcul GMQ devient le premier service métier ; les séances suivantes alimentent ses couches. L'intégration finale ne doit pas commencer la veille de la soutenance.

## 4. Modalités pédagogiques

Les cours alternent une définition, un exemple résolu puis une variation demandée à l'étudiant. Les TD utilisent des traces de variables et des contre-exemples. Les TP exigent l'exécution du code et un résultat archivé. Les travaux d'IA sont effectués sur des données synthétiques ou autorisées et séparent erreur de programmation, erreur de mesure et incertitude du modèle.

Travail en binôme conseillé : un développeur et un relecteur permutent à chaque séance. L'utilisation d'agents IA est autorisée comme aide pédagogique ; joindre les prompts utiles, indiquer les corrections humaines et expliquer le code livré à l'oral. Aucune donnée d'exploitation confidentielle n'est nécessaire.

## 5. Évaluation

| Épreuve | Poids | Critères |
|---|---:|---|
| Contrôle algorithmique individuel | 20 % | Formalisation, trace, terminaison, complexité |
| Dossier de TP | 30 % | Exécution, qualité des données, figures, interprétation |
| Projet intégré | 40 % | Fonctions, calculs, architecture, tests, documentation |
| Soutenance individuelle | 10 % | Démonstration, justification et maîtrise des limites |

Pour le projet : calculs/unités 20 pts, stockage/intégrité 15, interface 15, temps et tâches 10, capteurs/alertes 10, assistant/évaluation 10, tests 10, documentation/reproductibilité 10. La note du projet est sur 100 puis pondérée à 40 %. Les modalités de rattrapage suivent le règlement de l'établissement.

## 6. Ressources et accompagnement

Un ordinateur sans GPU suffit au noyau du module et au projet final. L'installation Deep Learning est optionnelle et isolée ; un ESP32 et un Raspberry Pi sont facultatifs. En leur absence, conserver le même schéma de données avec un simulateur. Les versions et commandes sont documentées dans les README, avec distinction entre exemples vérifiés et matériel non testé.

Adaptations : possibilité de travailler en console avant l'interface, captures accompagnées d'un texte alternatif, schémas vectoriels agrandissables, consignes de TP avec sorties attendues. Prévoir une séance de remédiation sur les types et les fonctions avant le passage aux bibliothèques.
