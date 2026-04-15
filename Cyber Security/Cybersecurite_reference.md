# 🔐 Référence Complète en Cybersécurité

> **Note :** Ce document est un résumé de référence destiné à un usage personnel/éducatif. Il couvre les fondamentaux de la cybersécurité, les menaces, la protection des systèmes, et la conformité.

---

## 📚 Table des Matières

1. [Introduction à la Cybersécurité](#1-introduction-à-la-cybersécurité)
2. [Fondements de la Sécurité Informatique](#2-fondements-de-la-sécurité-informatique)
3. [Menaces, Vulnérabilités et Types d'Attaques](#3-menaces-vulnérabilités-et-types-dattaques)
4. [Protection des Réseaux et des Systèmes](#4-protection-des-réseaux-et-des-systèmes)
5. [Sécurité des Applications](#5-sécurité-des-applications)
6. [Détection et Réponse aux Incidents](#6-détection-et-réponse-aux-incidents)
7. [Gestion des Risques et Conformité](#7-gestion-des-risques-et-conformité)
8. [Ressources et Références](#8-ressources-et-références)

---

## 1. Introduction à la Cybersécurité

### 1.1 Définition

La **cybersécurité** regroupe l'ensemble des technologies, pratiques, processus et stratégies visant à protéger les **systèmes d'information**, les **réseaux**, les **applications** et les **données** contre les attaques, les dommages ou les accès non autorisés.

Elle couvre plusieurs dimensions :

| Domaine | Description |
|---|---|
| Sécurité réseau | Protection des flux et infrastructures réseau |
| Sécurité des systèmes | Hardening OS, gestion des accès |
| Sécurité applicative | Développement sécurisé, OWASP |
| Cloud & Mobile | Sécurisation des environnements cloud et appareils mobiles |
| Gouvernance & conformité | ISO 27001, RGPD, NIST |
| Sécurité physique | Contrôle d'accès physique aux locaux et matériels |

### 1.2 Importance stratégique

- **Protection des données sensibles** : clients, employés, secrets industriels
- **Continuité des services** : éviter les interruptions dues aux attaques
- **Réduction des coûts** : une cyberattaque peut coûter des millions
- **Image & confiance** : une fuite de données peut détruire la réputation
- **Conformité légale** : RGPD, lois nationales, normes ISO

#### Chiffres clés — Maroc (2024)

- 🇲🇦 3ème pays africain le plus touché par les cyberattaques
- 💸 Perte moyenne par PME : **1,2 à 2,3 MDH** par incident
- 📈 Hausse de **210%** des attaques bancaires au T1 2024
- 🎣 Plus de **6,4 millions** de tentatives de phishing neutralisées
- ⚠️ 62% des PME victimes, mais seulement **28% ont un plan de cybersécurité**

### 1.3 Panorama des menaces

#### Motivations des attaquants

- 💰 **Financières** : ransomware, fraude, revente de données
- 🏛️ **Politique / idéologique** : hacktivisme
- 💥 **Sabotage** : attaques sur infrastructures critiques
- 🎮 **Défi personnel** : script kiddies, curiosité

#### Acteurs

| Acteur | Description |
|---|---|
| Cybercriminels organisés | Groupes motivés par le gain financier |
| États / APT | Advanced Persistent Threat, espionnage à long terme |
| Hacktivistes | Anonymous, motivations politiques |
| Insiders | Employés malveillants ou négligents |
| Compétiteurs industriels | Espionnage économique |

### 1.4 Évolution historique

```
1980-1990  → Premiers virus (Morris Worm, ILOVEYOU)
2000       → Internet grand public, SQL Slammer, Blaster
2010       → Ransomwares à grande échelle, Stuxnet, vols Yahoo!/Equifax
2020+      → Cloud, IoT, RaaS, attaques supply chain (SolarWinds), IA dans les cyberattaques
```

### 1.5 Terminologie essentielle

| Terme | Définition |
|---|---|
| **Menace** | Événement potentiel pouvant causer un dommage |
| **Vulnérabilité** | Faiblesse exploitable dans un système |
| **Risque** | Menace × Vulnérabilité × Impact |
| **Attaque** | Action exploitant une vulnérabilité pour nuire |
| **Actif** | Tout élément de valeur pour l'organisation |
| **Incident** | Événement compromettant CIA d'un système |
| **Exploit** | Code/technique tirant parti d'une vulnérabilité |

---

## 2. Fondements de la Sécurité Informatique

### 2.1 Le Modèle CIA

Le modèle **CIA** est la base de toute stratégie de cybersécurité.

```
┌─────────────────────────────────────────┐
│              MODÈLE CIA                 │
│                                         │
│  Confidentialité  Intégrité  Disponibilité│
│        (C)           (I)        (A)     │
└─────────────────────────────────────────┘
```

#### Confidentialité (Confidentiality)
> Garantit que seules les personnes autorisées accèdent aux informations.

- Chiffrement (HTTPS, VPN, TLS)
- Contrôle d'accès basé sur les rôles (RBAC)
- Authentification forte (MFA)

#### Intégrité (Integrity)
> Garantit que les données sont exactes et non altérées.

- Fonctions de hachage (SHA-256, SHA-3)
- Signatures numériques (RSA, ECDSA)
- HMAC (Hash-based Message Authentication Code)

#### Disponibilité (Availability)
> Garantit l'accessibilité des systèmes quand nécessaire.

- Redondance et clustering
- Plans de reprise d'activité (PRA/PCA)
- Protection anti-DDoS

> ⚠️ Les 3 composants sont indissociables : un équilibre doit être trouvé.

### 2.2 Le Modèle AAA

| Composant | Question | Exemples |
|---|---|---|
| **Authentication** | Qui êtes-vous ? | MFA, biométrie, certificats |
| **Authorization** | Que pouvez-vous faire ? | RBAC, ACL, politiques IAM |
| **Accounting** | Qu'avez-vous fait ? | Logs, SIEM, audit trails |

```
CIA  = Ce que l'on veut protéger
AAA  = Comment on contrôle l'accès à ce qu'on protège
```

### 2.3 Cryptographie

#### Historique

| Époque | Événement |
|---|---|
| 1er siècle | Chiffre de César (décalage de 3) |
| 9e siècle | Al-Kindi — analyse fréquentielle |
| 16e siècle | Chiffre de Vigenère (polyalphabétique) |
| 1918-1945 | Machine Enigma (décryptée par Alan Turing) |
| 1977 | DES — 56 bits (obsolète) |
| 1976-1977 | Diffie-Hellman + RSA — cryptographie asymétrique |
| 2001 | AES — 128/192/256 bits (standard actuel) |
| 2024+ | Cryptographie post-quantique (CRYSTALS-Kyber, CRYSTALS-Dilithium) |

#### Chiffrement Symétrique vs Asymétrique

| Critère | Symétrique | Asymétrique |
|---|---|---|
| Clés | 1 clé partagée | Paire clé publique/privée |
| Vitesse | ⚡ Rapide | 🐢 Lent |
| Usage | Chiffrement de données volumineuses | Échange de clés, signatures |
| Exemples | AES, DES, 3DES, ChaCha20 | RSA, ECC, Diffie-Hellman |
| Utilisation | VPN, disques chiffrés, TLS session | Certificats TLS, emails signés |

#### Hachage Cryptographique

**Propriétés clés :**
- **Déterministe** : même donnée → même hash
- **Effet avalanche** : petite modification → hash complètement différent
- **Unidirectionnel** : impossible de retrouver les données originales
- **Résistance aux collisions** : difficile de trouver deux données avec le même hash

| Algorithme | Taille | Statut |
|---|---|---|
| MD5 | 128 bits | ❌ Obsolète (collisions connues) |
| SHA-1 | 160 bits | ❌ Obsolète |
| SHA-256 | 256 bits | ✅ Recommandé |
| SHA-3 | Variable | ✅ Recommandé |
| BLAKE2/BLAKE3 | Variable | ✅ Recommandé (très rapide) |

#### Signatures Numériques

Garantissent simultanément :
- ✅ **Authentification** : l'expéditeur est bien celui qu'il prétend être
- ✅ **Intégrité** : le message n'a pas été modifié
- ✅ **Non-répudiation** : l'expéditeur ne peut pas nier avoir envoyé le message

> ⚠️ La signature numérique ne garantit **PAS** la confidentialité — il faut aussi chiffrer le message.

#### Tableau récapitulatif des garanties

| Mécanisme | Confidentialité | Intégrité | Authentification | Non-répudiation |
|---|:---:|:---:|:---:|:---:|
| Chiffrement symétrique | ✅ | ❌ | ❌ | ❌ |
| Chiffrement asymétrique | ✅ | ❌ | ❌ | ❌ |
| Hachage (SHA-256) | ❌ | ✅ | ❌ | ❌ |
| HMAC | ❌ | ✅ | ✅ | ❌ |
| Signature numérique | ❌ | ✅ | ✅ | ✅ |
| TLS (HTTPS) | ✅ | ✅ | ✅ | ❌ |

---

## 3. Menaces, Vulnérabilités et Types d'Attaques

### 3.1 Logiciels Malveillants (Malwares)

| Type | Description | Propagation | Exemples |
|---|---|---|---|
| **Virus** | Infecte des fichiers existants | Action humaine requise | ILOVEYOU, Melissa |
| **Ver (Worm)** | Se propage de manière autonome | Réseau / vulnérabilités | Conficker, WannaCry |
| **Trojan** | Se déguise en logiciel légitime | Téléchargement | Zeus, Emotet |
| **Ransomware** | Chiffre les données et demande rançon | Phishing, RDP, failles | WannaCry, LockBit, REvil |
| **Spyware** | Espionnage des activités (keylogging) | Installation silencieuse | FinFisher, Pegasus |
| **Adware** | Publicités indésirables | Bundled software | - |
| **Rootkit** | Dissimule sa présence dans le système | Exploitation de failles | - |
| **Botnet** | Réseau de machines compromises | Malware | Mirai, Necurs |

> 🆕 **Tendance 2024-2025 :** Le modèle **Ransomware-as-a-Service (RaaS)** permet à des criminels non techniques de lancer des attaques ransomware. Les groupes comme LockBit, ALPHV/BlackCat opèrent comme de véritables entreprises avec support client et affiliés.

### 3.2 Ingénierie Sociale

#### Phishing et variantes

| Variante | Vecteur | Description |
|---|---|---|
| **Phishing** | Email | Masse, lien malveillant |
| **Spear Phishing** | Email ciblé | Attaque personnalisée (nom, poste) |
| **Whaling** | Email dirigeants | Cible les C-levels |
| **Smishing** | SMS | Faux messages bancaires |
| **Vishing** | Téléphone | Fausse assistance technique |
| **Quishing** | QR Code | QR code malveillant |

> 🆕 **Tendance 2024-2025 :** L'IA générative (deepfakes audio/vidéo) est de plus en plus utilisée pour rendre les attaques de vishing/whaling extrêmement convaincantes.

### 3.3 Attaques Réseau

#### DoS / DDoS

| Type | Description |
|---|---|
| **DoS** | Une seule source surcharge la cible |
| **DDoS** | Milliers de machines (botnet) submergent la cible |
| **Volumétrique** | Saturation de bande passante (UDP flood, ICMP flood) |
| **Applicatif (L7)** | Épuisement des ressources serveur (HTTP flood, Slowloris) |
| **Protocol** | Exploitation de failles protocoles (SYN flood, Smurf) |

#### Attaques d'interception

```
Sniffing    → Écoute passive du trafic réseau non chiffré
MITM        → Interception active entre deux parties communicantes
ARP Spoofing → Association de l'adresse MAC attaquant avec l'IP cible
DNS Spoofing → Redirection vers un serveur malveillant via faux enregistrements DNS
SSL Stripping → Dégradation HTTPS → HTTP pour intercepter le trafic
```

### 3.4 Attaques Applicatives

#### SQL Injection

```sql
-- Requête normale
SELECT * FROM users WHERE username='alice' AND password='secret';

-- Payload d'injection
username: ' OR '1'='1
-- Résultat
SELECT * FROM users WHERE username='' OR '1'='1' AND password='';
-- Retourne TOUS les utilisateurs → contournement d'authentification
```

#### XSS (Cross-Site Scripting)

```
Reflected XSS  → Le payload est dans l'URL, exécuté immédiatement
Stored XSS     → Le payload est stocké en BDD, exécuté pour chaque visiteur
DOM-Based XSS  → Manipulation du DOM côté client
```

### 3.5 Attaques Avancées

#### APT (Advanced Persistent Threat)

Phases d'une attaque APT :
```
1. Reconnaissance     → OSINT, scan réseau
2. Intrusion initiale → Spear phishing, exploit zero-day
3. Établissement      → Backdoor, persistance
4. Mouvement latéral  → Élévation de privilèges, pivoting
5. Collecte           → Identification des données cibles
6. Exfiltration       → Transfert discret des données
7. Couverture         → Effacement des traces
```

#### Zero-Day

> Une vulnérabilité **inconnue du fournisseur**, donc sans correctif disponible. Extrêmement dangereuse car indétectable par les défenses classiques basées sur des signatures.

---

## 4. Protection des Réseaux et des Systèmes

### 4.1 Pare-feu (Firewall)

| Type | Fonctionnement | Avantages | Limites |
|---|---|---|---|
| **Stateless (filtrage de paquets)** | Analyse IP/port sans état | Rapide | Peu intelligent |
| **Stateful** | Suit l'état des connexions TCP | Plus sécurisé | Moins performant |
| **Applicatif / NGFW** | DPI, inspection du contenu | Détecte SQL, XSS, patterns | Coûteux en ressources |
| **WAF** | Spécialisé pour les apps web | OWASP Top 10 | Uniquement couche applicative |

### 4.2 Segmentation Réseau

```
VLAN          → Isolation logique sur réseau physique
Subnetting    → Isolation par sous-réseaux IP
DMZ           → Zone tampon entre Internet et réseau interne
Micro-seg.    → Contrôle machine-à-machine (cloud, VMs)
Zero Trust    → "Ne jamais faire confiance, toujours vérifier"
```

#### Architecture DMZ typique

```
Internet
    │
[Firewall Externe]
    │
   DMZ
  ├── Serveur Web
  ├── Serveur Mail
  └── Reverse Proxy
    │
[Firewall Interne]
    │
Réseau Interne
  ├── Serveurs d'application
  ├── Base de données
  └── Active Directory
```

### 4.3 IDS / IPS

| Système | Rôle | Exemples |
|---|---|---|
| **NIDS** | Surveille le trafic réseau | Snort, Suricata |
| **HIDS** | Surveille un hôte spécifique | OSSEC, Wazuh |
| **IPS** | Détecte ET bloque en temps réel | Suricata (mode inline) |

**Méthodes de détection :**
- **Signatures** : compare avec des patterns d'attaques connus
- **Anomalies** : détecte les écarts par rapport à la baseline
- **Hybride** : combine les deux approches

### 4.4 Protocoles de Sécurisation des Communications

#### TLS/SSL (Transport Layer Security)

```
Handshake TLS 1.3 (simplifié) :
Client ──[ClientHello]──────────────→ Serveur
Client ←─[ServerHello + Certificat]── Serveur
Client ──[Clé de session chiffrée]──→ Serveur
         ↕ Communications chiffrées ↕
```

- Assure : Confidentialité, Intégrité, Authentification du serveur
- ⚠️ TLS 1.0 et 1.1 sont **dépréciés** — utiliser **TLS 1.2 ou 1.3**

#### SSH vs Telnet

| | SSH | Telnet |
|---|---|---|
| Chiffrement | ✅ Oui | ❌ Non (clair) |
| Port par défaut | 22 | 23 |
| Authentification | Mot de passe / Clé privée | Mot de passe en clair |
| Utilisation recommandée | ✅ Toujours | ❌ Jamais en prod |

#### VPN

| Type | Protocole | Usage |
|---|---|---|
| **Site-to-Site** | IPSec, GRE | Interconnexion sites distants |
| **Remote Access** | SSL/TLS, OpenVPN, WireGuard | Télétravail |
| **Zero Trust Network Access (ZTNA)** | Moderne | Remplace le VPN traditionnel |

---

## 5. Sécurité des Applications

### 5.1 SDLC Sécurisé

```
PLANIFICATION  → Exigences sécurité, conformité, données sensibles
CONCEPTION     → Threat modeling, architecture sécurisée, design patterns
DÉVELOPPEMENT  → Codage sécurisé, revue de code, gestion des secrets
TESTS          → SAST, DAST, pentest, fuzzing
DÉPLOIEMENT    → Hardening, configuration sécurisée, validation finale
MAINTENANCE    → Surveillance, patching, réponse aux vulnérabilités
```

> 💡 **Shift-Left Security** : intégrer la sécurité le plus tôt possible dans le cycle de développement réduit les coûts de correction par un facteur 10 à 100.

### 5.2 OWASP Top 10 (2021)

| # | Vulnérabilité | Description courte |
|---|---|---|
| A01 | **Broken Access Control** | Accès non autorisé aux ressources |
| A02 | **Cryptographic Failures** | Données sensibles non chiffrées ou algo faible |
| A03 | **Injection** | SQL, Command, LDAP, XPath injection |
| A04 | **Insecure Design** | Défauts de conception inhérents |
| A05 | **Security Misconfiguration** | Config par défaut, services inutiles |
| A06 | **Vulnerable Components** | Bibliothèques/frameworks obsolètes |
| A07 | **Auth Failures** | Mots de passe faibles, absence MFA |
| A08 | **Data Integrity Failures** | MAJ sans vérification d'intégrité, CI/CD non sécurisé |
| A09 | **Logging Failures** | Logs insuffisants, pas d'alertes |
| A10 | **SSRF** | Serveur forcé à faire des requêtes internes |

### 5.3 SAST vs DAST

| Critère | SAST | DAST |
|---|---|---|
| Accès au code | ✅ Oui | ❌ Non |
| Phase | Développement | Test / Production |
| Type d'analyse | Statique (code) | Dynamique (exécution) |
| Faux positifs | Plus fréquents | Moins fréquents |
| Vision attaque | Théorique | Réaliste |
| Outils connus | SonarQube, Semgrep, Checkmarx | OWASP ZAP, Burp Suite, Nikto |

> ✅ **SAST + DAST + Pentest = approche complète de test de sécurité**

### 5.4 Bonnes Pratiques de Développement Sécurisé

```
✅ Valider TOUTES les entrées utilisateur (whitelist > blacklist)
✅ Utiliser des requêtes préparées (Prepared Statements) contre SQLi
✅ Ne jamais stocker de secrets dans le code source
✅ Utiliser un gestionnaire de secrets (Vault, AWS Secrets Manager)
✅ Encoder les sorties (contre XSS)
✅ Implémenter le principe du moindre privilège
✅ Mettre à jour régulièrement les dépendances (Dependabot, Snyk)
✅ Activer les headers de sécurité HTTP (CSP, HSTS, X-Frame-Options)
✅ Logger les événements de sécurité
✅ Implémenter l'authentification MFA
```

---

## 6. Détection et Réponse aux Incidents

### 6.1 Cycle de Vie d'un Incident

```
1. PRÉPARATION       → Politiques, outils, formation des équipes
2. DÉTECTION         → SIEM, IDS, alertes, signalement
3. ANALYSE           → Qualification, triage, investigation
4. CONFINEMENT       → Isolation des systèmes compromis
5. ÉRADICATION       → Suppression du malware, correction des failles
6. RÉCUPÉRATION      → Restauration des services
7. POST-INCIDENT     → Retour d'expérience (REX), leçons apprises
```

> 📊 Selon Mandiant 2023 : le temps de résidence moyen mondial est de **16 jours** (mais peut atteindre plusieurs mois dans certains cas).

### 6.2 Indicateurs de Compromission (IoC)

| Catégorie | Exemples |
|---|---|
| **Réseau** | Connexions vers IP C2, DNS excessif, exfiltration de données |
| **Fichiers** | Hashes malveillants (MD5/SHA256), fichiers dans /tmp, /windows/temp |
| **Système** | Processus suspects, nouvelles clés de registre, comptes créés |
| **Comportemental** | Connexion à 3h du matin, upload massif de données |

### 6.3 SOC (Security Operations Center)

```
Tier 1 (Analyste SOC)  → Triage des alertes, qualification, escalade
Tier 2 (Expert SOC)    → Incident critique, threat hunting, reverse malware
Tier 3 / Red Team      → Pentest proactif, simulation d'attaques APT
SOC Manager            → Gestion équipe, reporting CISO, processus
```

### 6.4 SIEM

Le SIEM est le **cerveau du SOC** : il collecte, normalise, corrèle et alerte sur tous les événements de sécurité.

```
COLLECTE → NORMALISATION → ENRICHISSEMENT → CORRÉLATION → ALERTE
```

**Sources de logs typiques :**
- Pare-feu, IDS/IPS, routeurs/switchs
- Serveurs Windows/Linux, Active Directory
- Serveurs web, bases de données
- Antivirus/EDR, WAF

**Outils SIEM populaires :**

| Solution | Type | Notes |
|---|---|---|
| **Splunk** | Commercial | Leader du marché |
| **IBM QRadar** | Commercial | Très utilisé en entreprise |
| **Microsoft Sentinel** | Cloud (Azure) | Intégration native Microsoft |
| **Elastic SIEM** | Open-source/Commercial | Basé sur ELK Stack |
| **Wazuh** | Open-source | Excellent pour les HIDS |

> 🆕 **Tendance 2024-2025 :** Les **XDR (Extended Detection & Response)** unifient SIEM, EDR, et NDR pour une vision 360° des menaces.

### 6.5 Threat Intelligence

Les flux de Threat Intelligence permettent d'enrichir les SIEM avec des indicateurs de compromission connus :

- **MISP** : plateforme open-source de partage de Threat Intelligence
- **STIX/TAXII** : formats standards d'échange de TI
- **VirusTotal** : analyse de fichiers/URLs malveillants
- **MITRE ATT&CK** : framework de classification des tactiques et techniques d'attaque

---

## 7. Gestion des Risques et Conformité

### 7.1 Formule du Risque

```
Risque = Probabilité × Impact

ou

Risque = Menace × Vulnérabilité × Impact
```

### 7.2 Méthodes d'Évaluation des Risques

| Méthode | Origine | Caractéristiques |
|---|---|---|
| **EBIOS RM** | ANSSI (France) | 5 ateliers, scénarios stratégiques et opérationnels |
| **MEHARI** | CLUSIF (France) | +300 services de sécurité, approche mixte |
| **OCTAVE** | Carnegie Mellon (USA) | Centré sur les actifs critiques, auto-évaluation |
| **ISO 27005** | International | Cadre générique aligné sur ISO 27001 |
| **FAIR** | Open Group | Approche quantitative financière |

### 7.3 Traitements du Risque (4T)

```
TRANSFER  → Assurance cyber, sous-traitance
AVOID     → Ne pas exercer l'activité risquée
MITIGATE  → Mettre en place des contrôles de sécurité
ACCEPT    → Risques résiduels acceptés formellement
```

### 7.4 ISO 27001

La norme internationale de référence pour les **Systèmes de Management de la Sécurité de l'Information (SMSI)**.

**Cycle PDCA :**
```
PLAN  → Évaluation des risques, définition des objectifs
DO    → Mise en œuvre des contrôles de sécurité
CHECK → Audit interne, revue de direction
ACT   → Actions correctives, amélioration continue
```

**Annexe A (version 2022) — 93 mesures en 4 thèmes :**

| Thème | # Mesures | Exemples |
|---|---|---|
| Mesures organisationnelles | 37 | Politiques de sécurité, gestion des actifs |
| Mesures liées aux personnes | 8 | Sensibilisation, formation |
| Mesures physiques | 14 | Contrôle d'accès physique, CCTV |
| Mesures technologiques | 34 | Chiffrement, IDS, journalisation |

### 7.5 NIST Cybersecurity Framework (CSF 2.0)

Les 6 fonctions du NIST CSF 2.0 :

```
GOVERN   → Gouvernance, politiques, rôles (nouveau en v2.0)
IDENTIFY → Inventaire des actifs, évaluation des risques
PROTECT  → Contrôles d'accès, formation, chiffrement
DETECT   → Monitoring, détection d'anomalies
RESPOND  → Plan de réponse, communications
RECOVER  → Restauration, amélioration post-incident
```

### 7.6 Réglementations

#### RGPD (UE)

- En vigueur depuis le **25 mai 2018**
- S'applique à **toutes les organisations** traitant des données de résidents européens
- Sanctions : jusqu'à **20 millions € ou 4% du CA mondial**
- Principes : minimisation des données, droit à l'effacement, privacy by design

#### Loi 09-08 (Maroc)

- Équivalent marocain de la protection des données personnelles
- Supervisée par la **CNDP** (Commission Nationale de contrôle de la protection des Données)
- Promulguée par le Dahir n° 1-09-15 du 18 février 2009
- Applicabilité : tout traitement de données personnelles effectué au Maroc

> 🆕 **Mise à jour :** Le Maroc travaille sur une **refonte de la Loi 09-08** pour l'aligner davantage sur le RGPD et les standards internationaux.

#### Autres référentiels importants

| Référentiel | Secteur | Description |
|---|---|---|
| **PCI-DSS** | Financier / Paiement | Protection des données de cartes bancaires |
| **HIPAA** | Santé (USA) | Protection des données de santé |
| **SOC 2** | Technologie / SaaS | Contrôles sécurité, disponibilité, confidentialité |
| **NIS2** | Infrastructure critique (UE) | Directive européenne cybersécurité 2024 |

### 7.7 Politique de Sécurité de l'Information (PSI)

**Structure type d'une politique de sécurité :**

```
1. Objectif et périmètre
2. Références normatives
3. Définitions
4. Rôles et responsabilités
5. Règles et exigences
6. Non-conformité et sanctions
7. Révision et mise à jour
```

**Liaison entre risques et politiques :**
```
Analyse des risques → Identification des menaces
        ↓
Sélection des contrôles (Annexe A ISO 27001)
        ↓
Rédaction des politiques de sécurité
        ↓
Mise en œuvre et sensibilisation
        ↓
Audit et amélioration continue
```

---

## 8. Ressources et Références

### Organisations et Frameworks

| Ressource | URL | Description |
|---|---|---|
| **OWASP** | https://owasp.org | Sécurité applicative, Top 10 |
| **NIST** | https://csrc.nist.gov | Standards et frameworks US |
| **ANSSI** | https://www.ssi.gouv.fr | Agence française de cybersécurité |
| **MITRE ATT&CK** | https://attack.mitre.org | Tactics & techniques des attaquants |
| **CVE** | https://cve.mitre.org | Base de données de vulnérabilités |
| **CNDP Maroc** | https://www.cndp.ma | Protection des données au Maroc |

### Outils Open-Source Recommandés

| Catégorie | Outil | Usage |
|---|---|---|
| **SIEM** | Wazuh, Elastic SIEM | Surveillance et détection |
| **IDS/IPS** | Snort, Suricata | Détection d'intrusion réseau |
| **Scan réseau** | Nmap, Masscan | Cartographie réseau |
| **Vuln scanning** | OpenVAS, Nuclei | Scan de vulnérabilités |
| **Pentest web** | Burp Suite CE, OWASP ZAP | Test des applications web |
| **Forensics** | Autopsy, Volatility | Analyse forensique |
| **Threat Intel** | MISP | Partage d'indicateurs |
| **Mot de passe** | Hashcat, John the Ripper | Test de robustesse |

### Certifications Cybersécurité

| Niveau | Certification | Domaine |
|---|---|---|
| Débutant | **CompTIA Security+** | Généraliste |
| Intermédiaire | **CEH** (EC-Council) | Ethical Hacking |
| Intermédiaire | **eJPT** (eLearnSecurity) | Pentest |
| Avancé | **OSCP** (Offensive Security) | Pentest avancé |
| Management | **CISSP** (ISC²) | Management sécurité |
| Management | **CISM** (ISACA) | Management sécurité |
| Compliance | **ISO 27001 Lead Auditor** | Audit SMSI |

### Plateformes d'Apprentissage Pratique

- [TryHackMe](https://tryhackme.com) — Apprentissage guidé, idéal débutants
- [HackTheBox](https://hackthebox.com) — Labs avancés, CTF
- [PicoCTF](https://picoctf.org) — CTF éducatif
- [PortSwigger Web Academy](https://portswigger.net/web-security) — Sécurité web (OWASP)
- [Cybrary](https://cybrary.it) — Cours en ligne cybersécurité

---

## 🔄 Mises à Jour

| Date | Version | Changements |
|---|---|---|
| 2025-04 | 1.0 | Création initiale du document |

---

> **📝 Note de l'auteur :** Ce document est maintenu à titre de référence personnelle. La cybersécurité évolue rapidement — certaines informations peuvent devenir obsolètes. Toujours se référer aux sources officielles pour les informations les plus récentes.

---

*Références du cours : Introduction à la Cybersécurité — Document de cours.*  
*Références complémentaires : OWASP, NIST, ANSSI, Mandiant M-Trends 2023, IBM Cost of Data Breach Report 2022.*
