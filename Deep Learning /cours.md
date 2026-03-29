# Cours complet de Deep Learning 

## Table des matières

1. [Introduction](#introduction)
2. [Qu'est-ce que le Deep Learning ?](#quest-ce-que-le-deep-learning-)
3. [Prérequis indispensables](#prérequis-indispensables)
4. [Du neurone artificiel au réseau profond](#du-neurone-artificiel-au-réseau-profond)
5. [Les briques mathématiques essentielles](#les-briques-mathématiques-essentielles)
6. [Propagation avant, fonction de perte et backpropagation](#propagation-avant-fonction-de-perte-et-backpropagation)
7. [Optimisation : comment un réseau apprend](#optimisation--comment-un-réseau-apprend)
8. [Prétraitement des données et pipeline pratique](#prétraitement-des-données-et-pipeline-pratique)
9. [Overfitting, régularisation et stabilité d'entraînement](#overfitting-régularisation-et-stabilité-dentraînement)
10. [Architectures fondamentales](#architectures-fondamentales)
11. [Convolutional Neural Networks (CNN)](#convolutional-neural-networks-cnn)
12. [Réseaux séquentiels, RNN et limites](#réseaux-séquentiels-rnn-et-limites)
13. [Attention, Transformers et LLM](#attention-transformers-et-llm)
14. [Workflow pratique avec PyTorch et TensorFlow](#workflow-pratique-avec-pytorch-et-tensorflow)
15. [Debugging et bonnes pratiques expertes](#debugging-et-bonnes-pratiques-expertes)
16. [Évaluation, généralisation et mise en production](#évaluation-généralisation-et-mise-en-production)
17. [Feuille de route pour passer de débutant à expert](#feuille-de-route-pour-passer-de-débutant-à-expert)
18. [Mini-projets recommandés](#mini-projets-recommandés)
19. [Conclusion](#conclusion)
20. [Sources](#sources)

---

## Introduction

Le **Deep Learning** est une branche du Machine Learning qui repose sur des réseaux de neurones artificiels composés de plusieurs couches capables d'apprendre automatiquement des représentations complexes à partir des données. Il est particulièrement puissant lorsque les relations entre les variables sont non linéaires et difficiles à capturer par des modèles classiques. Les cours introductifs de Google présentent justement les réseaux de neurones comme des architectures capables de découvrir automatiquement des motifs non linéaires dans les données, là où un modèle linéaire seul serait insuffisant. [Source](https://developers.google.com/machine-learning/crash-course/neural-networks)

Ce document a pour objectif de te faire progresser **du niveau débutant au niveau expert**, en allant des concepts les plus simples jusqu'aux architectures modernes comme les CNN, les Transformers et les LLM. Il combine une vision théorique, des intuitions mathématiques, des bonnes pratiques d'entraînement et une lecture orientée ingénierie. [Source](https://developers.google.com/machine-learning/crash-course/neural-networks)

![Problème non linéaire motivant les réseaux de neurones](https://developers.google.com/static/machine-learning/crash-course/neural-networks/images/nonlinear_simple.png)
*Illustration d'un problème non linéaire qu'un simple modèle linéaire ne sépare pas correctement.* [Source](https://developers.google.com/machine-learning/crash-course/neural-networks)

---

## Qu'est-ce que le Deep Learning ?

Le Deep Learning est une sous-discipline du Machine Learning dans laquelle on empile plusieurs couches de calcul afin que le modèle apprenne lui-même des représentations hiérarchiques. Une couche basse peut apprendre des motifs simples, puis les couches suivantes composent ces motifs pour former des structures de plus en plus abstraites. Cette idée est au cœur des réseaux profonds modernes. [Source](https://cs231n.github.io/neural-networks-1/)

L'avantage principal du Deep Learning est qu'il réduit le besoin de fabriquer manuellement des variables complexes. Au lieu de construire à la main des croisements de variables, le réseau apprend lui-même ces combinaisons pendant l'entraînement. C'est l'une des idées mises en avant par le Machine Learning Crash Course de Google. [Source](https://developers.google.com/machine-learning/crash-course/neural-networks)

En pratique, le Deep Learning est devenu central dans :
- la vision par ordinateur,
- le traitement du langage naturel,
- la reconnaissance vocale,
- la recommandation,
- l'IA générative,
- les modèles de fondation et les LLM. [Source](http://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html)

---

## Prérequis indispensables

Avant d'attaquer sérieusement le Deep Learning, il faut déjà bien comprendre plusieurs fondations du Machine Learning classique : régression linéaire, régression logistique, classification, surapprentissage, types de données numériques et catégorielles, ainsi que l'idée générale de fonction de perte et d'optimisation. Google précise explicitement que ces notions sont des prérequis naturels avant d'aborder les réseaux de neurones. [Source](https://developers.google.com/machine-learning/crash-course/neural-networks)

Sur le plan technique, il faut aussi être à l'aise avec :
- Python,
- les tableaux et tenseurs,
- l'algèbre linéaire de base,
- les dérivées,
- les probabilités élémentaires,
- la lecture de courbes de loss et d'accuracy. [Source](https://cs231n.github.io/neural-networks-1/)

Un étudiant qui saute ces bases apprend souvent à utiliser une bibliothèque sans comprendre ce qu'il entraîne réellement. Un futur expert, au contraire, sait relier le code, les mathématiques et le comportement du modèle. [Source](https://cs231n.stanford.edu/slides/2025/lecture_4.pdf)

---

## Du neurone artificiel au réseau profond

Le neurone artificiel prend des entrées, effectue une combinaison linéaire pondérée, ajoute un biais puis applique une fonction d'activation. Cette idée s'inspire de façon simplifiée du neurone biologique, mais le modèle computationnel moderne s'interprète surtout comme un bloc mathématique : produit scalaire, biais, puis non-linéarité. [Source](https://cs231n.github.io/neural-networks-1/)

Dans un réseau entièrement connecté, plusieurs neurones sont organisés en couches. Une couche transforme son entrée par une multiplication matricielle, un biais, puis une activation. D'après CS231n, une couche fully connected se résume à une opération matricielle suivie d'une fonction d'activation, et l'empilement de couches permet de construire des fonctions très riches. [Source](https://cs231n.github.io/neural-networks-1/)

Sans non-linéarité, empiler plusieurs couches linéaires ne sert à rien : tout se réduit à une seule transformation linéaire équivalente. C'est donc l'activation qui donne au réseau sa capacité à modéliser des frontières de décision complexes. [Source](https://cs231n.github.io/neural-networks-1/)

![Modèle de neurone artificiel](https://cs231n.github.io/assets/nn1/neuron_model.jpeg)
*Le neurone artificiel combine entrées, poids, biais et fonction d'activation.* [Source](https://cs231n.github.io/neural-networks-1/)

![Exemple d'architecture multicouche](https://cs231n.github.io/assets/nn1/neural_net2.jpeg)
*Exemple d'un réseau de neurones multicouche.* [Source](https://cs231n.github.io/neural-networks-1/)

---

## Les briques mathématiques essentielles

### 1. Vecteurs, matrices et tenseurs

En Deep Learning, les données et les paramètres sont représentés par des **tenseurs**. Un vecteur est un tenseur 1D, une matrice un tenseur 2D, et une image couleur peut être représentée comme un tenseur 3D. Les frameworks modernes comme PyTorch structurent tout le workflow autour de ces objets. [Source](https://pytorch.org/tutorials/beginner/basics/intro.html)

### 2. Fonctions d'activation

Les activations apportent la non-linéarité. Dans la pratique moderne, **ReLU** est souvent privilégiée, et CS231n recommande explicitement son usage régulier, tout en mentionnant Leaky ReLU comme variante utile. [Source](https://cs231n.github.io/neural-networks-1/)

Quelques activations courantes :
- **Sigmoïde** : utile pour sorties probabilistes binaires,
- **Tanh** : centrée mais aujourd'hui moins dominante,
- **ReLU** : très utilisée car simple et efficace,
- **Leaky ReLU / variantes** : pour réduire le problème des neurones morts.

### 3. Fonction de perte

Un réseau apprend en minimisant une **fonction de perte**. Pour une classification multi-classe, une loss de type softmax / cross-entropy est standard. Pour la régression, on utilise souvent une MSE ou MAE selon le problème. La loss est le signal central qui guide l'optimisation. [Source](https://cs231n.github.io/neural-networks-2/)

### 4. Approximation universelle

CS231n rappelle qu'un réseau avec au moins une couche cachée est un approximateur universel. Cela veut dire qu'en théorie il peut approximer une très grande classe de fonctions continues, mais en pratique la profondeur, l'optimisation et la structure du problème comptent énormément. [Source](https://cs231n.github.io/neural-networks-1/)

---

## Propagation avant, fonction de perte et backpropagation

### Propagation avant

La **forward pass** consiste à faire circuler les données d'entrée dans le réseau jusqu'à la sortie. Chaque couche applique sa transformation, et l'ensemble du modèle produit une prédiction. [Source](https://cs231n.github.io/neural-networks-1/)

### Backpropagation

La **backpropagation** est l'application récursive de la règle de la chaîne à travers un graphe computationnel. Les slides de Stanford insistent sur le fait qu'il faut comprendre les gradients amont, les gradients locaux, et la manière dont le gradient traverse différents types d'opérations. [Source](https://cs231n.stanford.edu/slides/2025/lecture_4.pdf)

Parmi les idées essentielles à maîtriser :
- la règle de la chaîne,
- le gradient local d'une opération,
- le gradient reçu depuis l'aval,
- la composition de ces gradients jusqu'aux paramètres,
- le fait qu'en pratique on ne forme pas explicitement les Jacobiennes complètes quand elles sont creuses. [Source](https://cs231n.stanford.edu/slides/2025/lecture_4.pdf)

Un étudiant qui comprend vraiment la backpropagation comprend pourquoi l'entraînement peut échouer, pourquoi un gradient peut exploser ou disparaître, et pourquoi certaines architectures sont plus faciles à optimiser que d'autres. [Source](https://cs231n.stanford.edu/slides/2025/lecture_4.pdf)

---

## Optimisation : comment un réseau apprend

Les paramètres d'un réseau sont appris en minimisant la fonction de perte grâce à des algorithmes d'optimisation. CS231n recommande notamment **SGD avec Nesterov Momentum** ou **Adam** comme choix pratiques fréquents. [Source](https://cs231n.github.io/neural-networks-3/)

### 1. Descente de gradient

L'idée générale est simple : on calcule le gradient de la perte par rapport aux paramètres, puis on met à jour les poids dans le sens opposé au gradient.

### 2. Batch, mini-batch et epochs

L'entraînement moderne se fait presque toujours par **mini-batches**, ce qui permet un bon compromis entre stabilité, coût mémoire et vitesse de calcul. [Source](https://pytorch.org/tutorials/beginner/basics/intro.html)

### 3. Learning rate

Le **learning rate** est l'hyperparamètre le plus critique. Trop petit, l'apprentissage est lent. Trop grand, la loss diverge ou oscille. CS231n recommande de diminuer progressivement le learning rate au cours de l'entraînement, par exemple lorsque la performance de validation plafonne. [Source](https://cs231n.github.io/neural-networks-3/)

### 4. Heuristiques expertes

Quelques règles précieuses :
- commencer simple,
- surveiller la courbe de loss à chaque époque,
- tester si le réseau peut surapprendre un très petit sous-ensemble,
- faire une recherche d'hyperparamètres sur une échelle logarithmique,
- préférer souvent la recherche aléatoire à la grille classique. [Source](https://cs231n.github.io/neural-networks-3/)

![Effet du learning rate sur la loss](https://cs231n.github.io/assets/nn3/learningrates.jpeg)
*Des learning rates différents produisent des comportements d'entraînement très différents.* [Source](https://cs231n.github.io/neural-networks-3/)

---

## Prétraitement des données et pipeline pratique

Un bon modèle profond commence rarement par l'architecture ; il commence par de bonnes données. CS231n recommande de **centrer les données autour de zéro** et de **normaliser leur échelle**, par exemple vers une plage comparable, avant l'entraînement. [Source](https://cs231n.github.io/neural-networks-2/)

Principes importants :
- calculer les statistiques de normalisation uniquement sur le train,
- réutiliser ces mêmes statistiques pour validation et test,
- éviter toute fuite de données,
- documenter les transformations pour les reproduire en production. [Source](https://cs231n.github.io/neural-networks-2/)

Dans la pratique, un pipeline de Deep Learning comprend généralement :
1. chargement des données,
2. transformations,
3. batching,
4. définition du modèle,
5. entraînement,
6. évaluation,
7. sauvegarde du modèle. [Source](https://pytorch.org/tutorials/beginner/basics/intro.html)

![Pipeline de prétraitement](https://cs231n.github.io/assets/nn2/prepro1.jpeg)
*Le prétraitement est une étape structurelle, pas un détail optionnel.* [Source](https://cs231n.github.io/neural-networks-2/)

---

## Overfitting, régularisation et stabilité d'entraînement

Le Deep Learning manipule souvent des modèles à très grande capacité. Sans garde-fous, ils peuvent mémoriser le train au lieu de généraliser. Pour contrôler cela, plusieurs techniques sont recommandées.

### 1. Régularisation L2

CS231n recommande largement la **régularisation L2** comme mécanisme standard pour limiter la croissance excessive des poids. [Source](https://cs231n.github.io/neural-networks-2/)

### 2. Dropout

Le **dropout** désactive aléatoirement une partie des neurones pendant l'entraînement, ce qui réduit la co-adaptation et améliore souvent la généralisation. CS231n le recommande explicitement, notamment en combinaison avec L2. [Source](https://cs231n.github.io/neural-networks-2/)

### 3. Batch Normalization

La **Batch Normalization** stabilise l'apprentissage en contrôlant mieux la distribution des activations. Elle aide aussi à réduire la sensibilité à l'initialisation et rend l'entraînement plus robuste. [Source](https://cs231n.github.io/neural-networks-2/)

### 4. Initialisation des poids

Pour les réseaux avec ReLU, CS231n recommande l'initialisation de He, basée sur un écart-type de \(\sqrt{2/n}\), où \(n\) est le nombre d'entrées du neurone. Une bonne initialisation évite que les activations et les gradients ne deviennent trop petits ou trop grands dès le départ. [Source](https://cs231n.github.io/neural-networks-2/)

### 5. Diagnostic train/validation

Comparer train et validation reste l'un des diagnostics les plus puissants :
- train très bon, validation mauvaise → surapprentissage,
- train et validation faibles → capacité insuffisante ou mauvaise optimisation,
- train et validation proches et fortes → situation saine. [Source](https://cs231n.github.io/neural-networks-3/)

![Concept du dropout](https://cs231n.github.io/assets/nn2/dropout.jpeg)
*Le dropout aide à limiter la dépendance excessive entre neurones.* [Source](https://cs231n.github.io/neural-networks-2/)

![Courbes train/validation et capacité](https://cs231n.github.io/assets/nn3/accuracies.jpeg)
*L'écart entre train et validation est un signal essentiel pour diagnostiquer l'overfitting.* [Source](https://cs231n.github.io/neural-networks-3/)

---

## Architectures fondamentales

### 1. Réseaux fully connected

Ce sont les réseaux de base. Ils conviennent surtout aux données tabulaires ou à de petits problèmes pédagogiques. Ils permettent de comprendre les briques fondamentales du Deep Learning. [Source](https://cs231n.github.io/neural-networks-1/)

### 2. Réseaux profonds

Les réseaux modernes comportent beaucoup plus de couches et parfois des centaines de millions de paramètres. CS231n note qu'en pratique, les architectures modernes sont profondes et que la régularisation et l'optimisation sont souvent plus importantes que la simple réduction de taille du modèle. [Source](https://cs231n.github.io/neural-networks-1/)

### 3. Choisir une architecture

Un expert choisit l'architecture selon la structure des données :
- images → CNN ou Vision Transformer,
- texte → Transformer ou variantes,
- séries séquentielles → RNN/Transformers selon contexte,
- tabulaire → souvent modèles ML classiques, parfois MLP dans des cas particuliers.

---

## Convolutional Neural Networks (CNN)

Les **CNN** sont les architectures historiques majeures pour la vision par ordinateur. Leur force est d'exploiter explicitement la structure des images. CS231n explique que les CNN supposent que l'entrée est une image et encodent cette structure dans l'architecture, ce qui réduit fortement le nombre de paramètres tout en restant performant. [Source](https://cs231n.github.io/convolutional-networks/)

### Briques de base

Un CNN repose surtout sur :
- des couches de convolution,
- des couches de pooling,
- des couches fully connected en sortie selon le cas. [Source](https://cs231n.github.io/convolutional-networks/)

### Pourquoi les CNN marchent bien sur les images

Ils utilisent :
- la **connectivité locale**,
- le **partage de paramètres**,
- une forme d'**invariance à la translation**,
- une hiérarchie de motifs allant des bords simples vers les objets complexes. [Source](https://cs231n.github.io/convolutional-networks/)

### Hyperparamètres centraux

Pour les convolutions, il faut comprendre :
- le nombre de filtres,
- la taille des filtres,
- le stride,
- le padding. [Source](https://cs231n.github.io/convolutional-networks/)

![Réseau classique vs ConvNet](https://cs231n.github.io/assets/cnn/cnn.jpeg)
*Comparaison entre réseau dense classique et réseau convolutionnel adapté aux images.* [Source](https://cs231n.github.io/convolutional-networks/)

![Connectivité locale et champ réceptif](https://cs231n.github.io/assets/cnn/depthcol.jpeg)
*Les CNN exploitent une connectivité locale et un champ réceptif adapté aux images.* [Source](https://cs231n.github.io/convolutional-networks/)

---

## Réseaux séquentiels, RNN et limites

Avant l'essor des Transformers, les **RNN** ont été une architecture majeure pour traiter les séquences. Google rappelle qu'ils offrent davantage de contexte que les modèles N-gram, car ils parcourent les tokens un à un et accumulent progressivement de l'information contextuelle. [Source](https://developers.google.com/machine-learning/crash-course/llm)

Cependant, Google souligne aussi leurs limites : le contexte réellement exploitable reste restreint, et leur entraînement souffre notamment du problème de **vanishing gradients** sur des dépendances longues. [Source](https://developers.google.com/machine-learning/crash-course/llm)

Les RNN restent utiles à connaître pour la culture technique, mais les architectures modernes à base d'attention ont pris une place dominante dans de nombreux usages NLP et multimodaux. [Source](http://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html)

---

## Attention, Transformers et LLM

Le mécanisme d'**attention** est l'une des évolutions majeures du Deep Learning moderne. Dive into Deep Learning explique que les notions fondamentales sont celles de **queries, keys et values**, combinées avec des fonctions de scoring comme le dot product et le scaled dot product. [Source](http://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html)

### 1. Pourquoi l'attention ?

L'attention permet à un modèle de se concentrer sur les parties les plus pertinentes d'une séquence lorsqu'il calcule une représentation. Elle améliore fortement la gestion du contexte par rapport aux approches purement récurrentes. [Source](http://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html)

### 2. Self-attention

La **self-attention** permet à chaque token de regarder les autres tokens de la séquence, ce qui donne un accès global au contexte. C'est une différence majeure avec les RNN, qui traitent l'information de façon plus séquentielle. [Source](http://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html)

### 3. Positional encoding

Comme les Transformers ne lisent pas naturellement les tokens dans un ordre séquentiel comme un RNN, ils ont besoin d'un **codage positionnel** pour représenter la position des éléments dans la séquence. [Source](http://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html)

### 4. Architecture Transformer

D2L décrit les grands composants :
- multi-head attention,
- self-attention,
- positional encoding,
- réseaux feed-forward par position,
- connexions résiduelles,
- normalisation de couche,
- blocs encodeur et décodeur. [Source](http://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html)

### 5. LLM

Google définit un **language model** comme un modèle qui estime la probabilité d'un token ou d'une séquence de tokens dans un contexte donné. Les LLM étendent cette idée à grande échelle et produisent des capacités avancées de génération, résumé, traduction et raisonnement linguistique. [Source](https://developers.google.com/machine-learning/crash-course/llm)

### 6. Vision Transformer et modèles modernes

D2L relie aussi l'attention aux architectures modernes de vision et au préentraînement à grande échelle, montrant que les Transformers ne sont plus limités au texte. [Source](http://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html)

---

## Workflow pratique avec PyTorch et TensorFlow

### PyTorch

Le tutoriel d'introduction de PyTorch résume très bien le workflow standard : travailler avec les données, définir un modèle, optimiser ses paramètres et sauvegarder le modèle entraîné. Il met aussi en avant les concepts de tensors, datasets, dataloaders, autograd et optimisation. [Source](https://pytorch.org/tutorials/beginner/basics/intro.html)

Workflow typique PyTorch :
1. préparer `Dataset` et `DataLoader`,
2. définir la classe du modèle,
3. choisir loss et optimizer,
4. entraîner sur plusieurs epochs,
5. évaluer,
6. sauvegarder les poids. [Source](https://pytorch.org/tutorials/beginner/basics/intro.html)

### TensorFlow / Keras

Le tutoriel débutant de TensorFlow montre un pipeline minimal très clair :
1. charger un dataset,
2. construire un modèle de réseau de neurones,
3. compiler le modèle avec un optimiseur et une loss,
4. appeler `fit`,
5. puis `evaluate`. [Source](https://www.tensorflow.org/tutorials/quickstart/beginner)

Exemple typique :
- `model.compile(...)`
- `model.fit(...)`
- `model.evaluate(...)` [Source](https://www.tensorflow.org/tutorials/quickstart/beginner)

### Sauvegarde et chargement du modèle

PyTorch recommande comme bonne pratique de sauvegarder les poids via `state_dict`. Lors du chargement, il faut recréer l'architecture correspondante puis appeler `load_state_dict()`. La documentation rappelle aussi qu'il faut passer le modèle en mode évaluation avec `model.eval()` avant l'inférence, en particulier à cause des couches dropout et batch normalization. [Source](https://docs.pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html)

---

## Debugging et bonnes pratiques expertes

CS231n donne une série de conseils extrêmement précieux pour entraîner un réseau correctement.

### 1. Gradient checking

Quand on implémente une couche ou une loss personnalisée, il faut comparer le gradient analytique à un gradient numérique, de préférence avec une formule centrée et une erreur relative. Il faut désactiver dropout et effets stochastiques pendant cette vérification. [Source](https://cs231n.github.io/neural-networks-3/)

### 2. Sanity checks

Avant de lancer un long entraînement, il faut :
- vérifier que la loss initiale est cohérente avec le hasard,
- vérifier qu'une régularisation plus forte augmente la loss,
- vérifier que le réseau peut surapprendre un tout petit sous-ensemble. [Source](https://cs231n.github.io/neural-networks-3/)

### 3. Babysitting

Pendant l'entraînement, un expert surveille :
- la loss,
- l'accuracy train et validation,
- les distributions d'activations,
- les distributions de gradients,
- le ratio entre mises à jour et poids. [Source](https://cs231n.github.io/neural-networks-3/)

### 4. Interprétation des courbes

Si la loss ne descend pas du tout, le problème peut venir du learning rate, d'une implémentation incorrecte, d'une mauvaise initialisation ou d'un prétraitement incohérent. Si la validation décroche alors que le train explose en performance, la régularisation est probablement insuffisante. [Source](https://cs231n.github.io/neural-networks-3/)

---

## Évaluation, généralisation et mise en production

Un bon modèle profond n'est pas juste un modèle avec une bonne accuracy finale. Il faut mesurer sa capacité de **généralisation**, donc son comportement sur des données jamais vues. [Source](https://cs231n.github.io/neural-networks-3/)

En production, il faut aussi :
- sauvegarder les poids proprement,
- versionner le modèle,
- reproduire le preprocessing,
- passer en mode inférence correctement,
- surveiller les dérives de données,
- réentraîner si nécessaire. [Source](https://docs.pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html)

Un niveau expert implique de penser au-delà de l'entraînement offline : latence, mémoire GPU, stabilité de l'inférence, robustesse et coût de déploiement deviennent des critères aussi importants que la performance brute.

---

## Feuille de route pour passer de débutant à expert

### Niveau 1 — Débutant

À maîtriser :
- neurone artificiel,
- couches,
- activations,
- loss,
- gradient descent,
- premier réseau sur MNIST/FashionMNIST. [Source](https://www.tensorflow.org/tutorials/quickstart/beginner) [Source](https://pytorch.org/tutorials/beginner/basics/intro.html)

### Niveau 2 — Intermédiaire

À maîtriser :
- backpropagation,
- normalisation,
- initialisation,
- dropout,
- batch normalization,
- tuning du learning rate,
- lecture des courbes train/validation. [Source](https://cs231n.github.io/neural-networks-2/) [Source](https://cs231n.github.io/neural-networks-3/)

### Niveau 3 — Avancé

À maîtriser :
- CNN,
- RNN et leurs limites,
- attention,
- Transformers,
- workflows PyTorch propres,
- sauvegarde/chargement,
- debugging rigoureux. [Source](https://cs231n.github.io/convolutional-networks/) [Source](http://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html) [Source](https://docs.pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html)

### Niveau 4 — Expert

À maîtriser :
- choix d'architecture selon les données,
- optimisation des performances et du coût,
- scaling d'entraînement,
- préentraînement et fine-tuning,
- robustesse en production,
- lecture critique des nouvelles architectures. [Source](http://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html)

---

## Mini-projets recommandés

### Projet 1 — MNIST / FashionMNIST
Objectif : construire un premier classifieur d'images simple avec PyTorch ou TensorFlow. [Source](https://pytorch.org/tutorials/beginner/basics/intro.html) [Source](https://www.tensorflow.org/tutorials/quickstart/beginner)

### Projet 2 — MLP sur données tabulaires
Objectif : comparer un petit réseau dense à des méthodes ML classiques.

### Projet 3 — CNN sur images
Objectif : classifier des images plus riches et comprendre convolutions, pooling, data augmentation. [Source](https://cs231n.github.io/convolutional-networks/)

### Projet 4 — Séquence et attention
Objectif : implémenter une petite tâche séquentielle puis comparer RNN simple et Transformer. [Source](https://developers.google.com/machine-learning/crash-course/llm) [Source](http://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html)

### Projet 5 — Fine-tuning d'un modèle préentraîné
Objectif : charger un backbone préentraîné, l'adapter à une nouvelle tâche et sauvegarder proprement les poids. [Source](https://docs.pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html)

---

## Conclusion

Le Deep Learning est bien plus qu'un simple usage de bibliothèques comme PyTorch ou TensorFlow. C'est une discipline qui combine représentation mathématique, optimisation, architecture, qualité des données, régularisation, diagnostic expérimental et ingénierie de déploiement. Les ressources de Google, Stanford, PyTorch, TensorFlow et D2L convergent toutes vers une même idée : pour devenir bon, il faut comprendre les bases en profondeur avant de courir vers les architectures les plus récentes. [Source](https://developers.google.com/machine-learning/crash-course/neural-networks) [Source](https://cs231n.github.io/neural-networks-3/) [Source](https://pytorch.org/tutorials/beginner/basics/intro.html)

Si tu maîtrises vraiment les notions de propagation avant, backpropagation, learning rate, régularisation, choix d'architecture, monitoring train/validation et gestion du cycle complet d'entraînement, alors tu ne seras plus seulement utilisateur de modèles : tu commenceras à penser comme un ingénieur Deep Learning. [Source](https://cs231n.stanford.edu/slides/2025/lecture_4.pdf) [Source](https://cs231n.github.io/neural-networks-2/)

---

## Sources

- Google Machine Learning Crash Course — Neural Networks : https://developers.google.com/machine-learning/crash-course/neural-networks
- Google Machine Learning Crash Course — LLM : https://developers.google.com/machine-learning/crash-course/llm
- PyTorch Learn the Basics : https://pytorch.org/tutorials/beginner/basics/intro.html
- PyTorch Save & Load Model : https://docs.pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html
- TensorFlow Quickstart for Beginners : https://www.tensorflow.org/tutorials/quickstart/beginner
- Stanford CS231n — Neural Networks Part 1 : https://cs231n.github.io/neural-networks-1/
- Stanford CS231n — Neural Networks Part 2 : https://cs231n.github.io/neural-networks-2/
- Stanford CS231n — Neural Networks Part 3 : https://cs231n.github.io/neural-networks-3/
- Stanford CS231n — Convolutional Networks : https://cs231n.github.io/convolutional-networks/
- Stanford CS231n Slides — Backpropagation : https://cs231n.stanford.edu/slides/2025/lecture_4.pdf
- Dive into Deep Learning — Attention and Transformers : http://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html
