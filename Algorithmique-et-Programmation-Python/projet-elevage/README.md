# Élevage connecté — projet intégrateur PyQt5

Application locale opérationnelle pour le module **Algorithmique et Programmation Python**. Une base représente un projet d'élevage. L'interface couvre les animaux, les pesées, l'alimentation, le budget de temps des tâches, les mesures environnementales et l'aide à la décision. Les données d'exemple sont entièrement synthétiques.

## Démarrer en cinq minutes

Prévoir Python **3.11 ou 3.12**, un environnement de bureau Windows, Linux ou macOS et une connexion pour la première installation. Aucune clé d'API ni carte électronique n'est nécessaire. Les commandes suivantes sont exécutées dans `projet-elevage/`.

### Windows PowerShell

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py --demo
```

### Linux / macOS

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python main.py --demo
```

Si Python 3.12 n'est pas installé sous Windows, utiliser un interpréteur 3.11 installé et remplacer `-3.12` par `-3.11`. L'environnement n'a pas besoin d'être activé. Sur Linux, Qt nécessite les bibliothèques système de bureau/XCB adaptées à la distribution ; l'erreur « xcb plugin » signale généralement une dépendance système manquante. `QT_QPA_PLATFORM=offscreen` sert uniquement aux tests sans écran.

## Parcours de démonstration

1. Démarrer avec `--demo`. Trois bovins, quatre pesées chacun, 21 jours de consommation et deux tâches sont créés si la base ne contient aucun animal.
2. Dans **Tableau de bord**, sélectionner BOV-001 : GMQ attendu **800 g/j**, IC **5 kg/kg**. La température simulée de 31 °C dépasse le seuil d'exemple de 30 °C.
3. Sélectionner BOV-002 puis BOV-003 : GMQ respectifs **250** et **−100 g/j**. Une perte de poids produit un IC indisponible, jamais un rendement négatif affiché comme normal.
4. Dans **Projet et temps**, démarrer puis arrêter « Contrôle des abreuvoirs ». Le temps réel et son écart au budget sont recalculés. Marquer la tâche terminée.
5. Dans **Capteurs IoT**, simuler une mesure ou importer le CSV de `data/`. Un CSV ancien doit afficher une alerte d'ancienneté, pas une alerte thermique actuelle.
6. Dans **Assistant IA local**, demander un bilan de croissance, puis « quel est le temps des tâches ? ». Le texte expose les valeurs, la méthode et ses limites.
7. Dans **Animaux et pesées**, exporter les poids en CSV, puis fermer et rouvrir : les données persistent.

## Fonctions livrées et limites

| Livré et exécutable | Extension proposée aux étudiants |
|---|---|
| Interface PyQt5, six onglets, courbe des poids | Gestion multi-utilisateurs et authentification |
| SQLite, validations, clés étrangères, doublons refusés | Historique des corrections, audit et migrations |
| Animaux, pesées, consommation journalière | Lots homogènes, sorties, mortalité, achats et coûts |
| GMQ, IC, alertes par seuil et fraîcheur | Référentiels par espèce, âge et objectif d'élevage |
| Tâches, budget minutes, chronomètre, clôture | Jalons, responsables, Gantt, reprise après panne |
| Simulation et import de mesures CSV | Ingestion MQTT/HTTPS authentifiée en continu |
| Assistant à règles + régression OLS locale | Modèle validé sur plusieurs élevages, LLM optionnel |

Le logiciel constitue un **démonstrateur pédagogique à thème industriel**, utilisable immédiatement pour les TP. Il n'est pas une solution industrielle certifiée : aucun pilotage d'actionneur, aucune prescription vétérinaire, aucun cloud et aucune authentification intégrée. L'assistant n'est pas un chatbot génératif : il route les questions de temps vers les tâches et les autres questions vers le bilan animal. La régression apprend réellement sa pente sur l'historique disponible, mais n'est pas validée pour des décisions d'exploitation.

## Architecture et fichiers

| Fichier | Responsabilité |
|---|---|
| `main.py` | Arguments, démarrage, fermeture, test d'affichage |
| `elevage/domain.py` | GMQ, IC et régression linéaire sans interface |
| `elevage/storage.py` | Schéma SQL, transactions, import/export et jeu démo |
| `elevage/assistant.py` | Alertes explicables, fraîcheur, projection et texte |
| `elevage/ui.py` | Vues, signaux/slots, chronomètre et graphique Qt |
| `tests/test_project.py` | Calculs, stockage, imports et parcours Qt |
| `data/capteurs-exemple.csv` | Exemple de contrat d'entrée IoT |

