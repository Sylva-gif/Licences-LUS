# IA POUR LA CYBERSÉCURITÉ

---

## SOMMAIRE

I. Introduction générale (cybersécurité + IA & Deep Learning)
II. ML pour la cybersécurité
III. DL pour la cybersécurité
IV. IA offensive, défensive et résilience des systèmes intelligents
V. IA, cybersécurité & protection de la vie privée
VI. Projet de fin de module
Annexe A. Certifications professionnelles reconnues
Annexe B. Panorama des nouveaux outils (2026)
Annexe C. Glossaire général

## Objectifs du cours
1. Comprendre les bases du Deep Learning.
2. Comprendre les enjeux de la cybersécurité.
3. Appliquer les modèles de ML à des cas concrets en cybersécurité.
4. Mettre en œuvre des techniques de DL dans des problématiques de cybersécurité.
5. Concevoir et réaliser un mini-projet IA en cybersécurité.
6. Mener une démarche d'analyse de sécurité basée sur les données et l'IA.

## Prérequis
- Python (bases, pandas, scikit-learn)
- Machine Learning supervisé/non-supervisé
- Notions de classification / clustering
- Deep Learning (MLP, CNN, etc.)
- Bases de cybersécurité

---

# I. INTRODUCTION GÉNÉRALE

## I.1 Introduction à la cybersécurité

### a. Définition & enjeux

> **Définition — Cybersécurité**
> La cybersécurité est l'ensemble des méthodes, processus, outils et comportements visant à protéger les systèmes informatiques, les réseaux et les données contre les cyberattaques et les accès non autorisés.

Même si elle repose en grande partie sur la technologie, l'efficacité de la cybersécurité dépend également fortement des individus.

**Les enjeux** :
- **Complexité croissante** — Plus il y a d'outils et de technologies, plus la sécurité devient difficile à gérer.
- **Menaces en évolution** — Les attaques sont de plus en plus sophistiquées et difficiles à détecter.
- **Stratégies obsolètes** — Les anciennes méthodes de sécurité ne suffisent plus face aux menaces modernes.

### b. Concepts clés

**1 — CIA Triad (Confidentiality – Integrity – Availability)**
- Confidentialité : protection contre l'accès non autorisé.
- Intégrité : assurance que les données n'ont pas été altérées.
- Disponibilité : accès garanti aux ressources pour les utilisateurs autorisés.

**2 — Authentification, Autorisation, et Audit (AAA)**
- Authentification : vérifier qui est l'utilisateur (ex : login + mot de passe).
- Autorisation : ce que l'utilisateur a le droit de faire.
- Audit : journalisation des actions pour contrôle et traçabilité.

**3 — Menaces, vulnérabilités, et risques**
- Menace (Threat) : un danger potentiel (ex. : hacker, malware).
- Vulnérabilité : une faille exploitable (ex. : port ouvert, mot de passe faible).
- Risque : impact potentiel (menace × vulnérabilité).

> ⚠️ **Formule simple** : Risque = Menace × Vulnérabilité × Impact

**4 — Mesures de sécurité (Controls)**
- Préventives : éviter l'incident (firewall, antivirus, formation).
- Détectives : identifier l'incident (SIEM, IDS).
- Correctives : corriger après incident (restauration, patchs).

