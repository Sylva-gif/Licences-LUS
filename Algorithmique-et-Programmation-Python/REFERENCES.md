# Références officielles et lectures complémentaires

Les exemples et illustrations de ce dossier sont originaux. Les documentations ci-dessous servent à vérifier les API et à approfondir les notions ; elles évoluent indépendamment du cours. Vérification documentaire effectuée le **24 septembre 2026** sur une sélection des guides principaux. Les références ne constituent pas une promesse de compatibilité de toutes leurs versions futures.

| Domaine | Documentation officielle | Usage dans le module |
|---|---|---|
| Python | [Tutoriel](https://docs.python.org/3/tutorial/), [bibliothèque standard](https://docs.python.org/3/library/) | Syntaxe, types, fonctions, classes et fichiers |
| Tests | [unittest](https://docs.python.org/3/library/unittest.html) | Assertions et scénarios de non-régression |
| SQLite | [sqlite3](https://docs.python.org/3/library/sqlite3.html) | Connexions, paramètres et transactions |
| NumPy | [Guide utilisateur](https://numpy.org/doc/stable/user/) | Tableaux, forme, type et opérations |
| Pandas | [Tutoriels](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html) | DataFrame, groupby, nettoyage et jointures |
| Big Data | [Dask](https://docs.dask.org/en/stable/), [PySpark](https://spark.apache.org/docs/latest/api/python/) | Approfondissement distribué, non requis au socle |
| Graphiques | [Matplotlib](https://matplotlib.org/stable/users/explain/quick_start.html), [Seaborn](https://seaborn.pydata.org/tutorial.html) | Figures, axes et grammaire statistique |
| Machine Learning | [scikit-learn : pièges courants](https://scikit-learn.org/stable/common_pitfalls.html) | Pipelines, prétraitement et fuite de données |
| PyTorch | [Boucle d'optimisation](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html) | Perte, gradients, train/eval |
| TensorFlow | [Démarrage Keras](https://www.tensorflow.org/tutorials/quickstart/beginner) | Couches, compilation et entraînement |
| Réseau | [Scapy](https://scapy.readthedocs.io/en/latest/usage.html) | Paquets en couches et analyse locale |
| Cryptographie | [Fernet](https://cryptography.io/en/latest/fernet/) | Chiffrement authentifié et gestion des erreurs |
| API | [FastAPI](https://fastapi.tiangolo.com/tutorial/) | Contrats, validation et tests |
| Web léger | [Flask](https://flask.palletsprojects.com/en/stable/quickstart/) | Routage et réponses JSON |
| Web intégré | [Django 5.2](https://docs.djangoproject.com/en/5.2/intro/tutorial01/) | Projet, vues, modèles et migrations |
| Microcontrôleurs | [MicroPython ESP32](https://docs.micropython.org/en/latest/esp32/quickref.html) | machine.Pin, capteurs et limites de plateforme |
| Raspberry Pi | [GPIO Zero](https://gpiozero.readthedocs.io/en/stable/), [GPIO Raspberry Pi](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio) | Entrées/sorties et contraintes de câblage |
| SciPy | [solve_ivp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html), [signal](https://docs.scipy.org/doc/scipy/tutorial/signal.html) | Équations différentielles et filtres |
| Interface | [Guide PyQt5](https://www.riverbankcomputing.com/static/Docs/PyQt5/) | Widgets, signaux et slots |

## Repères bibliographiques

Pour prolonger : un ouvrage d'algorithmique pour invariants et complexité ; un ouvrage de méthodes numériques pour les erreurs de discrétisation ; un ouvrage d'apprentissage statistique pour biais/variance et validation. Les chapitres donnent les notions nécessaires aux TP sans prétendre remplacer ces disciplines.

Le projet calcule des indicateurs arithmétiques usuels avec des conventions explicitement définies. Il ne fournit pas de référentiel normatif de croissance animale ni de recommandations vétérinaires. Les valeurs de seuil sont uniquement des paramètres de démonstration.
