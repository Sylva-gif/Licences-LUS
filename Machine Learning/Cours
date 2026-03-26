# Machine Learning : de débutant à expert

## Table des matières

1. [Introduction](#introduction)
2. [IA, Machine Learning, Deep Learning : bien distinguer](#ia-machine-learning-deep-learning--bien-distinguer)
3. [Les grands types d'apprentissage](#les-grands-types-dapprentissage)
4. [Le cycle complet d'un projet ML](#le-cycle-complet-dun-projet-ml)
5. [Les bases mathématiques indispensables](#les-bases-mathématiques-indispensables)
6. [Données, features et prétraitement](#données-features-et-prétraitement)
7. [Évaluation des modèles](#évaluation-des-modèles)
8. [Apprentissage supervisé](#apprentissage-supervisé)
9. [Apprentissage non supervisé](#apprentissage-non-supervisé)
10. [Apprentissage par renforcement](#apprentissage-par-renforcement)
11. [Deep Learning et réseaux de neurones](#deep-learning-et-réseaux-de-neurones)
12. [Des modèles classiques aux LLM et Transformers](#des-modèles-classiques-aux-llm-et-transformers)
13. [MLOps et mise en production](#mlops-et-mise-en-production)
14. [ML responsable, biais et gestion du risque](#ml-responsable-biais-et-gestion-du-risque)
15. [Bibliothèques Python essentielles](#bibliothèques-python-essentielles)
16. [Exemple de pipeline professionnel en Python](#exemple-de-pipeline-professionnel-en-python)
17. [Erreurs fréquentes à éviter](#erreurs-fréquentes-à-éviter)
18. [Feuille de route : passer de débutant à expert](#feuille-de-route--passer-de-débutant-à-expert)
19. [Mini-projets pour monter en niveau](#mini-projets-pour-monter-en-niveau)
20. [Conclusion](#conclusion)

---

## Introduction

Le Machine Learning (ML), ou apprentissage automatique, est une sous-discipline de l'intelligence artificielle qui permet à des systèmes d'apprendre à partir de données, sans être explicitement programmés règle par règle. L'idée centrale est de construire un modèle mathématique qui capte des régularités dans les données pour faire des prédictions, prendre des décisions ou découvrir des structures cachées. C'est exactement l'esprit présenté dans ton cours, qui introduit aussi le lien entre IA, ML, Deep Learning, NLP, vision par ordinateur et IA générative. *Cours fourni*

L'objectif de ce document n'est pas seulement de t'expliquer des définitions, mais de te donner une vision progressive, rigoureuse et pratique : comprendre les concepts, savoir choisir un algorithme, éviter les erreurs classiques, construire un pipeline professionnel, et enfin raisonner comme un praticien expérimenté du ML. *Machine Learning Crash Course - Google* | *CS229 Stanford Notes*

---

## IA, Machine Learning, Deep Learning : bien distinguer

L'intelligence artificielle est le domaine général qui vise à construire des systèmes capables de réaliser des tâches associées à l'intelligence humaine : perception, compréhension, décision, génération de contenu, etc. Le Machine Learning est une branche de l'IA dans laquelle les performances du système s'améliorent grâce aux données. Le Deep Learning est une sous-catégorie du ML reposant sur des réseaux de neurones profonds, très performants pour les images, le texte, l'audio et les données massives. Ton cours présente aussi le NLP (traitement du langage naturel), la vision par ordinateur et l'IA générative comme grandes familles d'applications modernes de l'IA. *Cours fourni*

En pratique, on peut voir une hiérarchie simple :

- **IA** : domaine global
- **ML** : apprentissage à partir de données
- **DL** : apprentissage à l'aide de réseaux neuronaux profonds

Cette distinction est essentielle, car un bon ingénieur ML doit savoir qu'un problème ne nécessite pas toujours du deep learning. Très souvent, des modèles classiques bien conçus et bien évalués sont plus rapides, plus simples et plus robustes en production. *Machine Learning Crash Course - Google* | *Production ML systems - Google*

---

## Les grands types d'apprentissage

### 1. Apprentissage supervisé

L'apprentissage supervisé repose sur des données étiquetées : chaque exemple d'entrée X est associé à une sortie y. Le but est d'apprendre une fonction f(X)→y. Ton cours distingue correctement les deux grands cas : régression si la cible est continue, et classification si la cible est une catégorie. *Cours fourni*

Exemples :
- prédire le prix d'une maison
- détecter si un email est spam
- diagnostiquer un patient malade/sain
- prédire la consommation d'énergie

### 2. Apprentissage non supervisé

L'apprentissage non supervisé travaille sur des données sans labels. Le but n'est plus de prédire une cible connue, mais de découvrir une structure cachée : groupes, similarités, dimensions latentes, anomalies. Ton cours cite notamment K-Means, le clustering hiérarchique et la PCA. *Cours fourni*

Exemples :
- segmentation client
- détection d'anomalies
- exploration de données
- regroupement de documents similaires

### 3. Apprentissage par renforcement

En Reinforcement Learning (RL), un agent interagit avec un environnement, choisit des actions, reçoit des récompenses positives ou négatives, puis apprend une politique qui maximise la récompense cumulée. Ton cours le relie aux jeux vidéo, à la robotique et aux véhicules autonomes. *Cours fourni*

### 4. Vision experte

Un débutant classe souvent les problèmes par "algorithme". Un expert commence par les classer par type d'information disponible :

- labels complets → supervisé
- pas de labels → non supervisé
- interaction séquentielle avec récompense → renforcement
- données massives non structurées avec forte complexité → souvent deep learning

C'est cette capacité de cadrage qui fait gagner du temps et évite de mauvais choix techniques. *Machine Learning Crash Course - Google*

---

## Le cycle complet d'un projet ML

Ton cours donne un très bon schéma des étapes d'un projet ML : collecte, prétraitement, analyse exploratoire, choix du modèle, entraînement, évaluation, ajustement, déploiement. C'est une excellente base. *Cours fourni*

Je te propose une version plus experte du pipeline :

### 1. Compréhension du problème métier

Avant tout modèle, il faut répondre à :
- quelle décision veut-on améliorer ?
- quelle variable cible ?
- quel coût métier d'une erreur ?
- quelles contraintes de temps, latence, explicabilité, budget ?

Un bon projet ML commence rarement par "quel algorithme utiliser ?", mais plutôt par "quel problème décisionnel veut-on résoudre ?". *Production ML systems - Google*

### 2. Collecte et qualité des données

Les données peuvent venir de bases SQL, CSV, APIs, capteurs, logs, formulaires, images, texte ou flux temps réel. La qualité des données détermine souvent davantage la performance finale que le choix du modèle. *Cours fourni* | *Production ML systems - Google*

### 3. Analyse exploratoire (EDA)

On cherche à comprendre :
- la distribution des variables
- les valeurs manquantes
- les outliers
- les corrélations
- le déséquilibre de classes
- les risques de fuite d'information

### 4. Prétraitement

Le prétraitement comprend nettoyage, imputation, encodage, mise à l'échelle, sélection de variables, éventuellement réduction de dimension. *Cours fourni* | *Scikit-learn preprocessing*

### 5. Découpage train / validation / test

On sépare les données pour mesurer la généralisation. Cette étape doit être faite avant certains traitements afin d'éviter la fuite de données. *Scikit-learn common pitfalls*

### 6. Entraînement

Le modèle apprend ses paramètres sur l'ensemble d'entraînement.

### 7. Validation et tuning

On ajuste les hyperparamètres par validation croisée, recherche sur grille, recherche aléatoire ou optimisation bayésienne.

### 8. Évaluation finale

On mesure sur un jeu de test jamais vu.

### 9. Déploiement

Un modèle utile n'est pas seulement précis, il doit être :
- déployable
- monitorable
- reproductible
- maintenable
- robuste au drift

### 10. Monitoring et amélioration continue

Une fois en production, le vrai travail commence : dérive des données, baisse des performances, retours utilisateurs, nouvelles contraintes métier. *Production ML systems - Google*

---

## Les bases mathématiques indispensables

Pour passer de débutant à expert, il faut sortir de la simple recette "fit() puis predict()". Un vrai niveau expert repose sur des fondations mathématiques solides. Les notes de Stanford insistent particulièrement sur l'algèbre linéaire, le calcul matriciel, l'optimisation, la régularisation, la validation croisée et le compromis biais/variance. *CS229 Stanford Notes*

### 1. Algèbre linéaire

À maîtriser :
- vecteurs, matrices, dimensions
- produit scalaire
- multiplication matricielle
- transpose
- rang
- valeurs propres / vecteurs propres
- décomposition matricielle

Pourquoi ? Parce que les données tabulaires, les transformations, la PCA, les réseaux de neurones et les noyaux s'écrivent tous naturellement en notation matricielle. *CS229 Stanford Notes*

### 2. Calcul différentiel

Il faut comprendre :
- dérivées simples
- gradients
- dérivées partielles
- dérivées matricielles
- Hessienne (à un niveau avancé)

Pourquoi ? Parce que l'entraînement d'un modèle revient souvent à minimiser une fonction de coût. La descente de gradient et les méthodes de Newton sont des outils centraux en ML. *CS229 Stanford Notes*

### 3. Probabilités et statistiques

À connaître :
- variables aléatoires
- espérance, variance
- covariance, corrélation
- loi normale
- estimation
- intervalle de confiance
- vraisemblance
- Bayes

Pourquoi ? Parce que classifieurs probabilistes, incertitude, calibration, bruit, régularisation, validation croisée et généralisation s'appuient tous dessus. *CS229 Stanford Notes*

### 4. Optimisation

Notions clés :
- fonction de perte
- minimum local / global
- descente de gradient
- learning rate
- régularisation
- contraintes
- dualité de Lagrange

Ces notions deviennent critiques pour comprendre les SVM, les régressions régularisées et le deep learning. *CS229 Stanford Notes*

### 5. Compromis biais / variance

- **biais élevé** → modèle trop simple, sous-apprentissage
- **variance élevée** → modèle trop sensible aux données, surapprentissage

Un expert sait diagnostiquer rapidement si le problème vient du modèle, des données, du prétraitement ou de l'évaluation. *CS229 Stanford Notes*

---

## Données, features et prétraitement

Ton cours insiste sur le rôle des features, de la cible, du dataset et du nettoyage. C'est fondamental. *Cours fourni*

### 1. Features et target

- **Features** : variables d'entrée
- **Target** : variable à prédire
- **Dataset** : ensemble des observations

Un modèle n'apprend jamais "la réalité", il apprend une relation entre une représentation des données et une cible.

### 2. Principaux prétraitements

D'après la documentation officielle scikit-learn, les transformations les plus courantes sont :
- standardisation
- min-max scaling
- normalisation
- transformations non linéaires
- encodage catégoriel
- discrétisation
- imputation des valeurs manquantes
- génération de variables polynomiales
- transformateurs personnalisés

*Scikit-learn preprocessing*

### 3. Pourquoi la mise à l'échelle est importante

De nombreux algorithmes supposent que les features sont comparables en ordre de grandeur. Sans cela, une variable peut dominer la fonction objectif. C'est particulièrement important pour les modèles linéaires régularisés, les SVM et les méthodes basées sur les distances comme KNN. *Scikit-learn preprocessing*

### 4. Encodage des variables catégorielles

Pour les variables qualitatives, on utilise souvent :
- `OrdinalEncoder` si l'ordre a un sens
- `OneHotEncoder` sinon
- parfois un encodage cible pour des cardinalités élevées, avec prudence

*Scikit-learn preprocessing*

### 5. Imputation des valeurs manquantes

Il faut distinguer :
- suppression de lignes/colonnes
- imputation simple (moyenne, médiane, mode)
- imputation plus sophistiquée

Le choix dépend du volume de données manquantes et du mécanisme qui les génère.

### 6. Feature engineering

Le feature engineering reste un des leviers les plus puissants en ML classique :
- ratios
- interactions
- agrégations
- transformations log
- binning
- variables temporelles
- embeddings dans des cas avancés

*Machine Learning Crash Course - Google*

---

## Évaluation des modèles

Évaluer un modèle ne consiste pas à regarder un seul score. Il faut choisir une métrique cohérente avec le problème métier. La documentation scikit-learn recense les métriques majeures pour classification et régression, et rappelle qu'il faut interpréter correctement les conventions de score, surtout lorsque certaines erreurs sont renvoyées en version négative pour être compatibles avec l'API de scoring. *Scikit-learn model evaluation*

### 1. En régression

Métriques classiques :
- **MAE** : erreur absolue moyenne
- **MSE** : erreur quadratique moyenne
- **RMSE** : racine de l'erreur quadratique moyenne
- **R²** : part de variance expliquée

*Scikit-learn model evaluation*

Ton cours met particulièrement en avant MSE, RMSE et R², ce qui est tout à fait pertinent pour débuter. *Cours fourni*

### 2. En classification

Métriques majeures :
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Average Precision
- Log Loss

*Scikit-learn model evaluation*

### 3. Attention au déséquilibre de classes

Si 95 % des exemples sont négatifs, un modèle qui prédit toujours "négatif" peut avoir 95 % d'accuracy et pourtant être inutile. Dans ce cas, il faut regarder plutôt :
- recall
- precision
- F1
- PR-AUC
- balanced accuracy

*Scikit-learn model evaluation*

### 4. Validation croisée

La validation croisée permet d'estimer plus robustement la capacité de généralisation et aide au choix d'hyperparamètres. Elle est explicitement liée à la sélection de modèle dans les notes de Stanford. *CS229 Stanford Notes*

---

## Apprentissage supervisé

### Régression linéaire

Ton cours introduit la régression linéaire simple sous la forme y=ax+b, avec fonction de coût, descente de gradient et métriques associées. C'est la meilleure porte d'entrée pour comprendre la logique d'un modèle supervisé. *Cours fourni*

**Intuition**

On cherche la droite qui approxime au mieux la relation entre une feature et une cible continue.

**Forme générale**

$$\hat{y} = w_1 x_1 + w_2 x_2 + \cdots + w_n x_n + b$$

**Fonction de coût**

$$J(w, b) = \frac{1}{m} \sum_{i=1}^{m} \left( \hat{y}^{(i)} - y^{(i)} \right)^2$$

**Avantages**
- simple
- interprétable
- rapide
- bon baseline

**Limites**
- suppose une relation linéaire
- sensible aux outliers
- moins performant sur relations complexes

---

### Régression logistique

Même si son nom contient "régression", c'est un modèle de classification, souvent binaire. Le cours et les ressources Google la placent logiquement après la régression linéaire. *Cours fourni* | *Machine Learning Crash Course - Google*

**Intuition**

On prédit une probabilité P(y=1|x), puis on applique un seuil.

**Fonction sigmoïde**

$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

**Atouts**
- simple
- probabiliste
- interprétable
- excellente baseline pour classification tabulaire

**Limites**
- frontière linéaire dans l'espace des features d'origine
- dépend fortement de la qualité du feature engineering

---

### K-Nearest Neighbors (KNN)

Ton cours annonce un chapitre dédié à KNN, et la documentation scikit-learn précise bien ses principes et limites. *Cours fourni* | *Scikit-learn neighbors*

**Principe**

Pour prédire un nouveau point, on regarde ses k voisins les plus proches :
- en classification : vote majoritaire
- en régression : moyenne des valeurs voisines

*Scikit-learn neighbors*

**Forces**
- très intuitif
- non paramétrique
- peut bien fonctionner avec des frontières irrégulières

*Scikit-learn neighbors*

**Faiblesses**
- coûteux en mémoire
- lent si beaucoup de données
- sensible à l'échelle des variables
- souffre de la malédiction de la dimensionnalité

*Scikit-learn neighbors*

**Hyperparamètres clés**
- `n_neighbors`
- `weights`
- `metric`
- `algorithm`

*Scikit-learn neighbors*

---

### Support Vector Machines (SVM)

Ton cours annonce également un chapitre SVM, et la documentation officielle en donne une vue très claire. *Cours fourni* | *Scikit-learn SVM*

**Principe**

Le SVM cherche un hyperplan qui sépare au mieux les classes en maximisant la marge. Les points les plus proches de la frontière sont les vecteurs de support. *Scikit-learn SVM*

**Noyaux (kernel trick)**

Quand les données ne sont pas linéairement séparables, on peut utiliser des noyaux :
- linéaire
- polynomial
- RBF
- sigmoïde

*Scikit-learn SVM*

**Forces**
- efficace en grande dimension
- bon pour petits/moyens jeux de données
- très puissant avec bon choix de noyau

*Scikit-learn SVM*

**Limites**
- coûteux sur grands volumes
- réglage délicat
- nécessite souvent une bonne mise à l'échelle
- probabilités non natives ou coûteuses à calibrer

*Scikit-learn SVM*

**Hyperparamètres clés**
- `C`
- `kernel`
- `gamma`
- `degree`
- `class_weight`

*Scikit-learn SVM*

---

### Arbres de décision

Ton cours inclut un chapitre sur les Decision Trees, et scikit-learn rappelle bien leurs avantages et limites. *Cours fourni* | *Scikit-learn tree*

**Principe**

Un arbre construit des règles de décision successives du type :
- si x₁ < seuil, aller à gauche
- sinon, aller à droite

On obtient une partition de l'espace en régions. *Scikit-learn tree*

**Forces**
- très interprétables
- peu de prétraitement
- gèrent bien les non-linéarités
- utiles pour expliquer une logique métier

*Scikit-learn tree*

**Limites**
- facilement surappris
- instables
- mauvaises extrapolations
- sensibles aux petites variations de données

*Scikit-learn tree*

**Hyperparamètres clés**
- `max_depth`
- `min_samples_split`
- `min_samples_leaf`
- `ccp_alpha`

*Scikit-learn tree*

---

### Ensembles : Random Forest et boosting

Ton cours cite déjà les Random Forests parmi les algorithmes supervisés. Une vision experte consiste à comprendre qu'un arbre seul est souvent fragile, alors qu'un ensemble d'arbres est souvent beaucoup plus robuste. *Cours fourni*

**Random Forest**

Agrège plusieurs arbres entraînés sur des sous-échantillons / sous-espaces de features.

Effet :
- variance plus faible
- meilleure robustesse
- très bon baseline tabulaire

**Gradient Boosting / XGBoost / LightGBM / CatBoost**

Construit les arbres séquentiellement pour corriger les erreurs précédentes.

Effet :
- souvent excellent sur données tabulaires structurées
- tuning plus fin
- grande puissance prédictive

> **Règle experte :** sur des données tabulaires propres, les ensembles d'arbres sont très souvent parmi les meilleurs candidats.

---

## Apprentissage non supervisé

### K-Means

Ton cours prévoit un chapitre sur le clustering et K-Means. Scikit-learn le présente comme l'un des algorithmes les plus classiques. *Cours fourni* | *Scikit-learn clustering / K-Means*

**Principe**

K-Means cherche à partitionner les données en K groupes en minimisant l'inertie intra-cluster. L'algorithme alterne :
1. initialisation des centroïdes
2. affectation des points au centroïde le plus proche
3. recalcul des centroïdes
4. répétition jusqu'à convergence

*Scikit-learn clustering / K-Means*

**Forces**
- simple
- rapide
- efficace sur grands jeux de données
- bon premier choix pour clustering "compact"

*Scikit-learn clustering / K-Means*

**Limites**
- il faut choisir K
- suppose des clusters plutôt convexes/isotropes
- sensible à l'initialisation et aux outliers
- moins bon pour formes complexes

*Scikit-learn clustering / K-Means*

**Hyperparamètres clés**
- `n_clusters`
- `init`
- `n_init`
- `max_iter`

*Scikit-learn clustering / K-Means*

---

### PCA et réduction de dimension

Ton cours cite la PCA comme méthode non supervisée. Son but est de projeter les données dans un espace de plus faible dimension tout en conservant un maximum de variance. *Cours fourni*

Pourquoi c'est utile :
- visualiser
- débruiter
- compresser
- accélérer certains modèles
- limiter certaines redondances

Un expert n'utilise jamais la PCA "par réflexe" : il vérifie si la réduction améliore réellement la généralisation ou seulement la visualisation.

---

### Détection d'anomalies

Dans de nombreux contextes, le but n'est pas de classer toutes les observations mais de détecter les cas rares :
- fraude
- intrusion
- panne
- capteur défaillant
- transaction suspecte

C'est un domaine important où les labels sont souvent rares ou biaisés.

---

## Apprentissage par renforcement

Le Reinforcement Learning est conceptuellement très différent du supervisé. On y trouve :
- un agent
- un environnement
- des états
- des actions
- des récompenses
- une politique

*Cours fourni*

C'est particulièrement utile lorsque les décisions sont séquentielles, c'est-à-dire quand une action influence les états futurs :
- jeux
- robotique
- allocation de ressources
- pilotage autonome

> **Point expert important :** le RL est puissant, mais coûteux, instable, et souvent difficile à industrialiser. Il ne faut pas l'utiliser quand un bon modèle supervisé ou une optimisation classique suffit.

---

## Deep Learning et réseaux de neurones

Google présente les réseaux de neurones comme des architectures capables d'apprendre automatiquement des relations non linéaires sans dépendre autant du feature engineering manuel. *Neural Networks - Google*

### 1. Pourquoi les réseaux de neurones ?

Quand la relation entre variables est très complexe, des modèles linéaires ou des croisements de variables manuels deviennent insuffisants. Les réseaux apprennent eux-mêmes des représentations adaptées. *Neural Networks - Google*

### 2. Composants

- neurones
- couches cachées
- poids
- biais
- fonction d'activation
- rétropropagation
- fonction de perte

*Neural Networks - Google*

### 3. À comprendre avant d'aller plus loin

Avant le deep learning moderne, il faut déjà maîtriser :
- régression linéaire
- régression logistique
- gradient descent
- surapprentissage
- généralisation
- prétraitement

*Neural Networks - Google*

### 4. Usages typiques

- vision par ordinateur
- NLP
- audio
- séries temporelles complexes
- recommandation
- multimodal

---

## Des modèles classiques aux LLM et Transformers

Google rappelle qu'un language model estime la probabilité d'un token ou d'une séquence de tokens, et montre la progression historique depuis les N-grams vers les RNN, puis vers les modèles plus modernes capables de capturer le contexte à grande échelle. *LLM Intro - Google*

### 1. Concepts de base

- **token** : unité de texte (mot, sous-mot, caractère)
- **contexte** : information autour du token
- **modèle de langage** : prédit le token suivant ou évalue une séquence

*LLM Intro - Google*

### 2. De N-grams à Transformers

- **N-grams** : simples mais contexte limité
- **RNN** : meilleur contexte mais limites sur longues dépendances
- **Transformers** : traitement du contexte global bien plus puissant

*LLM Intro - Google*

### 3. Lien avec ton parcours ML

Pour vraiment comprendre les LLM, il faut déjà maîtriser :
- probabilités
- optimisation
- embeddings
- réseaux de neurones
- généralisation
- évaluation

*Machine Learning Crash Course - Google* | *LLM Intro - Google*

> **Conseil expert :** ne saute pas directement aux LLM sans maîtriser d'abord le ML classique. Les meilleurs ingénieurs IA comprennent les fondations avant les architectures "à la mode".

---

## MLOps et mise en production

L'un des messages les plus importants de Google est que, dans un vrai système ML en production, le modèle lui-même ne représente souvent qu'une petite partie du système total. La collecte de données, la validation, la gestion des ressources, le monitoring et l'infrastructure de serving occupent une place énorme. *Production ML systems - Google*

### 1. Composants d'un système ML pro

- collecte des données
- vérification des données
- extraction/serving des features
- orchestration
- entraînement
- validation
- déploiement
- monitoring
- infrastructure

*Production ML systems - Google*

### 2. Ce qu'un expert surveille

- dérive des features
- dérive de la cible
- latence
- disponibilité
- coût de calcul
- biais
- performance par segment
- reproductibilité

### 3. Pourquoi MLOps est crucial

Un bon modèle dans un notebook n'est pas un produit. Le niveau expert, c'est :
- versionner les données et le code
- reproduire les expériences
- industrialiser les pipelines
- monitorer le comportement réel
- prévoir le réentraînement

---

## ML responsable, biais et gestion du risque

Le NIST AI Risk Management Framework rappelle qu'un système d'IA doit être conçu, développé, utilisé et évalué avec une logique de gestion du risque et de fiabilité. Le framework vise à améliorer la confiance dans les systèmes d'IA et à intégrer des considérations de "trustworthiness" dès la conception. *NIST AI RMF*

### 1. Risques importants

- biais dans les données
- discrimination
- opacité
- erreurs sur populations rares
- vulnérabilités de sécurité
- dérive dans le temps
- mauvaise gouvernance

*NIST AI RMF*

### 2. Bonnes pratiques

- documenter les données
- documenter les limites du modèle
- tester par sous-groupes
- monitorer les effets réels
- prévoir des garde-fous humains
- tenir compte du contexte d'usage

*NIST AI RMF*

### 3. Niveau expert

Un expert ne demande pas seulement "mon modèle est-il précis ?"

Il demande aussi :
- est-il juste ?
- est-il stable ?
- est-il explicable ?
- est-il sûr ?
- est-il conforme à l'usage prévu ?

---

## Bibliothèques Python essentielles

Ton cours couvre déjà les bibliothèques de base : NumPy, Pandas, Matplotlib et Scikit-learn. C'est exactement la bonne base pour démarrer sérieusement. *Cours fourni*

### NumPy

Pour les tableaux, matrices, opérations numériques et la base du calcul scientifique en Python. *Cours fourni*

### Pandas

Pour charger, nettoyer, manipuler et analyser les données tabulaires avec les DataFrame. *Cours fourni*

### Matplotlib

Pour la visualisation simple et pédagogique : histogrammes, scatter plots, courbes, etc. *Cours fourni*

### Scikit-learn

Pour les modèles ML classiques, le prétraitement, les pipelines, la validation croisée, les métriques et le tuning. *Cours fourni* | *Scikit-learn documentation*

### En avançant

Ajoute ensuite :
- **Seaborn** pour la visualisation
- **XGBoost / LightGBM / CatBoost** pour le tabulaire avancé
- **PyTorch** ou **TensorFlow** pour le deep learning
- **MLflow / Weights & Biases** pour le tracking
- **FastAPI** pour l'exposition d'un modèle en API

---

## Exemple de pipeline professionnel en Python

Voici un exemple simple mais propre de pipeline ML pour une tâche de classification tabulaire. L'idée importante n'est pas juste le modèle, mais la bonne structure : séparation des colonnes, encodage, scaling, pipeline, évaluation. Les ressources scikit-learn recommandent fortement `Pipeline` et `ColumnTransformer` pour éviter la fuite de données et rendre le workflow reproductible. *Scikit-learn compose* | *Scikit-learn common pitfalls*

```python
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score

# 1) Charger les données
df = pd.read_csv("data.csv")

# 2) Définir features et target
X = df.drop(columns=["target"])
y = df["target"]

# 3) Séparer avant tout apprentissage de transformation
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4) Identifier types de colonnes
num_cols = X.select_dtypes(include=["int64", "float64"]).columns
cat_cols = X.select_dtypes(include=["object", "category", "bool"]).columns

# 5) Prétraitement numérique
numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

# 6) Prétraitement catégoriel
categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

# 7) Fusion des transformations
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, num_cols),
        ("cat", categorical_transformer, cat_cols)
    ]
)

# 8) Pipeline complet
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000))
])

# 9) Entraînement
model.fit(X_train, y_train)

# 10) Prédiction
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

# 11) Évaluation
print(classification_report(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_proba))
```

**Pourquoi ce code est "propre" :**
- split avant d'ajuster les transformations
- imputation cohérente
- encodage et scaling encapsulés
- pipeline unique reproductible
- moins de risque de fuite de données

*Scikit-learn compose* | *Scikit-learn common pitfalls*

---

## Erreurs fréquentes à éviter

Scikit-learn identifie explicitement plusieurs anti-patterns majeurs. Les connaître tôt te fera gagner énormément de temps. *Scikit-learn common pitfalls*

### 1. Prétraitement incohérent

Faire un `fit_transform()` sur train et un autre `fit_transform()` indépendant sur test est une erreur fréquente. Le test doit recevoir uniquement `transform()`. *Scikit-learn common pitfalls*

### 2. Fuite de données

Utiliser des statistiques calculées sur l'ensemble complet avant séparation train/test donne des performances artificiellement optimistes. *Scikit-learn common pitfalls*

### 3. Mauvais choix de métrique

Optimiser l'accuracy sur un dataset très déséquilibré peut être trompeur. *Scikit-learn model evaluation*

### 4. Oublier la baseline

Toujours comparer à :
- un modèle simple
- une règle naïve
- un arbre simple
- une régression logistique
- une forêt aléatoire de base

### 5. Chercher la complexité trop tôt

Un expert commence souvent par un modèle simple et explicable avant de passer au boosting ou au deep learning.

### 6. Négliger la qualité des données

Beaucoup d'échecs ML viennent plus des données que de l'algorithme.

### 7. Ignorer le contexte métier

Un modèle très précis mais inutilisable en production n'a pas de valeur.

---

## Feuille de route : passer de débutant à expert

### Niveau 1 — Débutant

**Objectif : comprendre les bases.**

- Python, NumPy, Pandas
- visualisation
- types de ML
- régression linéaire
- classification binaire
- train/test split
- métriques simples

*Cours fourni*

### Niveau 2 — Intermédiaire

**Objectif : construire des projets propres.**

- preprocessing
- pipelines
- cross-validation
- KNN, SVM, arbres
- K-Means, PCA
- tuning d'hyperparamètres
- interprétation des erreurs

*Scikit-learn preprocessing* | *Scikit-learn compose*

### Niveau 3 — Avancé

**Objectif : raisonner mathématiquement et comparer des approches.**

- biais/variance
- régularisation
- optimisation
- ensembles
- calibration
- analyse par segments
- gestion du déséquilibre

*CS229 Stanford Notes*

### Niveau 4 — Expert

**Objectif : industrialiser et concevoir.**

- MLOps
- monitoring
- drift
- gouvernance
- fairness
- coût/latence
- design de systèmes ML
- arbitrage entre ML classique, DL, LLM, heuristiques

*Production ML systems - Google* | *NIST AI RMF*

---

## Mini-projets pour monter en niveau

Voici une progression pratique cohérente avec ton cours et avec une montée en difficulté réelle.

### Projet 1 — Régression linéaire

Prédire le prix d'un bien immobilier à partir de la surface, du nombre de pièces, du quartier.

**Compétences :** EDA, régression, RMSE, R².

### Projet 2 — Classification binaire

Prédire spam / non spam ou malade / sain.

**Compétences :** précision, rappel, F1, matrice de confusion.

### Projet 3 — KNN et SVM

Comparer KNN, SVM et Logistic Regression sur un même dataset.

**Compétences :** scaling, hyperparamètres, biais/variance.

### Projet 4 — Arbres et forêts

Construire un modèle pour accorder ou refuser un crédit.

**Compétences :** explicabilité, feature importance, surapprentissage.

### Projet 5 — Clustering

Segmenter des clients avec K-Means.

**Compétences :** choix de K, inertie, interprétation business.

### Projet 6 — Pipeline pro

Construire un pipeline scikit-learn complet avec :
- imputation
- encodage
- scaling
- modèle
- cross-validation
- export du modèle

### Projet 7 — Deep Learning

Classifier des images simples (MNIST/CIFAR-like).

**Compétences :** réseaux de neurones, backpropagation, surapprentissage.

### Projet 8 — MLOps léger

Déployer un modèle avec FastAPI et suivre les prédictions/logs.

**Compétences :** industrialisation, API, monitoring.

---

## Conclusion

Le Machine Learning ne consiste pas à mémoriser une liste d'algorithmes. C'est une discipline qui combine modélisation mathématique, qualité des données, évaluation rigoureuse, vision métier, ingénierie logicielle et gestion du risque. Ton cours te donne une bonne base sur les types de ML, les étapes d'un projet, la régression linéaire, les bibliothèques Python et les principaux algorithmes comme KNN, SVM, arbres et K-Means. Les ressources externes permettent ensuite d'aller vers un niveau professionnel : pipelines, prévention de la fuite de données, généralisation, deep learning, LLM, MLOps et IA responsable. *Cours fourni* | *Scikit-learn common pitfalls* | *CS229 Stanford Notes* | *Production ML systems - Google* | *NIST AI RMF*

Si tu maîtrises vraiment les points suivants, tu changes de niveau :

- bien cadrer un problème,
- préparer proprement les données,
- choisir les bonnes métriques,
- comparer des baselines,
- éviter la fuite de données,
- comprendre le biais/variance,
- industrialiser un pipeline,
- raisonner en termes de risque et d'impact.

*Scikit-learn compose* | *Scikit-learn common pitfalls* | *NIST AI RMF*

---

## Sources utilisées

- Ton document de cours : *Tout cours Machine Learning*
- Google ML Crash Course : https://developers.google.com/machine-learning/crash-course
- Google Neural Networks : https://developers.google.com/machine-learning/crash-course/neural-networks
- Google Intro to LLMs : https://developers.google.com/machine-learning/crash-course/llm
- Google Production ML Systems : https://developers.google.com/machine-learning/crash-course/production-ml-systems
- Scikit-learn preprocessing : https://scikit-learn.org/stable/modules/preprocessing.html
- Scikit-learn model evaluation : https://scikit-learn.org/stable/modules/model_evaluation.html
- Scikit-learn neighbors : https://scikit-learn.org/stable/modules/neighbors.html
- Scikit-learn SVM : https://scikit-learn.org/stable/modules/svm.html
- Scikit-learn decision trees : https://scikit-learn.org/stable/modules/tree.html
- Scikit-learn K-Means : https://scikit-learn.org/stable/modules/clustering.html#k-means
- Scikit-learn compose / pipelines : https://scikit-learn.org/stable/modules/compose.html
- Scikit-learn common pitfalls : https://scikit-learn.org/stable/common_pitfalls.html
- Stanford CS229 Notes : https://cs229.stanford.edu/main_notes.pdf
- NIST AI Risk Management Framework : https://www.nist.gov/itl/ai-risk-management-framework