**5 — Principes de sécurité**
- Least privilege (moindre privilège)
- Defense in depth (défense en profondeur)
- Fail secure (mieux vaut bloquer qu'ouvrir en cas de problème)
- Security by design (penser sécurité dès la conception)

**6 — Types de sécurité**
- Sécurité physique : accès aux serveurs, caméras, badges.
- Sécurité logique : mots de passe, pare-feux, antivirus.
- Sécurité organisationnelle : politiques internes, procédures.

**Ce qu'un framework de cybersécurité doit couvrir** : Identify → Protect → Detect → Respond → Recover (cycle NIST CSF), appuyé sur des briques techniques : Network Access Control (NAC), Attack Surface Management, Firewall, Antivirus & Sandboxing, Web/DNS Filtering, Intrusion Prevention Systems (IPS), Remote Access VPNs.

### c. Types d'attaques

#### Par ingénierie sociale

**Attaques de phishing**
Le phishing (hameçonnage) est une attaque où un pirate envoie des e-mails frauduleux imitant une source de confiance afin de voler des informations sensibles (mots de passe, données bancaires…). L'attaquant utilise un lien piégé pour diriger la victime vers un site malveillant. Souvent, la victime ne se rend pas compte de l'attaque, ce qui permet à l'attaquant de se propager dans l'organisation.

*Pour se protéger* : être vigilant avant de cliquer sur un lien ou ouvrir une pièce jointe ; vérifier les en-têtes d'e-mails, les champs « Reply-to » et « Return-path ».

| Variante | Cible | Objectif | Tactique | Prévention |
|---|---|---|---|---|
| **Whale Phishing** | Dirigeants, cadres supérieurs (CEO, CFO) | Infos sensibles ou pression via ransomware | E-mails très convaincants | Vérification des expéditeurs, vigilance accrue |
| **Spear Phishing** | Une personne spécifique, ciblée après recherche | Vol de données perso/pro | E-mails personnalisés, spoofing, clonage de sites | Vérifier adresses e-mail, URLs, liens vérifiés |
| **Smishing** *(complément)* | Utilisateur mobile | Vol d'identifiants via SMS frauduleux | SMS imitant banque/livraison | Ne jamais cliquer un lien SMS non vérifié |
| **Vishing** *(complément)* | Utilisateur par téléphone | Extorsion vocale, souvent via deepfake voix (cf. IV) | Appel usurpant une voix connue | Procédure de vérification hors-bande |

> L'humain est le maillon faible.

#### Sur la confidentialité

**Vol de données / Data Breach** — Accès non autorisé à une base de données ou des fichiers sensibles. Souvent dû à un mot de passe faible, une mauvaise configuration serveur, une vulnérabilité logicielle.
*Protection* : MFA, chiffrement au repos/en transit, moindre privilège, mises à jour, SIEM.

**Sniffing / Eavesdropping** — Écoute passive des communications réseau. Sur un Wi-Fi non sécurisé, un pirate peut capturer les mots de passe échangés en clair.
*Protection* : HTTPS/TLS systématique, éviter le Wi-Fi public non sécurisé ou utiliser un VPN, segmentation réseau, IDS/IPS.

**Keylogging** — Logiciel ou matériel enregistrant les frappes clavier. Installé via malware, phishing ou clé USB malveillante.
*Protection* : antivirus/EDR à jour, ne pas télécharger de logiciels douteux, limiter les privilèges, claviers virtuels/2FA.

#### Sur la disponibilité

**Attaques DoS et DDoS** — Le déni de service vise à saturer les ressources d'un système. Le DDoS est lancé depuis un grand nombre de machines infectées (botnet) contrôlées par l'attaquant. L'objectif : rendre un service indisponible, pas d'y accéder.
*Protection* : pare-feu filtrant le trafic légitime du malveillant. Exemple notable : l'attaque contre AWS en février 2020.

**Botnets** — Réseau d'ordinateurs infectés (« zombies ») contrôlés à distance. Usages : DDoS, spam massif, vol d'identifiants, minage de crypto-monnaie.

#### Sur l'intégrité

**SQL Injection** — Injection de code SQL malveillant dans des champs de saisie pour manipuler une base de données. Peut mener à fuite, modification, suppression de données, voire exécution de commandes système.
*Protection* : moindre privilège, validation/sécurisation de toutes les entrées utilisateur (requêtes préparées, ORM).

**Attaques MITM (Man-in-the-Middle)** — Interception des communications entre deux parties à leur insu. Le détournement de session (session hijacking) est une variante de MITM où l'attaquant prend le contrôle d'une session client-serveur.
*Protection* : chiffrement fort sur les points d'accès, VPN.

#### Logiciels malveillants (Malwares)

| Type | Mécanisme | Exemple |
|---|---|---|
| **Virus** | S'attache à un fichier légitime ; se propage à l'ouverture | Clé USB infectée corrompant des fichiers |
| **Ver (worm)** | Se propage automatiquement via le réseau, sans action utilisateur | WannaCry (2017), exploitant une faille Windows |
| **Cheval de Troie (Trojan)** | Se fait passer pour un logiciel utile, installe un accès malveillant en secret | Faux logiciel de facturation ouvrant une porte dérobée |
| **Ransomware** | Bloque l'accès au système/fichiers jusqu'au paiement d'une rançon | Propagation via pièces jointes, réseau interne, clés USB ; peut contourner les antivirus classiques |
| **Spyware** *(complément)* | Collecte discrètement des informations sur l'utilisateur | Suivi de navigation, capture d'écran |
| **Rootkit** *(complément)* | Dissimule la présence d'un malware en modifiant le système d'exploitation | Persistance profonde, difficile à détecter |

*Protection générale* : antivirus/EDR à jour, ne pas ouvrir de pièces jointes suspectes, mises à jour système régulières, droits administrateurs limités.

#### Attaques avancées

**APT (Advanced Persistent Threats)** — Attaques longues, discrètes, souvent menées par des groupes organisés (cyber-espionnage). L'attaquant s'infiltre, reste caché, exfiltre des données sur des mois.
*Protection* : surveillance continue (logs, SIEM), segmentation réseau, threat intelligence, sécurité des accès privilégiés.

**Attaques Zero-Day** — Exploitent une faille encore inconnue du fabricant. Très dangereuses car aucun correctif n'existe encore.
*Protection* : patchs de sécurité rapides, détection comportementale (SIEM, EDR), réduction de la surface d'attaque.

#### Tableau récapitulatif — Attaques vs CIA Triad

| Attaques | Confidentialité | Intégrité | Disponibilité |
|---|---|---|---|
| Data breach | ✓ | ✗ | ✗ |
| Sniffing | ✓ | ✗ | ✗ |
| MITM | ✓ | ✓ | ✗ |
| Virus / Trojan | ✓ | ✓ | ✗ |
| Ransomware | ✓ | ✓ | ✓ |
| Spyware / Keylogger | ✓ | ✗ | ✗ |
| Phishing / Spear Phishing | ✓ | ✗ | ✗ |
| DoS / DDoS | ✗ | ✗ | ✓ |
| Injection SQL | ✗ | ✓ | ✗ |
| Zero-Day | ✓ | ✓ | ✓ |
| APT | ✓ | ✓ | ✓ |

## I.2 L'IA & Deep Learning

### a. Définitions

```
Intelligence artificielle
   └── Machine Learning
          └── Deep Learning
```

**Intelligence artificielle** — Domaine général visant à créer des systèmes qui imitent des comportements humains intelligents. Inclut les systèmes à règles (logique, arbres de décision faits main), les agents intelligents (chatbots, systèmes experts), le ML et le DL. Pas forcément « apprenant » : un algorithme à base de règles peut être considéré comme une IA.

**Machine Learning** — Sous-domaine de l'IA : les machines apprennent automatiquement à partir de données sans être explicitement programmées. L'algorithme trouve des motifs dans les données, puis génère un modèle capable de faire des prédictions.
Algorithmes classiques : K-Nearest Neighbors (KNN), Decision Trees, Random Forest, Support Vector Machines (SVM), Naive Bayes, Régressions (linéaire, logistique).
*Avantages* : peu de données suffisent souvent, interprétables (selon l'algo). *Désavantages* : moins performants sur des tâches complexes (vision, NLP).

**Deep Learning** — Sous-domaine du ML : modèles basés sur des réseaux de neurones profonds, capables de traiter des données complexes (images, texte, etc.). Utilise des réseaux de neurones artificiels (ANN) ; les réseaux profonds (> 2 couches) apprennent des fonctions très complexes.
Exemples : CNN (images), RNN/LSTM/Transformers (séquences, texte), Autoencoders, GANs.
*Avantages* : très performant sur les grandes bases de données (vision, texte, voix). *Désavantages* : demande beaucoup de calcul et de données, moins interprétable.

### b. Machine Learning vs Deep Learning

| Critère | Machine Learning | Deep Learning |
|---|---|---|
| Type de données | Tableaux (features tabulaires) | Images, audio, texte, séquences |
| Quantité de données | Moins | Beaucoup (1000s à millions d'exemples) |
| Prétraitement | Nécessaire (feature engineering) | Moins nécessaire (le réseau apprend seul) |
| Temps d'entraînement | Rapide | Long (surtout sans GPU) |
| Interprétabilité | Plus facile | Moins interprétable (« boîte noire ») |

**Utiliser ML si** : données structurées/tabulaires, dataset pas très grand (1k-100k lignes), besoin d'interprétabilité, entraînement rapide requis.
*Exemples* : prédire un prix immobilier, détection de fraude bancaire, analyse de churn, prédiction de panne via capteurs.

**Utiliser DL si** : données non structurées (images, sons, textes, séries longues), beaucoup de données (> 100k exemples), haute performance recherchée quitte à perdre en interprétabilité.
*Exemples* : reconnaissance vocale, détection d'objets, traduction automatique, **analyse de logs/alertes pour détection d'attaques (IDS) en cybersécurité**.

> **Quand l'interprétabilité est cruciale** : en médecine (justifier un classement à risque), en banque (justifier un refus de prêt), et **en cybersécurité (justifier une alerte comme étant une attaque vs un faux positif)**. Dans ces domaines, on privilégie parfois des modèles moins performants mais interprétables (arbres de décision).

### c. Structure d'un modèle de Deep Learning

```
Input layer → Hidden layers → Output layer
```

**Couche d'entrée (input layer)** — Ne fait pas de calcul « intelligent » ; reçoit les données brutes et les encode numériquement. Ex. : image 28×28 → vecteur de 784 valeurs ; texte → embeddings ; audio → spectrogramme.

**Couches cachées (hidden layers)** — Là où se fait l'apprentissage. Chaque neurone calcule `z = Σ(wᵢ·xᵢ) + b` puis applique une fonction d'activation `a = f(z)`. La **profondeur** = nombre de couches cachées.

Types de couches cachées :
- **Dense (fully connected)** — chaque neurone connecté à tous ceux de la couche précédente ; généraliste (MLP, classification).
- **Convolutionnelle (CNN)** — applique des filtres (kernels 3×3, 5×5…) qui balayent l'entrée pour détecter des motifs (contours, textures) ; poids partagés → moins de paramètres. Utilisée pour vision, audio, NLP (Conv1D).
- **Récurrente (RNN, LSTM, GRU)** — traite des séquences : `hₜ = f(Wxₜ + Uhₜ₋₁ + b)`. LSTM/GRU ajoutent des portes (gates) pour contrôler ce qu'on garde ou oublie. Utilisée pour texte, audio, séries temporelles.
- **Dropout** — éteint aléatoirement un pourcentage de neurones (p=0.2 à 0.5) pendant l'entraînement pour éviter le surapprentissage (régularisation).
- **Batch Normalization** — normalise les activations d'une couche (moyenne ≈ 0, variance ≈ 1) pour stabiliser et accélérer l'entraînement.

**Fonctions d'activation pour les couches cachées** :

| Fonction | Formule | Plage | Utilisation |
|---|---|---|---|
| ReLU | f(x) = max(x, 0) | [0, +∞[ | Standard (CNN, MLP, Transformers) ; risque de « neurones morts » |
| Leaky ReLU / PReLU | x si x≥0, αx sinon | ℝ | Évite les neurones morts |
| ELU | x si x≥0, α(eˣ-1) sinon | ℝ | Version lisse de ReLU |
| Tanh | (eˣ-e⁻ˣ)/(eˣ+e⁻ˣ) | [-1, 1] | RNN classiques |
| Sigmoid | 1/(1+e⁻ˣ) | [0, 1] | Historique, saturante |
| Swish / Mish | x·sigmoid(x) / variante lissée | ℝ | Architectures modernes (EfficientNet, Transformers) |

**Couche de sortie (output layer)** — Transforme les représentations apprises en résultat final adapté à la tâche.

| Tâche | Activation | Fonction de coût | Exemple |
|---|---|---|---|
| Régression | Identity (linéaire) | MSE / MAE | Prédire un prix, une température |
| Classification binaire | Sigmoid | Binary Cross-Entropy | Malade/pas malade, spam/pas spam |
| Classification multi-classes | Softmax | Cross-Entropy | Chat/chien/oiseau |
| Multi-label | Sigmoid par neurone | Binary Cross-Entropy par label | Image contenant chien + chat |
| Segmentation d'images | Softmax ou Sigmoid par pixel | Cross-Entropy | Imagerie médicale, segmentation routière |

### d. Cycle d'apprentissage d'un réseau de neurones

1. **Forward propagation** — chaque couche calcule `z⁽ˡ⁾ = W⁽ˡ⁾a⁽ˡ⁻¹⁾ + b⁽ˡ⁾`, puis `a⁽ˡ⁾ = f⁽ˡ⁾(z⁽ˡ⁾)`, jusqu'à obtenir la prédiction `ŷ = a⁽ᴸ⁾`.
2. **Calcul de la perte (loss)** — compare `ŷ` à `y` : MSE en régression, Binary Cross-Entropy en classification binaire, Cross-Entropy + Softmax en multi-classes.
3. **Backpropagation** — propage l'erreur de la sortie vers les couches cachées via la règle de dérivation en chaîne, pour calculer le gradient de la perte par rapport à chaque poids et biais.
4. **Descente de gradient** — met à jour les paramètres : `W⁽ˡ⁾ ← W⁽ˡ⁾ - η·∂ℒ/∂W⁽ˡ⁾`, où η est le taux d'apprentissage (learning rate).

**Boucle d'entraînement** : répéter 1→4 pour chaque mini-batch ; un passage complet sur le dataset = 1 époque ; répéter plusieurs époques jusqu'à convergence.

### e. Lien entre IA et cybersécurité

**Lien positif** — l'IA sert la défense : analyse d'anomalies, détection de menaces, réponse automatique.
**Lien négatif** — la cybersécurité doit protéger l'IA elle-même : ses données d'apprentissage, ses modèles, ses décisions.

| Catégorie | Exemples |
|---|---|
| Attaques **détectées** par l'IA | Phishing, ransomwares, DDoS |
| Attaques **générées** par l'IA | E-mails malveillants créés par IA, deepfakes |
| Attaques **contre** l'IA | Data poisoning, attaques adversariales |

*(Ces trois axes sont développés en détail aux chapitres III et IV.)*

---

# II. ML POUR LA CYBERSÉCURITÉ

## Objectif
Utiliser des modèles classiques (SVM, Random Forest, k-NN) pour détecter des menaces, et mettre en œuvre des pipelines de traitement complets (préparation des données, vectorisation, normalisation, évaluation des performances).

## II.1 Attaques & données

Pour entraîner un modèle ML de cybersécurité, il faut d'abord identifier la **source de données** correspondant au type de menace visé.

| Type de détection | Source de données | Exemples de jeux publics |
|---|---|---|
| Détection d'intrusion réseau (IDS) | Flux réseau, paquets, NetFlow | NSL-KDD, CICIDS2017/2018, UNSW-NB15 |
| Détection de malware | Binaires exécutables, hashs, comportements sandbox | EMBER, VirusShare (metadata), Malware Bazaar |
| Détection de phishing | URLs, contenu HTML/e-mail, métadonnées DNS | PhishTank, UCI Phishing Websites |
| Détection de fraude | Transactions, logs applicatifs | Kaggle Credit Card Fraud |
| Analyse de logs / SIEM | Logs système, logs applicatifs, logs d'authentification | LANL Auth dataset, HDFS logs |

> **Point de vigilance** : les jeux de données de cybersécurité vieillissent vite (les attaques évoluent). Un modèle entraîné sur NSL-KDD (2009, dérivé de KDD Cup 1999) peut ne pas généraliser aux menaces actuelles — c'est le problème du **concept drift**, central en cybersécurité.

### Caractéristiques (features) typiques
- **Réseau** : durée de connexion, protocole, nombre de paquets, octets envoyés/reçus, flags TCP, ports source/destination.
- **Hôte/malware** : entropie du fichier, appels système (syscalls), imports de DLL, taille du fichier, présence de packers.
- **Phishing/URL** : longueur de l'URL, présence d'IP au lieu d'un nom de domaine, nombre de sous-domaines, âge du domaine (WHOIS), présence de caractères suspects.
- **Comportemental (utilisateur)** : heure de connexion, localisation, fréquence des échecs d'authentification, volume de données téléchargées.

## II.2 Préparation des données

Le pipeline de préparation est le prolongement direct des principes ETL déjà connus (extraction, nettoyage), appliqué spécifiquement aux données de sécurité.

### a. Nettoyage
- Traiter les valeurs manquantes (imputation ou suppression selon le taux de complétude).
- Détecter et traiter les outliers (ex. durée de connexion négative = erreur de capture).
- Dédupliquer les événements (un même paquet capturé deux fois par des sondes différentes).

### b. Vectorisation / Encodage
- **Variables catégorielles** (protocole, type de service) → One-Hot Encoding ou Label Encoding.
- **Texte** (contenu d'e-mail, User-Agent, commandes) → TF-IDF, Bag-of-Words, ou embeddings (pour les approches DL, voir chapitre III).
- **IP/ports** → parfois transformés en catégories (port bien connu vs port éphémère) plutôt que gardés en valeur brute.

### c. Normalisation
- **Min-Max scaling** : ramène les valeurs entre 0 et 1 — utile pour les algorithmes sensibles à l'échelle (SVM, k-NN, réseaux de neurones).
- **Standardisation (Z-score)** : centre-réduit les données (moyenne 0, écart-type 1) — utile pour la régression logistique, PCA.
- **Log-transform** : utile pour des variables très asymétriques comme le volume d'octets échangés.

### d. Gestion du déséquilibre des classes (class imbalance)
C'est **le défi central du ML en cybersécurité** : les attaques représentent généralement une infime fraction du trafic total (souvent < 1%).

| Technique | Principe |
|---|---|
| Sous-échantillonnage (undersampling) | Réduire la classe majoritaire (trafic normal) |
| Sur-échantillonnage (oversampling) | Dupliquer ou générer des exemples de la classe minoritaire |
| **SMOTE** (Synthetic Minority Oversampling) | Génère des exemples synthétiques d'attaques par interpolation entre voisins |
| Pondération des classes (class weights) | Pénaliser davantage les erreurs sur la classe minoritaire dans la fonction de coût |
| Détection d'anomalies (approche non supervisée) | Modéliser uniquement le comportement « normal », traiter tout écart comme suspect (utile quand les attaques sont trop rares pour être apprises directement) |

### e. Split train/validation/test
Attention à la **fuite temporelle (temporal leakage)** : en cybersécurité, il faut respecter l'ordre chronologique des événements (entraîner sur le passé, tester sur le futur) plutôt qu'un split aléatoire classique, sous peine de surestimer la performance réelle du modèle en production.

## II.3 Application des modèles ML

### a. k-Nearest Neighbors (k-NN)
Classe un événement selon la classe majoritaire de ses k voisins les plus proches dans l'espace des features.
- **Usage** : détection d'intrusion simple, détection d'outliers.
- **Avantages** : simple, pas d'entraînement explicite (« lazy learning »).
- **Limites** : coûteux en calcul sur de gros volumes (calcule les distances à chaque prédiction), sensible à la dimensionnalité (curse of dimensionality) et au bruit.

### b. Support Vector Machines (SVM)
Cherche l'hyperplan séparant au mieux deux classes (ex. trafic normal vs malveillant), en maximisant la marge entre les classes. Le **kernel trick** (RBF, polynomial) permet de séparer des classes non linéairement séparables.
- **Usage** : classification de trafic réseau, détection de spam.
- **Avantages** : performant sur des données de dimension élevée et en volume modéré.
- **Limites** : moins adapté aux très grands volumes ; peu interprétable avec un kernel non linéaire.

### c. Arbres de décision & Random Forest
Un arbre de décision découpe l'espace des features par une succession de règles (« si durée > X et protocole = TCP alors… »). Random Forest agrège de nombreux arbres entraînés sur des sous-échantillons aléatoires (bagging), améliorant la robustesse et réduisant le surapprentissage.
- **Usage** : très répandu en détection d'intrusion (NSL-KDD, CICIDS) et en détection de malware (à partir de features statiques).
- **Avantages** : bonne performance out-of-the-box, gère bien les features mixtes, donne une mesure d'**importance des features** (utile pour l'explicabilité, cruciale en SOC — cf. I.2.b).
- **Limites** : modèle plus lourd qu'un arbre unique, moins interprétable qu'un arbre isolé.

### d. Gradient Boosting (XGBoost, LightGBM) *(complément)*
Construit les arbres de façon séquentielle, chaque nouvel arbre corrigeant les erreurs des précédents. Aujourd'hui l'un des algorithmes ML les plus utilisés en production pour la détection de fraude et d'intrusion, pour son excellent compromis performance/vitesse sur données tabulaires.

### e. Naive Bayes
Classifieur probabiliste basé sur le théorème de Bayes, avec une hypothèse (naïve) d'indépendance entre les features.
- **Usage** : filtrage de spam/phishing (historiquement l'un des tout premiers succès du ML en sécurité), classification de texte.
- **Avantages** : très rapide, fonctionne bien avec peu de données.

### f. Clustering non supervisé (k-means, DBSCAN)
Utilisé quand on ne dispose pas d'étiquettes (« normal » / « attaque ») fiables : regroupe les événements similaires et isole les points atypiques comme suspects.
- **Usage** : détection d'anomalies comportementales (UEBA — User and Entity Behavior Analytics), découverte de nouvelles familles de malware par similarité.
- **DBSCAN** est particulièrement adapté car il ne nécessite pas de fixer à l'avance le nombre de clusters, et identifie naturellement les points de bruit (potentielles anomalies).

### g. Isolation Forest *(complément)*
Algorithme dédié à la détection d'anomalies : isole les observations en partitionnant aléatoirement l'espace des features ; les anomalies nécessitent en moyenne moins de partitions pour être isolées (elles sont « faciles à séparer » du reste).
- **Usage** : détection de fraude, détection d'intrusion en mode non supervisé, quand les attaques sont trop rares ou nouvelles pour être apprises par classification supervisée.

## II.4 Évaluation des performances

En cybersécurité, la **précision globale (accuracy)** est trompeuse à cause du déséquilibre des classes (un modèle qui prédit toujours « normal » peut avoir 99% d'accuracy si les attaques sont à 1%, tout en étant inutile).

| Métrique | Formule | Sens en cybersécurité |
|---|---|---|
| Précision (Precision) | VP / (VP + FP) | Parmi les alertes levées, combien sont de vraies attaques ? (mesure le taux de faux positifs) |
| Rappel (Recall) | VP / (VP + FN) | Parmi les vraies attaques, combien ont été détectées ? (mesure le taux de faux négatifs) |
| F1-score | 2·(Precision×Recall)/(Precision+Recall) | Compromis précision/rappel |
| Matrice de confusion | — | Vue complète VP/FP/VN/FN |
| Courbe ROC / AUC | — | Performance du modèle à différents seuils de décision |
| Courbe Précision-Rappel | — | Préférée à la ROC quand les classes sont très déséquilibrées |

> **Arbitrage clé en SOC** : un **faux négatif** (attaque non détectée) est souvent bien plus coûteux qu'un **faux positif** (fausse alerte) — mais trop de faux positifs entraîne l'« alert fatigue » qui pousse les analystes à ignorer les alertes légitimes. Le choix du seuil de décision doit refléter ce compromis métier, pas seulement l'optimum mathématique.

## II.5 Cas pratique guidé — Détection d'intrusion réseau

1. **Données** : jeu NSL-KDD ou CICIDS2017 (flux réseau labellisés normal/attaque).
2. **Préparation** : encodage des variables catégorielles (protocole, service, flag), normalisation Min-Max des features numériques, gestion du déséquilibre (SMOTE ou pondération de classes).
3. **Modélisation** : entraîner un Random Forest et un SVM, comparer.
4. **Évaluation** : matrice de confusion, F1-score, courbe ROC — en particulier sur les classes d'attaques minoritaires (ex. U2R, R2L dans NSL-KDD, historiquement les plus difficiles à détecter).
5. **Explicabilité** : extraire l'importance des features du Random Forest pour identifier quelles variables réseau sont les plus discriminantes (utile pour justifier une alerte auprès d'un analyste SOC).

---

# III. DL POUR LA CYBERSÉCURITÉ

## III.1 Pourquoi le DL pour la cybersécurité ?

Le ML classique (chapitre II) atteint ses limites quand :
- les données sont **non structurées** ou très volumineuses (logs bruts, paquets réseau complets, code binaire, images de trafic) ;
- les **motifs d'attaque évoluent** et nécessitent une représentation apprise automatiquement plutôt que des features conçues manuellement (feature engineering) ;
- il faut modéliser des **dépendances séquentielles/temporelles** longues (une APT se déroule sur plusieurs mois — cf. I.1.c).

Le DL permet un **apprentissage de représentation (representation learning)** : au lieu de définir manuellement les features (comme en ML classique), le réseau apprend lui-même les représentations pertinentes à partir des données brutes.

## III.2 Architectures utiles en cybersécurité

### a. CNN (Convolutional Neural Networks)
Initialement conçus pour la vision, les CNN sont détournés en cybersécurité par une astuce : **transformer les données en « images »**.
- **Détection de malware par visualisation binaire** : le code exécutable est converti en image en niveaux de gris (chaque octet = un pixel), puis un CNN classifie l'image comme bénigne ou appartenant à une famille de malware. Les malwares d'une même famille produisent des motifs visuels similaires.
- **Classification de trafic réseau** : les paquets ou flux peuvent être représentés sous forme de matrices (image) pour être classifiés par CNN.
- **NLP côté sécurité** : Conv1D appliqué à des séquences de caractères ou de tokens (URLs, logs) pour détecter des motifs locaux suspects (ex. patterns d'injection SQL).

### b. RNN, LSTM, GRU
Adaptés aux données **séquentielles** : une session réseau, une séquence de commandes, un flux de logs dans le temps.
- **Détection d'intrusion basée sur les séquences** : modéliser une session utilisateur comme une séquence d'appels système ou de requêtes, et détecter les déviations par rapport aux séquences normales.
- **Analyse de logs** : les LSTM sont utilisés pour apprendre la structure normale des logs système (ex. DeepLog) et signaler les séquences anormales, sans besoin de règles écrites manuellement.
- **Détection de DGA (Domain Generation Algorithm)** : les LSTM classifient des noms de domaine caractère par caractère pour détecter les domaines générés algorithmiquement par des malwares (technique d'évasion des botnets).

### c. Autoencoders
Réseau entraîné à reconstruire son entrée en passant par une représentation compressée (goulot d'étranglement). Entraîné **uniquement sur du trafic normal**, il reconstruit mal tout ce qui s'écarte de la normale — l'erreur de reconstruction devient un score d'anomalie.
- **Usage** : détection d'anomalies non supervisée, particulièrement adaptée quand les attaques sont rares ou inconnues (zero-day, cf. I.1.c).
- **Variational Autoencoders (VAE)** *(complément)* : version probabiliste, utile pour modéliser l'incertitude et générer des échantillons synthétiques d'entraînement.

### d. Transformers *(complément important)*
Architecture devenue dominante depuis 2020, initialement pour le NLP (traduction, LLM), aujourd'hui appliquée à la cybersécurité :
- **Analyse de logs et de séquences longues** — le mécanisme d'attention capture des dépendances à longue portée mieux que les LSTM, utile pour repérer une APT qui se déroule sur des milliers d'événements.
- **Analyse de code / détection de vulnérabilités** — modèles de type CodeBERT analysant du code source pour repérer des patterns vulnérables.
- **Classification de contenu de phishing/e-mail** — modèles de langage (type BERT) analysant le contenu textuel d'un e-mail pour détecter des indices linguistiques de phishing plus fins que le simple filtrage par mots-clés.

### e. GANs (Generative Adversarial Networks) *(complément)*
Deux réseaux (générateur / discriminateur) s'entraînent en compétition. En cybersécurité :
- **Usage défensif** : génération de données synthétiques d'attaques pour enrichir des jeux de données déséquilibrés (alternative à SMOTE pour les données complexes).
- **Usage offensif** *(voir chapitre IV)* : génération de malwares adverses capables de contourner un détecteur, ou de deepfakes pour l'ingénierie sociale.

## III.3 Études de cas

### Cas 1 — Détection d'intrusion (IDS) par Autoencoder
Un autoencoder est entraîné exclusivement sur des flux réseau normaux (ex. CICIDS2017, sous-ensemble bénin). En production, chaque nouveau flux est passé dans l'autoencoder ; si l'erreur de reconstruction dépasse un seuil, le flux est signalé comme anomalie potentielle. Avantage clé : détecte des attaques **jamais vues à l'entraînement** (contrairement à un classifieur supervisé).

### Cas 2 — Détection de malware par CNN sur image binaire
Les fichiers exécutables (`.exe`) sont convertis en images en niveaux de gris de taille fixe. Un CNN (architecture proche de LeNet/ResNet simplifié) est entraîné à classifier ces images par famille de malware. Résultats : performances proches ou supérieures aux approches à base de signatures pour détecter des variantes d'une même famille (polymorphisme).

### Cas 3 — Analyse de logs par LSTM (type DeepLog)
Les logs système sont transformés en séquences de « clés de log » (templates d'événements). Un LSTM apprend la séquence normale des événements système. Toute séquence qui s'écarte significativement du modèle appris (probabilité faible du prochain événement observé) déclenche une alerte — sans qu'aucune règle SIEM n'ait été écrite manuellement.

### Cas 4 — Classification de trafic chiffré
Avec la généralisation de TLS, l'inspection profonde de paquets (DPI) classique devient impossible sur le contenu chiffré. Des modèles DL (souvent CNN ou LSTM) classifient le trafic à partir de métadonnées observables même sous chiffrement : taille des paquets, timing entre paquets, séquence de tailles — une approche appelée **traffic fingerprinting**.

## À retenir — Chapitre III
- Le DL est pertinent quand les données sont non structurées, volumineuses, ou nécessitent une modélisation séquentielle/temporelle.
- CNN → données transformées en « image » (malware, trafic) ; RNN/LSTM → séquences (logs, sessions) ; Autoencoders → détection d'anomalies non supervisée ; Transformers → dépendances longues et NLP de sécurité.
- Le DL améliore la détection de menaces inconnues (zero-day) via l'apprentissage de représentation, au prix d'une interprétabilité réduite — d'où l'importance de l'explicabilité (XAI, voir IV et V).

---

# IV. IA OFFENSIVE, DÉFENSIVE ET RÉSILIENCE DES SYSTÈMES INTELLIGENTS

## IV.1 IA pour les cyberattaques (IA offensive)

L'IA n'est pas seulement un outil défensif : elle abaisse le coût et augmente l'échelle des cyberattaques.

| Usage offensif de l'IA | Description |
|---|---|
| **Phishing généré par IA** | Des LLM génèrent des e-mails de spear phishing personnalisés, grammaticalement parfaits, dans la langue et le style de l'organisation ciblée — à grande échelle et à faible coût. |
| **Deepfakes** | Vidéos/audios synthétiques imitant un dirigeant pour tromper un employé (variante IA du Whale Phishing, cf. I.1.c) — des fraudes au « faux CEO » par deepfake vocal ou vidéo ont déjà causé des pertes de plusieurs millions de dollars à des entreprises. |
| **Malware polymorphe généré par IA** | Génération automatique de variantes de code malveillant pour échapper aux signatures antivirus (mutation continue). |
| **Reconnaissance automatisée (OSINT augmenté)** | Des agents IA collectent et croisent automatiquement des informations publiques pour préparer une attaque ciblée (spear phishing, social engineering) plus rapidement qu'un humain. |
| **Cracking de mots de passe assisté par IA** | Des modèles de langage entraînés sur des fuites de mots de passe génèrent des candidats plus pertinents que les règles classiques (dictionnaires, règles de mutation). |
| **Attaques automatisées / agentic AI** | Agents IA autonomes capables d'enchaîner reconnaissance, exploitation et exfiltration avec une supervision humaine minimale — une tendance émergente activement surveillée par les frameworks comme MITRE ATLAS (voir IV.3). |

## IV.2 IA pour la défense

### a. Security Operations Center (SOC) augmenté par l'IA
- **Triage automatique des alertes** — un modèle ML/DL priorise les milliers d'alertes SIEM quotidiennes selon leur probabilité d'être une vraie menace, réduisant l'« alert fatigue » (cf. II.4).
- **SOAR (Security Orchestration, Automation and Response)** — automatise les réponses à des scénarios connus (isoler une machine, bloquer une IP) une fois une menace confirmée par l'IA.
- **UEBA (User and Entity Behavior Analytics)** — modélise le comportement normal de chaque utilisateur/machine (cf. clustering, II.3.f) pour détecter les déviations (compte compromis, menace interne).
- **Threat Hunting assisté** — des copilotes IA (souvent basés sur des LLM) aident les analystes à formuler des requêtes de recherche de menaces en langage naturel sur les données SIEM, et à résumer automatiquement les investigations.

### b. XDR (Extended Detection and Response)
Extension du concept d'EDR (Endpoint Detection and Response) : corrèle les signaux de plusieurs sources (endpoint, réseau, cloud, e-mail) via des modèles ML/DL pour détecter des attaques qui ne seraient pas visibles en observant une seule source isolément.

### c. Détection de deepfakes
Des modèles DL (souvent CNN sur images/vidéo, ou analyse spectrale sur l'audio) sont spécifiquement entraînés à repérer les artefacts de génération (incohérences de clignement des yeux, artefacts fréquentiels de synthèse vocale) pour contrer les usages offensifs listés en IV.1.

### d. Threat Intelligence augmentée par l'IA
Des modèles NLP analysent en continu les sources ouvertes (forums, dark web, CVE, réseaux sociaux) pour détecter automatiquement l'émergence de nouvelles menaces, avant même leur exploitation massive.

## IV.3 Attaques contre les IA (Adversarial Machine Learning)

C'est le pendant du « lien négatif » évoqué en I.2.e : les modèles d'IA de sécurité sont eux-mêmes des cibles. Le référentiel de référence pour cataloguer ces menaces est **MITRE ATLAS** (Adversarial Threat Landscape for Artificial-Intelligence Systems), équivalent de MITRE ATT&CK pour l'IA.

### a. Attaques adversariales (evasion attacks)
Perturbations imperceptibles ajoutées à une entrée pour tromper un modèle déjà entraîné, sans modifier le modèle lui-même.
- **Exemple classique** : ajouter un bruit calculé à une image pour qu'un CNN la classe incorrectement, alors que l'image paraît identique à l'œil humain.
- **En cybersécurité** : modifier légèrement un binaire malveillant (ajout d'octets inoffensifs, réorganisation de sections) pour qu'un détecteur de malware par CNN (cf. III.2.a) le classe comme bénin, tout en conservant le comportement malveillant.
- **Prompt injection** *(spécifique aux LLM)* : instructions cachées dans un contenu (document, page web, e-mail) visant à détourner le comportement d'un LLM/agent IA — un enjeu de sécurité central pour les copilotes SOC (IV.2.a).

### b. Data poisoning (empoisonnement des données)
Corruption des données d'entraînement pour dégrader ou biaiser un modèle avant même son déploiement.
- **Exemple** : injecter de faux exemples « bénins » ressemblant à des attaques réelles dans le jeu d'entraînement d'un IDS, pour créer un point aveugle exploitable ensuite.
- Particulièrement critique pour les modèles réentraînés en continu (online learning) sur des données de production non filtrées.

### c. Model extraction / model stealing
Un attaquant interroge massivement un modèle en production (via son API) pour reconstruire un modèle de substitution qui en imite le comportement — permettant ensuite de préparer des attaques adversariales hors ligne, ou de voler la propriété intellectuelle du modèle.

### d. Model inversion / membership inference
- **Model inversion** — reconstruire des données d'entraînement sensibles à partir des sorties du modèle (risque de confidentialité, cf. chapitre V).
- **Membership inference** — déterminer si un enregistrement spécifique faisait partie du jeu d'entraînement, ce qui peut révéler des informations personnelles (ex. si les données d'entraînement d'un modèle médical contenaient les données d'un individu précis).

### e. Attaques spécifiques aux LLM / IA générative
- **Jailbreaking** — contourner les garde-fous de sécurité/éthique d'un LLM via des formulations de prompt spécifiques.
- **Prompt injection indirecte** — instructions malveillantes cachées dans un contenu que le LLM va lire (document, résultat de recherche), plutôt que dans le prompt direct de l'utilisateur.
- **Empoisonnement de la chaîne d'approvisionnement IA (AI supply chain)** — modèles pré-entraînés téléchargés depuis des dépôts publics (Hugging Face, etc.) contenant du code malveillant ou des biais intentionnels.

### Panorama des contre-mesures

| Menace | Contre-mesure principale |
|---|---|
| Attaques adversariales (evasion) | Adversarial training (entraîner le modèle avec des exemples adversariaux), détection d'anomalies sur les entrées, ensembles de modèles |
| Data poisoning | Validation/traçabilité des données d'entraînement, détection d'outliers avant entraînement, apprentissage robuste |
| Model extraction | Limitation du taux de requêtes (rate limiting), watermarking de modèle, détection de patterns de requêtes suspects |
| Model inversion / membership inference | Differential privacy (voir chapitre V), réduction de la précision des sorties exposées |
| Prompt injection / jailbreaking | Filtrage des entrées/sorties, séparation stricte instructions/données, tests de red teaming réguliers (cf. OWASP LLM Top 10) |

## À retenir — Chapitre IV
- L'IA abaisse le coût des attaques (phishing personnalisé, deepfakes, malware polymorphe) tout en démultipliant les capacités défensives (SOC augmenté, XDR, threat hunting).
- Les modèles d'IA sont eux-mêmes des surfaces d'attaque : MITRE ATLAS structure ces menaces (evasion, poisoning, extraction, inversion, attaques LLM).
- La résilience d'un système IA de sécurité nécessite des contre-mesures spécifiques, distinctes de la sécurité applicative classique.

---

# V. IA, CYBERSÉCURITÉ & PROTECTION DE LA VIE PRIVÉE

## V.1 Confidentialité & RGPD

### a. Rappel des principes RGPD pertinents pour l'IA
Le Règlement Général sur la Protection des Données (RGPD, UE, 2018) encadre tout traitement de données personnelles, y compris par des systèmes d'IA/ML de cybersécurité (logs contenant des adresses IP, identifiants utilisateurs, comportements).

| Principe RGPD | Implication pour un système IA de sécurité |
|---|---|
| Minimisation des données | Ne collecter/conserver que les données réellement nécessaires à la détection de menaces |
| Limitation de la finalité | Les logs collectés pour la sécurité ne peuvent pas être réutilisés librement pour d'autres finalités (ex. évaluation RH) |
| Droit à l'explication *(lié à l'art. 22)* | Une décision automatisée à fort impact (ex. blocage automatique d'un compte) doit pouvoir être expliquée — lien direct avec l'explicabilité évoquée en I.2.b et II.4 |
| Privacy by design | La protection des données doit être pensée dès la conception du pipeline ML (cf. II.2), pas ajoutée après coup |
| Droit à l'effacement | Complexe pour les modèles ML : un modèle entraîné sur des données personnelles « mémorise » potentiellement ces données (cf. model inversion, IV.3.d) — d'où l'émergence du **machine unlearning** |

### b. Tension structurelle : sécurité vs vie privée
La cybersécurité nécessite souvent une **surveillance étendue** (logs détaillés, comportements utilisateurs, contenus d'e-mails) pour détecter les menaces — ce qui entre en tension directe avec les principes de minimisation des données du RGPD. Les architectures de sécurité modernes doivent arbitrer explicitement entre :
- **couverture de détection maximale** (plus de données = meilleure détection, cf. chapitres II-III) ;
- **respect de la vie privée** (minimisation, anonymisation, durée de conservation limitée).

## V.2 IA & Privacy-Enhancing Technologies (PET)

Ces technologies permettent de concilier performance des modèles IA et protection de la vie privée.

### a. Anonymisation et pseudonymisation
- **Anonymisation** — suppression irréversible du lien entre une donnée et une personne (ex. suppression complète des adresses IP dans les logs analysés).
- **Pseudonymisation** — remplacement des identifiants directs par des identifiants indirects réversibles sous conditions (utile pour investiguer un incident tout en limitant l'exposition au quotidien).
- **Limite en ML** : l'anonymisation naïve peut être contournée par ré-identification en croisant plusieurs sources de données (attaque de corrélation) — d'où le recours à des techniques plus robustes ci-dessous.

### b. Differential Privacy (confidentialité différentielle)
Ajoute un bruit statistique calibré aux données ou aux résultats d'un modèle, garantissant mathématiquement qu'aucune conclusion précise ne peut être tirée sur un individu spécifique, tout en préservant les tendances statistiques globales utiles à la détection de menaces.
- **Usage en cybersécurité** : publier des statistiques agrégées sur les incidents de sécurité sans exposer d'utilisateurs individuels ; entraîner des modèles ML avec garanties de confidentialité (DP-SGD — Differentially Private Stochastic Gradient Descent), en contre-mesure directe au **model inversion** (IV.3.d).

### c. Federated Learning (apprentissage fédéré)
Le modèle est entraîné localement sur chaque appareil/organisation (les données ne quittent jamais leur environnement d'origine) ; seuls les paramètres du modèle (gradients) sont partagés et agrégés centralement.
- **Usage en cybersécurité** : plusieurs organisations (ex. banques, opérateurs télécom) collaborent pour entraîner un détecteur de fraude/malware commun plus performant, sans jamais partager leurs données brutes sensibles entre elles — un enjeu particulièrement pertinent pour de la threat intelligence mutualisée.

### d. Chiffrement homomorphe (Homomorphic Encryption)
Permet d'effectuer des calculs directement sur des données chiffrées, sans jamais les déchiffrer — le résultat du calcul, une fois déchiffré, est identique à celui obtenu sur les données en clair.
- **Usage** : exécuter un modèle de détection de menace sur des données chiffrées hébergées par un tiers (cloud), sans jamais exposer les données en clair au fournisseur cloud. Coût de calcul encore élevé, en progression rapide.

### e. Secure Multi-Party Computation (SMPC) *(complément)*
Plusieurs parties calculent conjointement une fonction sur leurs données privées respectives sans qu'aucune partie ne révèle ses données aux autres — utile pour du partage de threat intelligence entre organisations concurrentes.

### Tableau de synthèse

| Technologie | Protège contre | Coût principal |
|---|---|---|
| Anonymisation/pseudonymisation | Exposition directe des identifiants | Risque de ré-identification par corrélation |
| Differential Privacy | Model inversion, membership inference | Perte de précision statistique (compromis privacy/utility) |
| Federated Learning | Centralisation de données sensibles | Complexité d'infrastructure, attaques possibles sur les gradients partagés |
| Chiffrement homomorphe | Exposition des données à un tiers de calcul | Coût de calcul très élevé |
| SMPC | Partage de données entre parties non-confiantes | Complexité protocolaire, latence |

## V.3 Cadres réglementaires complémentaires (2025-2026)

- **RGPD (UE)** — cadre de référence pour les données personnelles, applicable à tout traitement IA sur des données européennes.
- **EU AI Act** — règlement européen sur l'IA, avec des obligations renforcées pour les systèmes d'IA « à haut risque » (dont certains usages de sécurité) ; échéances de mise en conformité pour les systèmes à haut risque en 2026.
- **NIST AI Risk Management Framework (AI RMF)** — cadre américain de gestion des risques IA, incluant un profil spécifique pour l'IA générative (NIST AI 600-1).
- **ISO/IEC 42001** — norme internationale de système de management de l'IA, avec les premières certifications d'organisations apparaissant en 2025-2026.
- **OWASP Top 10 for LLM Applications** — référentiel des vulnérabilités spécifiques aux applications basées sur des LLM (prompt injection, data poisoning, etc.), complémentaire à MITRE ATLAS (cf. IV.3).

## À retenir — Chapitre V
- La cybersécurité par l'IA repose sur la collecte de données souvent sensibles, ce qui crée une tension structurelle avec le RGPD et les principes de minimisation.
- Les Privacy-Enhancing Technologies (differential privacy, federated learning, chiffrement homomorphe, SMPC) permettent de concilier performance de détection et protection de la vie privée.
- Le cadre réglementaire (RGPD, EU AI Act, NIST AI RMF, ISO/IEC 42001) structure de plus en plus les obligations de gouvernance IA en contexte de sécurité.

---

# VI. PROJET DE FIN DE MODULE

## Objectif
Concevoir, réaliser et présenter un mini-projet IA appliqué à la cybersécurité, mobilisant les compétences des chapitres I à V.

## Étapes attendues

1. **Choix du sujet et du jeu de données** — sélectionner un cas d'usage (détection d'intrusion, malware, phishing, anomalies de logs…) et un jeu de données réel (cf. II.1 pour des sources publiques).
2. **Choix de l'approche (ML ou DL)** — justifier le choix selon les critères du tableau III.2.b/II (volume de données, structure, besoin d'interprétabilité — cf. I.2.b).
3. **Pipeline de données** — extraction, nettoyage, vectorisation, normalisation, gestion du déséquilibre des classes (cf. II.2).
4. **Construction et entraînement du modèle** — choix de l'algorithme/architecture, hyperparamètres, validation croisée respectant la chronologie (cf. II.2.e).
5. **Évaluation** — matrice de confusion, precision/recall/F1, courbe ROC/PR, analyse spécifique des faux négatifs (cf. II.4).
6. **Explicabilité** — importance des features (modèles ML), ou techniques XAI pour le DL (SHAP, LIME, Grad-CAM selon l'architecture) — justifier les décisions du modèle dans un contexte métier/sécurité.
7. **Discussion éthique et robustesse** — le modèle est-il vulnérable à des attaques adversariales (cf. IV.3) ? Respecte-t-il les principes de minimisation des données (cf. V.1) ?
8. **Documentation et présentation** — rapport structuré (contexte, méthode, résultats, limites, perspectives) + soutenance orale.

## Grille d'évaluation indicative

| Critère | Points de vigilance |
|---|---|
| Pertinence du cas d'usage | Le problème est-il clairement défini et réaliste ? |
| Qualité du pipeline de données | Gestion du déséquilibre, absence de fuite temporelle (temporal leakage) |
| Justification technique | Le choix ML vs DL et de l'algorithme est-il argumenté, pas seulement appliqué ? |
| Rigueur de l'évaluation | Métriques adaptées au déséquilibre des classes, pas seulement l'accuracy |
| Explicabilité | Capacité à justifier une alerte, pas seulement à l'émettre |
| Analyse critique | Limites du modèle, biais potentiels, robustesse adversariale discutée |
| Communication | Rapport et présentation clairs, vulgarisation pour un public non technique |

---

# ANNEXE A · Certifications professionnelles reconnues

## A.1 Certifications cybersécurité généralistes

| Certification | Éditeur | Lien officiel |
|---|---|---|
| CompTIA Security+ | CompTIA | https://www.comptia.org/certifications/security |
| CompTIA CySA+ (Cybersecurity Analyst) | CompTIA | https://www.comptia.org/certifications/cybersecurity-analyst |
| CompTIA PenTest+ | CompTIA | https://www.comptia.org/certifications/pentest |
| CEH (Certified Ethical Hacker) | EC-Council | https://www.eccouncil.org/programs/certified-ethical-hacker-ceh/ |
| OSCP (Offensive Security Certified Professional) | OffSec | https://www.offsec.com/courses/pen-200/ |
| CISSP (Certified Information Systems Security Professional) | ISC2 | https://www.isc2.org/certifications/cissp |
| CISM (Certified Information Security Manager) | ISACA | https://www.isaca.org/credentialing/cism |
| GIAC GSEC / GCFA / GDAT | SANS/GIAC | https://www.giac.org/certifications/ |

## A.2 Certifications IA & sécurité de l'IA (2026)

| Certification | Éditeur | Focus | Lien officiel |
|---|---|---|---|
| CAISP (Certified AI Security Professional) | Practical DevSecOps | Technique/hands-on : LLM, MITRE ATLAS, OWASP LLM Top 10, threat modeling STRIDE, supply chain IA | https://www.practical-devsecops.com/certified-ai-security-professional/ |
| CompTIA SecAI+ | CompTIA | Vendor-neutre, extension de Security+/CySA+/PenTest+ vers l'IA (lancé février 2026) | https://www.comptia.org/certifications |
| AAISM (Advanced in AI Security Management) | ISACA | Gouvernance/management IA, nécessite CISM ou CISSP actif | https://www.isaca.org/credentialing |
| AIGP (Artificial Intelligence Governance Professional) | IAPP | Gouvernance et conformité IA (RGPD, EU AI Act) | https://iapp.org/certify/aigp/ |
| Microsoft Certified: Azure AI Engineer Associate (AI-102) | Microsoft | Sécurisation des services IA Azure | https://learn.microsoft.com/fr-fr/credentials/certifications/azure-ai-engineer/ |
| ISO/IEC 42001 Lead Auditor / Lead Implementer | Organismes accrédités (PECB, BSI…) | Système de management de l'IA (audit/implémentation) | https://www.iso.org/standard/81230.html |

> **Repères de gouvernance à connaître** (référencés dans les certifications ci-dessus) : OWASP Top 10 for LLM Applications (owasp.org/www-project-top-10-for-large-language-model-applications/), MITRE ATLAS (atlas.mitre.org), NIST AI Risk Management Framework (nist.gov/itl/ai-risk-management-framework).

## A.3 Certifications Machine Learning / Data Science appliquées

| Certification | Éditeur | Lien officiel |
|---|---|---|
| Microsoft Certified: Azure Data Scientist Associate (DP-100) | Microsoft | https://learn.microsoft.com/fr-fr/credentials/certifications/azure-data-scientist/ |
| Google Cloud Professional Machine Learning Engineer | Google Cloud | https://cloud.google.com/learn/certification/machine-learning-engineer |
| AWS Certified Machine Learning – Specialty | Amazon Web Services | https://aws.amazon.com/fr/certification/certified-machine-learning-specialty/ |
| TensorFlow Developer Certificate | Google | https://www.tensorflow.org/certificate |

> **Recommandation de parcours pour un profil double cybersécurité/data science** (cohérent avec un parcours ENSA Génie Informatique Digitalisation et Cybersécurité) :
> 1. **CompTIA Security+** puis **CySA+** — bases solides et largement reconnues internationalement.
> 2. **DP-100 (Azure Data Scientist)** ou **AWS ML Specialty** — valorise les compétences ML/DL du présent cours (chapitres II-III).
> 3. **CAISP** — spécialisation directe sur l'intersection IA × cybersécurité (chapitre IV), certification technique la plus alignée avec ce module.
> 4. **OSCP** — si orientation offensive/red team, en particulier pour approfondir le volet IA offensive (IV.1) et les attaques adversariales (IV.3).

*Note : tarifs, prérequis et formats d'examen évoluent régulièrement — vérifier les informations à jour sur le site officiel de chaque éditeur avant inscription.*

---

# ANNEXE B · Panorama des nouveaux outils (2026)

## B.1 Outils ML/DL pour la sécurité (frameworks et bibliothèques)

| Outil | Usage |
|---|---|
| **TensorFlow / Keras** | Framework DL généraliste, prototypage rapide de CNN/RNN pour la détection de menaces |
| **PyTorch** | Framework DL de référence en recherche, très utilisé pour les architectures Transformer de sécurité |
| **scikit-learn** | ML classique (chapitre II) : Random Forest, SVM, k-NN, clustering |
| **XGBoost / LightGBM** | Gradient boosting, standard de production pour la détection de fraude/intrusion sur données tabulaires |
| **Hugging Face Transformers** | Modèles de langage pré-entraînés pour l'analyse de logs, la classification de phishing par NLP |
| **imbalanced-learn** | Implémentation de SMOTE et autres techniques de gestion du déséquilibre des classes (II.2.d) |

## B.2 Outils de threat intelligence et d'analyse assistée par IA

| Outil | Positionnement |
|---|---|
| **MITRE ATLAS Navigator** | Cartographie des menaces adversariales contre les systèmes IA (équivalent ATT&CK Navigator pour l'IA) |
| **Microsoft Security Copilot** | Copilote IA générative intégré au SOC (threat hunting en langage naturel, résumé d'incidents) |
| **Google Threat Intelligence (Gemini-powered)** | Analyse de threat intelligence augmentée par IA générative |
| **CrowdStrike Charlotte AI** | Assistant IA pour l'analyse et la réponse aux incidents dans l'écosystème CrowdStrike Falcon |
| **Darktrace ActiveAI Security Platform** | Détection d'anomalies par IA non supervisée (proche des principes du chapitre III), auto-réponse |
| **Vectra AI** | Détection et réponse réseau (NDR) basée sur le ML comportemental |

## B.3 Outils de test et de red teaming pour l'IA (adversarial ML)

| Outil | Usage |
|---|---|
| **Garak** (NVIDIA) | Scanner de vulnérabilités LLM open source (prompt injection, jailbreak, fuites de données) |
| **PyRIT** (Microsoft) | Python Risk Identification Toolkit — red teaming automatisé de systèmes IA générative |
| **Adversarial Robustness Toolbox (ART)** (IBM/Linux Foundation AI) | Bibliothèque open source pour tester et défendre contre les attaques adversariales (evasion, poisoning, extraction — cf. IV.3) |
| **Counterfit** (Microsoft) | Outil d'évaluation de la sécurité des modèles ML en environnement de production |
| **Foolbox / CleverHans** | Bibliothèques de génération d'exemples adversariaux pour tester la robustesse des modèles DL |

## B.4 Outils de protection de la vie privée (Privacy-Enhancing Technologies)

| Outil | Technologie associée (cf. chapitre V) |
|---|---|
| **PySyft / PyGrid** (OpenMined) | Federated Learning et calcul sécurisé multi-parties |
| **TensorFlow Privacy** | Differential Privacy pour l'entraînement de modèles TensorFlow (DP-SGD) |
| **Opacus** (Meta) | Differential Privacy pour PyTorch |
| **Microsoft SEAL** | Bibliothèque de chiffrement homomorphe |
| **Presidio** (Microsoft) | Détection et anonymisation automatique de données personnelles (PII) dans du texte |

## B.5 Plateformes SOC / XDR intégrant l'IA nativement

| Outil | Positionnement |
|---|---|
| **Splunk (avec Splunk AI Assistant)** | SIEM avec assistance IA pour la rédaction de requêtes et la corrélation d'événements |
| **Microsoft Sentinel** | SIEM/SOAR cloud avec détection d'anomalies par ML intégrée |
| **Elastic Security** | SIEM open-core avec détection ML native |
| **Wazuh** | SIEM/XDR open source, alternative gratuite pour les projets académiques (adapté au chapitre VI) |

---

# ANNEXE C · Glossaire général

| Terme | Définition |
|---|---|
| CIA Triad | Confidentialité, Intégrité, Disponibilité — les trois piliers de la sécurité de l'information |
| IDS / IPS | Intrusion Detection/Prevention System — détection/prévention d'intrusion réseau |
| SIEM | Security Information and Event Management — centralisation et corrélation des logs de sécurité |
| SOC | Security Operations Center — équipe/plateforme de supervision de la sécurité |
| SOAR | Security Orchestration, Automation and Response — automatisation des réponses aux incidents |
| EDR / XDR | Endpoint / Extended Detection and Response — détection et réponse au niveau poste de travail / multi-sources |
| UEBA | User and Entity Behavior Analytics — analyse comportementale pour détecter les anomalies |
| APT | Advanced Persistent Threat — attaque furtive et prolongée, souvent étatique ou organisée |
| Zero-Day | Vulnérabilité inconnue du fabricant, sans correctif disponible |
| MLP / CNN / RNN | Multi-Layer Perceptron / Convolutional / Recurrent Neural Network — architectures de réseaux de neurones |
| Backpropagation | Algorithme de rétropropagation du gradient pour l'entraînement des réseaux de neurones |
| Concept drift | Évolution des motifs de données dans le temps, rendant un modèle obsolète (fréquent en cybersécurité) |
| SMOTE | Synthetic Minority Oversampling Technique — génération d'exemples synthétiques pour rééquilibrer les classes |
| Adversarial example | Entrée légèrement perturbée pour tromper un modèle IA |
| Data poisoning | Empoisonnement des données d'entraînement d'un modèle IA |
| Prompt injection | Instructions malveillantes visant à détourner le comportement d'un LLM |
| MITRE ATLAS | Référentiel des tactiques et techniques d'attaque contre les systèmes IA |
| Differential Privacy | Technique garantissant mathématiquement la confidentialité des individus dans des données/modèles |
| Federated Learning | Apprentissage distribué où les données ne quittent jamais leur environnement d'origine |
| XAI | Explainable AI — techniques rendant les décisions d'un modèle IA interprétables (SHAP, LIME, Grad-CAM) |
| RGPD / EU AI Act | Cadres réglementaires européens sur les données personnelles et l'intelligence artificielle |

---

*Support de cours original : Dr. HONNIT Bouchra — « IA pour la cybersécurité »*
*Version enrichie et complétée (chapitres II à VI développés en détail, certifications, panorama d'outils 2026) — Juillet 2026*
