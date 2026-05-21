# SOC INTELLIGENT — Dashboard IDS (NSL-KDD)

Résumé
------
Ce projet fournit un tableau de bord Streamlit pour la détection d'intrusions réseau (IDS) entraîné sur le dataset NSL‑KDD. Il combine deux modèles scikit‑learn : Random Forest et SVM (noyau RBF). L'interface permet d'explorer des statistiques globales, de visualiser les performances et de simuler des prédictions en temps réel.

Structure du dépôt
------------------
- `app.py` : Interface Streamlit (frontend). Lancez avec `streamlit run app.py`.
- `main.py` : Script d'entraînement / préparation (génère les modèles, préprocesseur et métriques).
- `KDDTrain+.txt`, `KDDTest+.txt` : Fichiers NSL‑KDD (datasets).
- `requirements.txt` : Dépendances Python.
- `models/` : Contient les artefacts ML générés par `main.py` :
  - `random_forest_model.joblib`
  - `svm_model.joblib`
  - `preprocessor.joblib`
  - `metrics.joblib`
  - `test_data.joblib`

Prérequis
---------
- Python 3.8+ installé
- Sur Windows, utilisez PowerShell ou un terminal compatible

Installation
------------
Créez un environnement virtuel (recommandé) puis installez les dépendances :

```bash
python -m venv .venv
.\.venv\Scripts\activate      # Windows PowerShell
pip install -r requirements.txt
```

Génération / Entraînement des modèles
-------------------------------------
Avant d'utiliser l'interface, exécutez `main.py` pour préparer les données et entraîner/sauvegarder les modèles :

```bash
python main.py
```

Ce script doit générer les fichiers dans le dossier `models/`. Si `models/` est vide, `app.py` affichera des messages d'alerte indiquant que les modèles sont manquants.

Lancer l'interface Streamlit
---------------------------
Après installation et entraînement, démarrez le dashboard :

```bash
streamlit run app.py
```

Utilisation du dashboard
------------------------
- Barre latérale : indique l'état des composants (modèles, préprocesseur, dataset) et permet de sélectionner le modèle actif (Random Forest ou SVM).
- Section 01 — Vue d'ensemble : statistiques et graphiques sur le dataset NSL‑KDD (répartition normal/attaque, top types d'attaques, etc.).
- Section 02 — Performances : affiche accuracy, precision, recall, f1 et un radar comparatif si `metrics.joblib` est présent.
- Section 03 — Simulation : formulaire pour saisir des features (durée, protocole, service, bytes, flag, etc.) et bouton **ANALYSER** pour obtenir une prédiction et la confiance.
- Exemples pré‑définis : tests rapides (HTTP normal, DoS SYN, Brute Force FTP).

Comportement attendu
---------------------
- Si `models/` ou les fichiers de dataset sont absents, l'interface indique comment lancer `main.py` pour créer ces artefacts.
- Les prédictions passent par la fonction `predire(...)` dans `app.py` qui applique le même préprocesseur que pour l'entraînement.

Dépannage rapide
----------------
- Erreur "Modèles non chargés" : exécutez `python main.py` puis rechargez la page Streamlit.
- Erreur de `joblib.load` : vérifiez que les fichiers `.joblib` existent et ne sont pas corrompus.
- Erreur liée au préprocesseur (`preprocessor.transform`) : assurez‑vous que `main.py` a sauvegardé un préprocesseur compatible et que les colonnes d'entrée correspondent.

Bonnes pratiques
----------------
- Toujours lancer `main.py` après modification des étapes d'entraînement.
- Travailler dans un environnement virtuel pour isoler les dépendances.

Contribuer
----------
- Ouvrez une issue pour signaler un bug ou proposer une amélioration.
- Pour contributions de code : forkez, créez une branche et proposez une Pull Request.

Licence
-------
- Licence : MIT (adaptez selon vos besoins)

---