![Architecture de l'application](../images/14-projet.svg)

## Formules et conventions

- **GMQ (g/j)** = 1 000 × (dernier poids kg − premier poids kg) / jours écoulés. Un seul point donne `N/D` ; les dates sont triées ; les pesées du même jour sont refusées.
- **IC (kg/kg)** = consommation totale kg / gain de poids kg. Les consommations couvrent chaque journée de `[date première pesée, date dernière pesée[`. Cette convention suppose une pesée en début de journée. L'aliment du jour de la dernière pesée est exclu. Si un jour manque ou si le gain est nul/négatif : `N/D`.
- **Temps** : durée en secondes mesurée avec une horloge monotone Qt, puis affichée en minutes. L'écart = réel − prévu ; un nombre positif signifie un dépassement.
- **Projection** : moindres carrés ordinaires sur au moins trois dates ; horizon de 7 jours après la dernière pesée. Le RMSE décrit l'ajustement aux données utilisées, pas la performance future.
- **Alertes** : seuils éditables, valeurs initiales purement pédagogiques ; capteur ancien après 30 min, pesée ancienne après 7 jours. Les seuils sont communs au projet : utiliser des projets homogènes.

## Données, sauvegarde et incidents

La base par défaut est `ElevageConnecte/elevage.sqlite3` dans le dossier personnel. Le lancement suivant ouvre un projet distinct :

```bash
python main.py --db ./autre-projet.sqlite3 --demo
```

Pour sauvegarder, fermer l'application normalement et copier ce fichier. Pour restaurer, ouvrir la copie avec `--db`. Le CSV de pesées ne remplace pas la sauvegarde complète. Ne pas envoyer de base contenant des données réelles dans Git. Le chronomètre sauvegarde à l'arrêt et à la fermeture normale ; une coupure brutale peut perdre la session active. Les autres saisies validées sont immédiatement enregistrées.

Les doublons ne remplacent jamais silencieusement une donnée. La version initiale ne propose pas d'édition/suppression dans l'interface : le TP d'extension exige une confirmation, un journal d'audit et une transaction. En cas de saisie erronée pendant une démonstration, utiliser une nouvelle base de test. Ne pas modifier une base réelle sans sauvegarde et procédure de correction.

### Contrat CSV IoT

UTF-8, virgules, en-tête exact `barn,measured_at,temperature,humidity`, maximum 2 Mo. `measured_at` est une date ISO 8601 avec fuseau ; températures en °C ; humidité relative en %. Les dates futures au-delà de cinq minutes sont refusées. La paire bâtiment/horodatage est unique. L'import est atomique : si une ligne ou un doublon échoue, aucune ligne du lot n'est conservée.

Les mesures de `data/capteurs-exemple.csv` sont fixes et donc éventuellement anciennes. Le bouton de simulation génère des mesures à l'heure actuelle. Une future passerelle peut produire ce même CSV ; les chapitres IoT et Web expliquent comment remplacer ensuite ce transport par un service authentifié.

## Vérification

```bash
python -m unittest discover -s tests -v
python main.py --db :memory: --demo --smoke
```

Sur un serveur Linux sans écran :

```bash
QT_QPA_PLATFORM=offscreen python -m unittest discover -s tests -v
QT_QPA_PLATFORM=offscreen python main.py --db :memory: --demo --smoke
```

Les tests couvrent notamment les unités, les dates, les poids non finis, les données manquantes, les clés étrangères, les imports invalides, le rollback, les formules CSV, les capteurs périmés, la persistance et la fermeture du chronomètre. Voir le [rapport de vérification](../VERIFICATION.md).

## Cadre de distribution

PyQt5 est fourni sous licence GPL/commerciale : consulter [Riverbank](https://www.riverbankcomputing.com/software/pyqt/) avant une redistribution propriétaire. Aucune licence globale n'est ajoutée au dépôt existant. Les commandes ci-dessus exécutent les sources ; la génération d'un installateur Windows/macOS/Linux constitue un TP de déploiement, pas un livrable binaire déjà fourni.
