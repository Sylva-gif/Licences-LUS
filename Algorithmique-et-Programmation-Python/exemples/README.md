# Exemples exécutables et environnements

Les commandes suivantes sont lancées depuis `Algorithmique-et-Programmation-Python/`. Le projet Qt dispose de son propre [README](../projet-elevage/README.md) et ne nécessite pas les dépendances scientifiques.

## Socle : chapitres 1 à 5

Python 3.11 ou 3.12 suffit, sans paquet supplémentaire :

```bash
python exemples/01_bases.py
python exemples/02_collections.py
python exemples/03_fonctions.py
python exemples/04_objets.py
python exemples/05_stockage.py
```

## Data, visualisation, ML, cybersécurité, Web et sciences

Créer un environnement dédié. Sous Windows, remplacer `.venv-exemples/bin/python` par `.venv-exemples\Scripts\python.exe`.

```bash
python -m venv .venv-exemples
.venv-exemples/bin/python -m pip install -r exemples/requirements.txt
.venv-exemples/bin/python exemples/06_data.py
.venv-exemples/bin/python exemples/07_visualisation.py
.venv-exemples/bin/python exemples/08_ml.py
.venv-exemples/bin/python exemples/10_cyber.py
.venv-exemples/bin/python exemples/11_api.py
.venv-exemples/bin/python exemples/11_flask.py
.venv-exemples/bin/python exemples/12_simulateur.py
.venv-exemples/bin/python exemples/13_sciences.py
```

Les figures et le CSV simulé sont générés dans `exemples/sorties/`, ignoré par Git. Les scripts API utilisent des clients de test et n'ouvrent pas de serveur public. Le TP Scapy n'émet aucun paquet. Le [guide Django](11_django.md) décrit une installation séparée et un projet à créer par l'étudiant.

## Deep Learning optionnel

Pour vérifier Django sans créer de portail complet : `python -m pip install 'Django>=5.2,<5.3'`, puis `python exemples/11_django.py` dans l'environnement dédié. Le script utilise une base en mémoire et teste une route JSON ainsi que l'unicité d'un identifiant.

Installer un seul backend dans un environnement séparé afin de ne pas imposer ses paquets volumineux au socle. Les commandes CPU sont indicatives pour une version de Python supportée ; consulter les sélecteurs officiels pour une installation GPU et les contraintes système.

```bash
python -m venv .venv-torch
.venv-torch/bin/python -m pip install torch
.venv-torch/bin/python exemples/09_pytorch.py
```

```bash
python -m venv .venv-tensorflow
.venv-tensorflow/bin/python -m pip install tensorflow
.venv-tensorflow/bin/python exemples/09_tensorflow.py
```

Pas de dataset à télécharger : les deux scripts créent leurs données synthétiques. Consigner les versions installées et les métriques. Voir [PyTorch](https://pytorch.org/get-started/locally/) et [TensorFlow](https://www.tensorflow.org/install/pip) pour la compatibilité de plateforme. Ces deux exemples ne sont pas des dépendances du projet PyQt5.

## IoT

`12_simulateur.py` s'exécute sur PC avec la bibliothèque standard. `12_esp32_micropython.py` requiert une carte, son firmware MicroPython, un DHT22 et un câblage adapté. `12_raspberry_gpio.py` requiert Raspberry Pi, GPIO Zero et une entrée de contact compatible. Ne pas lancer les deux scripts matériels dans l'environnement PC en espérant simuler le matériel.

## Schémas

```bash
python outils/generer_schemas.py
```

Le générateur ne télécharge aucune ressource ; il régénère les 14 SVG déterministes. Les résultats réellement exécutés et les limites sont consignés dans [VERIFICATION.md](../VERIFICATION.md).
