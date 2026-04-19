# 🤖🔐 IA pour la Cybersécurité — Introduction Générale

> **Cours** : IA pour la Cybersécurité | **Dr. HONNIT Bouchra**

---

## 📚 Table des Matières

1. [Objectifs du cours](#1-objectifs-du-cours)
2. [Plan du module](#2-plan-du-module)
3. [Introduction à la Cybersécurité](#3-introduction-à-la-cybersécurité)
4. [Introduction à l'IA & Deep Learning](#4-introduction-à-lia--deep-learning)

---

## 1. Objectifs du Cours

| # | Objectif | Contenu |
|---|---|---|
| 1 | **Bases du Deep Learning** | MLP, CNN, RNN, Autoencoders, TensorFlow/Keras, PyTorch |
| 2 | **Enjeux de la cybersécurité** | Menaces, détection d'anomalies, classification, analyse de logs |
| 3 | **ML appliqué à la cybersécurité** | SVM, Random Forest, k-NN, pipelines de traitement |
| 4 | **DL pour la cybersécurité** | IDS, détection de malwares, classification de trafic, analyse d'e-mails |
| 5 | **Mini-projet IA** | Dataset réel, choix ML/DL, évaluation, documentation |
| 6 | **Analyse basée sur les données** | Explicabilité, éthique, robustesse, limites et perspectives |

### Prérequis

- Python (pandas, scikit-learn)
- Machine Learning supervisé / non supervisé
- Notions de classification / clustering
- Deep Learning (MLP, CNN, etc.)
- Bases de cybersécurité

---

## 2. Plan du Module

```
I.   Introduction générale          → Cybersécurité + IA & DL
II.  ML pour la cybersécurité       → Attaques, données, modèles ML
III. DL pour la cybersécurité       → Architectures, études de cas
IV.  IA offensive, défensive        → IA pour attaquer/défendre, attaques contre l'IA
V.   IA, cybersécurité & vie privée → RGPD, privacy-enhancing technologies
VI.  Projet de fin de module        → Présentation des projets
```

---

## 3. Introduction à la Cybersécurité

### 3.1 Définition & Enjeux

> La cybersécurité est l'ensemble des **méthodes**, **processus**, **outils** et **comportements** visant à **protéger** les systèmes informatiques, les réseaux et les données contre les cyberattaques et les accès non autorisés.

> ⚠️ Même si elle repose en grande partie sur la technologie, l'efficacité de la cybersécurité dépend **fortement des individus**.

**Les grands enjeux :**

- **Complexité croissante** : plus il y a d'outils et de technologies, plus la sécurité est difficile à gérer
- **Menaces en évolution** : les attaques sont de plus en plus sophistiquées et difficiles à détecter
- **Stratégies obsolètes** : les anciennes méthodes ne suffisent plus face aux menaces modernes

---

### 3.2 Concepts Clés

#### Concept 1 — CIA Triad

| Pilier | Définition | Exemple de violation |
|---|---|---|
| **Confidentialité** | Protection contre l'accès non autorisé | Vol de données, écoute réseau |
| **Intégrité** | Les données n'ont pas été altérées | Modification d'un fichier de log |
| **Disponibilité** | Accès garanti aux ressources autorisées | Attaque DDoS qui rend un site inaccessible |

#### Concept 2 — AAA (Authentification, Autorisation, Audit)

| Composant | Question | Exemple |
|---|---|---|
| **Authentification** | Qui êtes-vous ? | Login + mot de passe, MFA |
| **Autorisation** | Que pouvez-vous faire ? | RBAC, ACL |
| **Audit** | Qu'avez-vous fait ? | Logs, SIEM, journalisation |

#### Concept 3 — Menaces, Vulnérabilités, Risques

```
Risque = Menace × Vulnérabilité × Impact
```

| Terme | Définition | Exemple |
|---|---|---|
| **Menace** | Danger potentiel | Hacker, malware |
| **Vulnérabilité** | Faille exploitable | Port ouvert, mot de passe faible |
| **Risque** | Impact potentiel si la menace exploite la vulnérabilité | Perte de données critiques |

#### Concept 4 — Mesures de Sécurité (Controls)

| Type | Rôle | Exemples |
|---|---|---|
| **Préventives** | Éviter l'incident | Firewall, antivirus, formation |
| **Détectives** | Identifier l'incident | SIEM, IDS/IPS |
| **Correctives** | Corriger après l'incident | Restauration, patchs de sécurité |

#### Concept 5 — Principes de Sécurité

- **Least Privilege** (moindre privilège) — donner uniquement les droits nécessaires
- **Defense in Depth** (défense en profondeur) — plusieurs couches de protection
- **Fail Secure** — mieux vaut bloquer qu'ouvrir en cas de problème
- **Security by Design** — penser sécurité dès la conception

#### Concept 6 — Types de Sécurité

| Type | Description |
|---|---|
| **Sécurité physique** | Accès aux serveurs, caméras, badges |
| **Sécurité logique** | Mots de passe, pare-feux, antivirus, chiffrement |
| **Sécurité organisationnelle** | Politiques internes, procédures, formation |

---

### 3.3 Types d'Attaques

#### Vue d'ensemble — Attaques vs CIA Triad

| Attaque | Confidentialité | Intégrité | Disponibilité |
|---|:---:|:---:|:---:|
| Phishing | ✅ | | |
| Data Breach | ✅ | | |
| Sniffing / Eavesdropping | ✅ | | |
| Keylogging | ✅ | | |
| MITM | ✅ | ✅ | |
| SQL Injection | ✅ | ✅ | |
| DoS / DDoS | | | ✅ |
| Botnet | ✅ | | ✅ |
| Ransomware | ✅ | ✅ | ✅ |
| Virus / Ver / Trojan | ✅ | ✅ | ✅ |
| APT | ✅ | ✅ | |
| Zero-Day | ✅ | ✅ | ✅ |

---

#### 🎣 Attaques par Ingénierie Sociale

**Phishing**
- Envoi d'e-mails frauduleux imitant une source de confiance pour voler des informations sensibles
- L'attaquant utilise un lien piégé vers un site malveillant ou pour télécharger un malware
- Protection : vérifier les en-têtes d'e-mail, les champs `Reply-to` et `Return-path`

**Spear Phishing**
- Cible une personne **spécifique** après une phase de recherche approfondie
- Tactiques : e-mails personnalisés, usurpation d'identité (spoofing), clonage de sites web
- Protection : vérifier minutieusement les adresses e-mail, les URLs

**Whale Phishing**
- Cible les **hauts responsables** (CEO, CFO, dirigeants)
- Objectif : obtenir des informations sensibles ou exercer une pression via ransomware
- Protection : mêmes précautions que le phishing classique, vigilance accrue

> 💡 **L'humain est le maillon faible.**

---

#### 🔒 Attaques sur la Confidentialité

**Data Breach (Vol de données)**
- Accès non autorisé à une base de données (mots de passe, données bancaires, dossiers médicaux)
- Souvent dû à : mot de passe faible, mauvaise configuration serveur, vulnérabilité logicielle
- Protection : MFA, chiffrement des données, moindre privilège, SIEM, mises à jour régulières

**Sniffing / Eavesdropping**
- Écoute passive des communications réseau (ex : Wi-Fi non sécurisé → capture de mots de passe en clair)
- Protection : HTTPS/TLS, VPN, segmentation réseau, IDS/IPS

**Keylogging**
- Logiciel ou matériel enregistrant tout ce que l'utilisateur tape (mots de passe, données bancaires)
- Installé via malware, phishing ou clé USB malveillante
- Protection : antivirus/EDR, clavier virtuel, 2FA, vérification des périphériques physiques

---

#### 🌊 Attaques sur la Disponibilité

**DoS (Denial of Service)**
- Sature les ressources d'un système jusqu'à le rendre incapable de répondre aux requêtes légitimes
- L'objectif n'est pas l'accès au système mais de **perturber son fonctionnement**

**DDoS (Distributed DoS)**
- Lancée depuis un grand nombre de machines infectées (botnet)
- Exemple célèbre : attaque contre **AWS en février 2020**
- Protection : pare-feu filtrant, anti-DDoS, CDN, rate limiting

**Botnet**
- Réseau d'ordinateurs infectés (« zombies ») contrôlés à distance par un attaquant
- Usages : DDoS, spam massif, vol d'identifiants, minage de cryptomonnaie
- Exemple : 100 000 machines infectées → armée pour saturer un serveur cible

---

#### ⚙️ Attaques sur l'Intégrité

**SQL Injection**
- Injection de code SQL malveillant dans des champs de saisie pour manipuler une base de données
- Conséquences : fuite, modification, suppression de données, voire exécution de commandes système
- Protection : requêtes préparées (Prepared Statements), validation des entrées, moindre privilège

**MITM (Man-in-the-Middle)**
- L'attaquant s'interpose entre deux parties communicantes à leur insu
- Variante : **Session Hijacking** — prise de contrôle d'une session client/serveur
- Protection : chiffrement fort (TLS), VPN

---

#### 🦠 Logiciels Malveillants (Malwares)

| Malware | Mécanisme | Exemple |
|---|---|---|
| **Virus** | S'attache à un fichier légitime, se propage à l'ouverture | Fichier infecté sur clé USB |
| **Ver (Worm)** | Se propage automatiquement via le réseau, sans action utilisateur | WannaCry (2017) |
| **Trojan** | Se fait passer pour un logiciel utile, installe une backdoor | Faux logiciel de facturation |
| **Ransomware** | Chiffre les données et demande une rançon | LockBit, REvil, WannaCry |

**Protection commune :**
- Antivirus/EDR à jour
- Ne pas ouvrir de pièces jointes suspectes
- Mises à jour système régulières
- Limiter les droits administrateurs

---

#### 🎯 Attaques Avancées

**APT (Advanced Persistent Threats)**
- Attaques longues et discrètes, souvent menées par des groupes organisés (cyber-espionnage)
- L'attaquant s'infiltre, reste caché et exfiltre des données sur des **mois, voire des années**
- Protection : surveillance continue (SIEM), segmentation réseau, threat intelligence, sécurité des accès privilégiés

**Zero-Day**
- Exploitent une faille **encore inconnue du fabricant** → aucun correctif disponible
- Très dangereuses : indétectables par les défenses classiques basées sur signatures
- Protection : détection comportementale (EDR, SIEM), réduction de la surface d'attaque, patching rapide

---

## 4. Introduction à l'IA & Deep Learning

### 4.1 Définitions et Hiérarchie

```
Intelligence Artificielle (IA)
    └── Machine Learning (ML)
            └── Deep Learning (DL)
```

| Niveau | Définition | Caractéristiques |
|---|---|---|
| **IA** | Systèmes imitant des comportements humains intelligents | Peut inclure règles, agents, ML, DL |
| **ML** | Les machines apprennent automatiquement à partir de données | K-NN, SVM, Random Forest, Régression |
| **DL** | Réseaux de neurones profonds apprenant des représentations complexes | CNN, RNN, LSTM, Transformers |

---

### 4.2 ML vs Deep Learning

| Critère | Machine Learning | Deep Learning |
|---|---|---|
| Type de données | Tableaux (features tabulaires) | Images, audio, texte, séquences |
| Quantité de données | Peu suffisent | Beaucoup (1000s à millions d'exemples) |
| Prétraitement | Feature engineering nécessaire | Moins nécessaire (le réseau apprend seul) |
| Temps d'entraînement | Rapide | Long (surtout sans GPU) |
| Interprétabilité | Plus facile | Moins interprétable (« boîte noire ») |

#### Quand utiliser ML ?
- Données structurées/tabulaires
- Dataset de taille modeste (1k à 100k lignes)
- Besoin d'interprétabilité
- Ressources de calcul limitées

#### Quand utiliser DL ?
- Données non structurées : images, sons, textes, séries temporelles longues
- Très grand volume de données (> 100k exemples)
- Haute performance prioritaire sur l'interprétabilité

> 💡 **L'interprétabilité est cruciale** en médecine (justifier un diagnostic), en banque (expliquer un refus de prêt), et en **cybersécurité** (justifier une alerte vs faux positif).

---

### 4.3 Structure d'un Réseau de Neurones

```
Données → [Couche d'entrée] → [Couches cachées] → [Couche de sortie] → Prédiction
```

#### Couche d'entrée
- Reçoit les données brutes encodées sous forme numérique
- Ne fait pas de calcul d'apprentissage
- Exemples : image 28×28 → 784 neurones, texte → embeddings, audio → spectrogramme

#### Couches cachées
- C'est là où se fait l'**apprentissage**
- Chaque neurone calcule : `z = W·x + b` puis applique une fonction d'activation `a = f(z)`
- La "profondeur" = nombre de couches cachées

#### Couche de sortie
- Transforme les représentations apprises en résultat final

| Tâche | Activation | Fonction de coût |
|---|---|---|
| Régression | Identity (linéaire) | MSE / MAE |
| Classification binaire | Sigmoid → [0,1] | Binary Cross-Entropy |
| Classification multi-classes | Softmax → somme = 1 | Cross-Entropy |
| Multi-label | Sigmoid (par neurone) | Binary Cross-Entropy |

---

### 4.4 Fonctions d'Activation

#### Pour les couches cachées

| Fonction | Formule | Avantages | Limites | Usage |
|---|---|---|---|---|
| **ReLU** | `max(0, x)` | Simple, efficace, réduit vanishing gradient | Neurones morts | Standard (CNN, MLP) |
| **Leaky ReLU** | `x if x≥0, αx if x<0` | Évite les neurones morts (α petit) | — | Remplacement de ReLU |
| **ELU** | `x if x≥0, α(eˣ-1) if x<0` | Plus lisse que Leaky ReLU | — | CNN |
| **Tanh** | `(eˣ-e⁻ˣ)/(eˣ+e⁻ˣ)` → [-1,1] | Centrée en zéro | Saturation | RNN, séquences |
| **Sigmoid** | `1/(1+e⁻ˣ)` → [0,1] | Interprétable (probabilité) | Vanishing gradient | Couche de sortie binaire |
| **Swish** | `x · sigmoid(x)` | Meilleur flux de gradient | — | Transformers, EfficientNet |
| **Mish** | `x · tanh(softplus(x))` | Très lisse | — | Architectures récentes |

---

### 4.5 Types de Couches Cachées

#### Dense (Fully Connected)
- Chaque neurone connecté à **tous** les neurones de la couche précédente
- Couche la plus générale
- Utilisation : classification, MLP, couches de sortie après CNN/RNN

#### Convolutionnelle (CNN)
- Applique des filtres (kernels) qui balayent l'entrée pour extraire des motifs
- Poids **partagés** → moins de paramètres que Dense
- Les filtres sont appris automatiquement par backpropagation
- Utilisation : vision par ordinateur, traitement audio, NLP (Conv1D)

#### Récurrente (RNN, LSTM, GRU)
- La sortie dépend de l'entrée actuelle **et de l'état précédent** : `hₜ = f(Wxₜ + Uhₜ₋₁ + b)`
- LSTM/GRU : ajoutent des **gates** (portes) pour contrôler ce qu'on garde ou oublie
- Utilisation : texte, audio, séries temporelles

#### Dropout
- Éteint aléatoirement un % de neurones pendant l'entraînement (`p = 0.2 à 0.5`)
- Rôle : **régularisation** → évite le surapprentissage (overfitting)
- Valeurs courantes : 0.2–0.3 pour CNN, 0.5 pour Dense

#### Batch Normalization
- Normalise les activations par mini-batch (moyenne ≈ 0, variance ≈ 1)
- Formule : `x̂ = (x - μ) / √(σ² + ε)`, puis `y = γx̂ + β`
- Stabilise et accélère l'entraînement

---

### 4.6 Cycle d'Apprentissage

```
┌─────────────────────────────────────────────────────────┐
│              BOUCLE D'ENTRAÎNEMENT                      │
│                                                         │
│  Pour chaque mini-batch :                               │
│                                                         │
│  1. FORWARD PASS    → Calculer la prédiction ŷ          │
│  2. LOSS            → Mesurer l'erreur L(y, ŷ)          │
│  3. BACKPROPAGATION → Calculer les gradients ∂L/∂W      │
│  4. GRADIENT DESCENT→ Mettre à jour W ← W - η·∂L/∂W    │
│                                                         │
│  ↺ Répéter pour chaque époque jusqu'à convergence       │
└─────────────────────────────────────────────────────────┘
```

**Paramètres clés :**
- **η (learning rate)** : pas de mise à jour des poids — trop grand → diverge, trop petit → lent
- **Époque** : passage complet sur tout le dataset
- **Mini-batch** : sous-ensemble de données traité à chaque itération

#### Fonctions de perte (Loss Functions)

| Tâche | Formule | Nom |
|---|---|---|
| Régression | `L = (1/n) Σ(ŷᵢ - yᵢ)²` | MSE |
| Classification binaire | `L = -(1/n) Σ[y·log(ŷ) + (1-y)·log(1-ŷ)]` | Binary Cross-Entropy |
| Classification multi-classes | `L = -(1/n) Σᵢ Σⱼ yᵢⱼ·log(ŷᵢⱼ)` | Cross-Entropy |

---

### 4.7 Lien IA ↔ Cybersécurité

```
         ┌─────────────────────────────────────┐
         │         CYBERSÉCURITÉ               │
         │                                     │
  Lien   │  Protéger les données, modèles      │  Lien
 positif │  et décisions de l'IA               │ négatif
    ↑    └─────────────────────────────────────┘   ↑
    │                    ↕                          │
    │     ┌─────────────────────────────────┐      │
    └─────│           IA                   │──────┘
          │                                 │
          │  Détection de menaces,          │
          │  analyse d'anomalies,           │
          │  réponse automatique            │
          └─────────────────────────────────┘
```

#### Ce que l'IA peut détecter / traiter

| Domaine | Application |
|---|---|
| **Détection d'intrusions (IDS)** | Classification de trafic réseau normal vs malveillant |
| **Détection de malwares** | Analyse comportementale, classification de binaires |
| **Anti-phishing** | Analyse de texte et d'URLs d'e-mails |
| **Analyse de logs** | Détection d'anomalies dans les journaux système |
| **Détection de DDoS** | Identification de pics de trafic anormaux |

#### Ce que l'IA peut générer (usage offensif)

| Menace | Description |
|---|---|
| **E-mails malveillants générés par IA** | Phishing ultra-personnalisé et convaincant |
| **Deepfakes** | Audio/vidéo falsifiés pour le vishing/whaling |
| **Attaques adversariales** | Inputs modifiés pour tromper les modèles de DL |
| **Data Poisoning** | Contamination des données d'entraînement |

> ⚠️ **L'IA est une arme à double tranchant** : elle renforce la défense mais aussi la capacité offensive des attaquants.

---

## 📝 Résumé

| Section | Points clés |
|---|---|
| **Cybersécurité** | CIA Triad + AAA + Risque = Menace × Vulnérabilité × Impact |
| **Types d'attaques** | Ingénierie sociale, réseau, applicatives, malwares, attaques avancées |
| **IA vs DL** | ML = données tabulaires + interprétabilité / DL = données complexes + haute performance |
| **Réseau de neurones** | Input → Hidden (Dense, CNN, RNN, Dropout, BN) → Output |
| **Apprentissage** | Forward pass → Loss → Backprop → Gradient Descent |
| **IA + Cyber** | IA pour défendre (IDS, anti-phishing) ET pour attaquer (deepfakes, adversarial) |

---

*Références : Dr. HONNIT Bouchra — Cours IA pour la Cybersécurité | OWASP | NIST | Scikit-learn documentation | TensorFlow/Keras documentation*
