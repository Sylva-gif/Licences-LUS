# BUSINESS INTELLIGENCE — INFORMATIQUE DÉCISIONNELLE
*Version enrichie : concepts approfondis, certifications professionnelles, chapitre IA & BI*

---

## SOMMAIRE

1. Introduction à l'Informatique Décisionnelle & Concepts Clés (3h)
2. Modélisation Décisionnelle (6h)
3. Le Processus d'Alimentation : l'ETL (6h)
4. Stockage & Requêtage : le Data Warehouse (6h)
5. Restitution, Analyse OLAP & Data Visualisation (6h)
6. **[Chapitre ajouté] Intelligence Artificielle & Business Intelligence** (4h)
7. **[Annexe ajoutée] Certifications professionnelles reconnues**
A. Glossaire général & ressources
B. Corrigés des exercices

**Fil conducteur** : l'analyse des ventes d'une entreprise (produits, clients, régions, temps) illustre chaque notion d'un chapitre à l'autre.

---

# CHAPITRE 1 · Introduction à l'Informatique Décisionnelle & Concepts Clés (3h)

## Objectif
Maîtriser le vocabulaire normalisé, les enjeux stratégiques et les architectures fondamentales d'un Système d'Information Décisionnel.

## Compétences visées
- Définir et expliciter les acronymes majeurs de l'écosystème Data (BI, SID, KPI, ETL, OLAP, OLTP).
- Différencier de manière rigoureuse une base de production (OLTP) d'une base décisionnelle (OLAP).
- Cartographier les flux de données au sein d'une architecture décisionnelle type.

## 1.1 Qu'est-ce que la Business Intelligence ?

La Business Intelligence (informatique décisionnelle) désigne l'ensemble des méthodes, outils et processus qui transforment des données brutes en information exploitable pour éclairer la prise de décision.

Une organisation produit chaque jour d'énormes volumes de données à travers ses applications opérationnelles (ventes, stocks, RH…). Ces données, dispersées et orientées « transaction », ne répondent pas directement aux questions des décideurs : quelles sont mes ventes par région et par trimestre ? quel produit décline ? La BI comble ce fossé en collectant, consolidant et restituant l'information sous une forme analytique.

> **Définition — Business Intelligence**
> Ensemble des méthodes, outils et processus qui collectent, consolident et restituent les données d'une organisation afin d'aider à la décision. La BI ne crée pas la donnée : elle la rend analysable et compréhensible.

**Donnée → Information → Connaissance → Décision**

La donnée est un fait brut (« 42 »). L'information est une donnée mise en contexte (« 42 ventes à Rabat en mai »). La connaissance résulte de l'analyse (« les ventes de Rabat progressent »). La décision en découle (« renforcer le stock à Rabat »).

### Exemples de questions BI
1. Quel est mon chiffre d'affaires par région et par trimestre ?
2. Quels produits sont en déclin sur les 6 derniers mois ?
3. Quel canal de vente recrute les clients les plus fidèles ?

## 1.2 Le Système d'Information Décisionnel & ses enjeux

> **Définition — KPI (indicateur clé de performance)**
> Mesure quantifiable, alignée sur un objectif, qui permet de suivre la performance d'une activité dans le temps. Un bon KPI est chiffrable, comparable à une cible et actionnable. Exemples : chiffre d'affaires mensuel, taux de churn, panier moyen, délai de livraison.

Le SID (Système d'Information Décisionnel) est l'infrastructure dédiée à l'analyse, distincte du système opérationnel. Ses enjeux sont stratégiques :

- **Pilotage** — mesurer la performance via des indicateurs (KPI) fiables et partagés.
- **Réactivité** — détecter tendances et anomalies pour décider vite.
- **Vision unifiée** — offrir une « source unique de vérité » consolidant des sources hétérogènes.
- **Autonomie** — permettre aux métiers d'explorer les données sans passer par l'IT.

## 1.3 Glossaire des acronymes essentiels

| Acronyme | Signification & rôle |
|---|---|
| BI | Business Intelligence — informatique décisionnelle ; l'ensemble de la démarche. |
| SID | Système d'Information Décisionnel — l'infrastructure supportant la BI. |
| KPI | Key Performance Indicator — indicateur clé de performance (ex. CA, taux de churn). |
| ETL | Extract – Transform – Load — le processus d'alimentation de l'entrepôt. |
| DW / DWH | Data Warehouse — entrepôt de données centralisé orienté analyse. |
| OLTP | OnLine Transaction Processing — base de production, orientée transactions. |
| OLAP | OnLine Analytical Processing — analyse multidimensionnelle des données. |

## 1.4 OLTP vs OLAP : deux mondes opposés

Distinguer ces deux familles est fondamental : elles n'ont ni le même but, ni la même structure, ni les mêmes performances attendues.

**OLTP** — OnLine Transaction Processing. Base de production gérant les transactions courantes au fil de l'eau : nombreuses écritures rapides sur peu de lignes. Ex. enregistrer une commande sur un site e-commerce.

**OLAP** — OnLine Analytical Processing. Base décisionnelle optimisée pour l'analyse : lectures massives et agrégations sur l'historique. Ex. calculer le CA par région sur 3 ans.

| Critère | OLTP (production) | OLAP (décisionnel) |
|---|---|---|
| Finalité | Exécuter des transactions | Analyser, décider |
| Opérations | Insert / Update / Delete fréquents | Lectures massives, agrégations |
| Données | Actuelles, détaillées | Historisées, agrégées |
| Modèle | Normalisé (3NF) | Dénormalisé (étoile) |
| Requêtes | Simples, prédéfinies | Complexes, ad hoc |
| Utilisateurs | Nombreux (opérationnels) | Peu (analystes, décideurs) |

## 1.5 Architecture décisionnelle type

Les données suivent un flux depuis les sources opérationnelles jusqu'aux outils de restitution. C'est la « chaîne décisionnelle ».

```
Sources (OLTP, CSV, API) → ETL (extraire, nettoyer) → Data Warehouse (stockage central) → Restitution (OLAP, dataviz)
```

Chaque maillon correspond à un chapitre de ce cours : l'ETL (ch. 3) alimente le Data Warehouse (ch. 4), lui-même modélisé (ch. 2) puis restitué (ch. 5).

> **Définition — Zone de préparation (staging area)**
> Espace de stockage intermédiaire, entre les sources et l'entrepôt, où les données extraites sont déposées telles quelles avant transformation. Il isole les systèmes de production du traitement et permet de rejouer un chargement en cas d'erreur.

## 1.6 Les métiers & acteurs de la BI

| Rôle | Mission principale |
|---|---|
| Data Engineer | Construit et maintient les pipelines ETL et l'infrastructure de données. |
| Data Analyst | Explore les données, construit indicateurs et tableaux de bord. |
| BI Developer | Modélise l'entrepôt et développe les rapports décisionnels. |
| Data Steward | Garant de la qualité et de la gouvernance des données. |
| Décideur / métier | Exprime le besoin et exploite les analyses pour décider. |
| *Analytics Engineer* | *(rôle émergent)* Fait le pont entre Data Engineer et Data Analyst ; modélise les données transformées (souvent avec dbt) pour les rendre directement exploitables en self-service BI. |
| *Data Scientist* | *(rôle connexe)* Va au-delà du reporting descriptif pour construire des modèles prédictifs et du machine learning à partir des données de l'entrepôt. |

## 1.7 Panorama des outils du marché

| Étape | Outils représentatifs |
|---|---|
| Intégration (ETL) | Talend, Informatica, Microsoft SSIS, Apache NiFi. |
| Entrepôt (DW) | PostgreSQL, Oracle, Snowflake, Google BigQuery, Amazon Redshift. |
| Restitution (BI) | Qlik Cloud, Power BI, Tableau, Looker. |

**Dans ce module** : les TP s'appuient sur Talend pour l'intégration et Qlik Cloud pour la restitution — deux outils représentatifs et accessibles gratuitement.

## 1.8 Reporting, analyse & fouille de données

| Niveau | Question type |
|---|---|
| Reporting | Que s'est-il passé ? Restituer des chiffres figés (rapport mensuel de ventes). |
| Analyse (OLAP) | Pourquoi ? Explorer interactivement, croiser les axes, forer le détail. |
| Data mining | Que va-t-il se passer ? Détecter des motifs, prédire (segmentation, scoring). |

**Repères historiques** : Le terme Business Intelligence se popularise dans les années 1990 avec les premiers entrepôts de données. Les années 2010 apportent la self-service BI (Qlik, Tableau, Power BI) puis les entrepôts cloud, rendant l'analyse accessible aux métiers eux-mêmes. Depuis 2023-2024, l'intégration de l'IA générative (copilotes, requêtes en langage naturel) redéfinit encore l'usage de la BI — voir Chapitre 6.

## À retenir — Chapitre 1
- La BI transforme la donnée brute en information d'aide à la décision.
- Un KPI est un indicateur chiffré, comparable à une cible et actionnable.
- OLTP = production (transactions) ; OLAP = décisionnel (analyse historisée).
- La chaîne décisionnelle : Sources → ETL → Data Warehouse → Restitution.

## Exercices
1. Donnez la signification complète des acronymes : BI, SID, KPI, ETL, OLTP, OLAP.
2. Pour chacun des cas suivants, indiquez s'il relève d'OLTP ou d'OLAP : (a) enregistrer un paiement ; (b) calculer le CA annuel par région ; (c) mettre à jour un stock ; (d) analyser l'évolution du churn sur 2 ans.
3. Citez trois questions métier auxquelles un SID peut répondre dans une entreprise de e-commerce.
4. Schématisez la chaîne décisionnelle et placez-y les outils Talend et Qlik.

---

# CHAPITRE 2 · Modélisation Décisionnelle (6h)

## Objectif
Concevoir une architecture de données optimisée pour la vitesse de requêtage et l'analyse multidimensionnelle.

## Compétences visées
- Modéliser un besoin métier sous forme de schéma en Étoile ou en Flocon.
- Structurer les tables de Faits (mesures, granularité) et de Dimensions (axes d'analyse).
- Gérer l'historique des données via les dimensions à variation lente (SCD).

## 2.1 De la modélisation relationnelle à la modélisation dimensionnelle

Là où la modélisation transactionnelle (3NF) cherche à éviter la redondance, la modélisation dimensionnelle privilégie la simplicité de lecture et la performance analytique, quitte à dénormaliser.

On raisonne autour d'une question centrale : « que veut-on mesurer, et selon quels axes ? ». La réponse structure le modèle en deux types de tables complémentaires : les faits (ce que l'on mesure) et les dimensions (les angles d'analyse).

## 2.2 La table de faits

> **Définition — Table de faits**
> Table centrale du schéma qui enregistre les événements mesurables de l'activité. Chaque ligne combine des mesures (valeurs numériques : montant, quantité, durée) et des clés étrangères pointant vers les dimensions qui la contextualisent.

> **Définition — Granularité**
> Niveau de détail représenté par une ligne de faits (ex. « une ligne = une ligne de commande » vs « une ligne = un total journalier »). C'est la décision la plus structurante du modèle : elle fixe la finesse maximale d'analyse possible.

Les mesures se classent selon leur additivité :

### Exemples — types de mesures
1. **Additive**. Le montant d'une vente : sommable sur tous les axes (temps, produit, région).
2. **Semi-additive**. Un stock : sommable par produit mais pas dans le temps (on ne cumule pas les stocks de deux jours).
3. **Non additive**. Un taux de marge (%) : ne se somme jamais, il se recalcule.

## 2.3 Les tables de dimensions

> **Définition — Table de dimension**
> Table décrivant un axe d'analyse (le temps, le produit, le client, la géographie…). Elle regroupe des attributs descriptifs textuels (libellés, catégories) servant à filtrer, grouper et étiqueter les mesures.

> **Définition — Hiérarchie**
> Organisation des attributs d'une dimension en niveaux emboîtés, du plus fin au plus large, permettant le forage (drill-down / roll-up).

### Exemples de dimensions & hiérarchies
1. **Temps**. Jour → Mois → Trimestre → Année.
2. **Produit**. Article → Sous-catégorie → Catégorie → Rayon.
3. **Géographie**. Ville → Région → Pays.

## 2.4 Schéma en étoile vs schéma en flocon

Le schéma en étoile place la table de faits au centre, entourée de dimensions dénormalisées : lisible et rapide. Le flocon normalise les dimensions en sous-tables : moins de redondance, mais des jointures supplémentaires.

```
        Dim_Temps          Dim_Client
        jour·mois·année    nom·segment
              \                /
               \              /
              Faits_Ventes
              montant·quantité
               /              \
              /                \
        Dim_Produit         Dim_Géo
        libellé·catégorie   ville·région
```

*Schéma en étoile : une table de faits centrale reliée à ses dimensions.*

| Critère | Étoile | Flocon |
|---|---|---|
| Dimensions | Dénormalisées | Normalisées |
| Jointures | Peu (rapide) | Nombreuses |
| Lisibilité | Élevée | Plus complexe |
| Redondance | Plus élevée | Réduite |

### Un troisième modèle : le schéma en constellation (galaxie)
Lorsque plusieurs tables de faits partagent des dimensions communes (ex. `Faits_Ventes` et `Faits_Retours` partageant `Dim_Produit` et `Dim_Temps`), on parle de **schéma en constellation** (ou *fact constellation*). C'est le modèle le plus courant dans un vrai Data Warehouse d'entreprise, qui combine plusieurs processus métier autour de dimensions conformées (« conformed dimensions » selon Kimball).

## 2.5 Dimensions à variation lente (SCD)

Les attributs d'une dimension changent parfois (un client déménage). Les Slowly Changing Dimensions définissent comment gérer cet historique :

| Type | Comportement |
|---|---|
| Type 0 | Figé : la valeur d'origine n'est jamais modifiée. |
| Type 1 | Écrasement : on remplace l'ancienne valeur, sans historique. |
| Type 2 | Historisation : on crée une nouvelle ligne (dates de validité / drapeau courant). Le plus courant. |
| Type 3 | Colonne supplémentaire : on conserve « valeur précédente » et « valeur actuelle ». |
| Type 4 | *(complément)* Table d'historique séparée : la dimension principale ne garde que l'état courant, une table miroir conserve tout l'historique — utile pour de gros volumes de changements. |
| Type 6 | *(complément)* Hybride 1+2+3 : combine écrasement, historisation par ligne et colonne « valeur précédente » pour un maximum de flexibilité analytique. |

### Exemple — un client déménage de Rabat à Fès
1. **Type 1**. On écrase « Rabat » par « Fès » : les ventes passées semblent avoir eu lieu à Fès (historique perdu).
2. **Type 2**. On ajoute une nouvelle ligne « Fès » (avec dates de validité) : les ventes d'avant restent liées à Rabat, celles d'après à Fès.
3. **Type 3**. On garde deux colonnes : `ville_actuelle = Fès` et `ville_precedente = Rabat`.

## 2.6 Méthode de conception d'un modèle dimensionnel

La démarche de référence (Kimball) structure la conception en quatre étapes ordonnées :

| Étape | Décision |
|---|---|
| 1 | Choisir le processus métier à analyser (ex. les ventes). |
| 2 | Définir la granularité (ex. une ligne = une ligne de ticket de caisse). |
| 3 | Identifier les dimensions (temps, produit, client, magasin…). |
| 4 | Identifier les mesures (montant, quantité, remise…). |

> **Kimball vs Inmon** : deux écoles de pensée coexistent. **Kimball** (bottom-up) construit l'entrepôt par assemblage de data marts dimensionnels autour de dimensions conformées — approche agile, rapide à livrer. **Inmon** (top-down) construit d'abord un entrepôt central normalisé (3NF), puis en dérive des data marts dimensionnels — approche plus longue mais avec une source unique de vérité plus rigoureuse. La plupart des entreprises modernes adoptent une approche hybride.

## 2.7 Les types de tables de faits

### Exemples — trois natures de faits
1. **Fait de transaction**. Un événement à un instant précis (une vente, un clic). Le plus fin et le plus courant.
2. **Fait de photographie périodique (snapshot)**. Un état relevé à intervalle régulier (le stock chaque fin de journée).
3. **Fait d'accumulation (accumulating)**. Le suivi d'un processus à étapes (commande → préparation → expédition → livraison), mis à jour au fil des jalons.

## 2.8 Cas pratique — Modéliser les ventes

Appliquons la méthode au fil rouge. Besoin : analyser le chiffre d'affaires par produit, client, région et période.

**Résolution guidée**
1. Processus : la vente. Grain : une ligne de facture.
2. Dimensions : `Dim_Temps`, `Dim_Produit`, `Dim_Client`, `Dim_Géo`.
3. Mesures : montant (additive), quantité (additive), taux_remise (non additive).
4. Le modèle obtenu est le schéma en étoile présenté en 2.4.

## À retenir — Chapitre 2
- Le modèle dimensionnel oppose faits (mesures) et dimensions (axes).
- La granularité est la décision la plus structurante du modèle.
- Étoile = dénormalisé et rapide ; flocon = normalisé, moins redondant ; constellation = plusieurs faits, dimensions partagées.
- Les SCD gèrent l'historique des changements de dimensions (Type 2 le plus courant).

## Exercices
1. Une bibliothèque veut analyser ses emprunts de livres. Proposez un schéma en étoile (faits, mesures, dimensions).
2. Pour ce modèle, indiquez la granularité choisie et justifiez-la.
3. Classez ces mesures : nombre d'emprunts, durée moyenne de prêt, stock d'exemplaires disponibles.
4. Le nom d'un adhérent change (mariage). Quel type de SCD préconisez-vous et pourquoi ?

---

# CHAPITRE 3 · Le Processus d'Alimentation : l'ETL (6h)

## Objectif
Construire des pipelines automatisés pour collecter, nettoyer et consolider des sources de données hétérogènes.

## Compétences visées
- Extraire des données de formats multiples (SQL, CSV, API, Excel).
- Appliquer des règles de transformation (nettoyage, dédoublonnage, gestion des types) pour garantir la qualité.
- Gérer l'intégrité référentielle lors du chargement via des clés de substitution.

## 3.1 Le rôle de l'ETL

L'ETL (Extract – Transform – Load) est le pont entre les sources opérationnelles et l'entrepôt. Il collecte, fiabilise et met en forme les données avant leur stockage analytique.

```
Extract (collecter les sources) → Transform (nettoyer, harmoniser) → Load (charger vers le DW)
```

## 3.2 Extract — l'extraction

> **Définition — Extraction**
> L'extraction est l'opération qui consiste à lire et copier les données depuis une ou plusieurs sources vers une zone de travail (souvent une staging area), sans les altérer, afin de les préparer aux transformations. C'est le point de contact entre le monde opérationnel et le monde décisionnel.

Les sources sont hétérogènes par leur format et leur mode d'accès. L'extracteur doit s'adapter à chacune tout en ménageant les systèmes de production : on privilégie une fenêtre de faible activité et, dès que possible, une extraction incrémentale.

> **Extraction complète vs incrémentale**
> L'extraction complète relit l'intégralité de la source à chaque cycle (simple, mais coûteuse). L'extraction incrémentale ne récupère que les données nouvelles ou modifiées depuis le dernier chargement (via une date de modification, un numéro de séquence ou la capture de changements « CDC »).

### Exemples d'extraction
1. **Base SQL (production)**. Récupérer les commandes du jour : `SELECT * FROM commandes WHERE date_maj >= '2026-05-01'` — extraction incrémentale sur la date de mise à jour.
2. **Fichier CSV (partenaire)**. Un fournisseur dépose chaque nuit `ventes_2026-05-12.csv` sur un serveur FTP ; l'ETL lit le fichier du jour.
3. **API REST (service web)**. Interroger `GET /api/clients?modified_since=…` qui renvoie du JSON, page par page.

## 3.3 Transform — la transformation

> **Définition — Transformation**
> La transformation applique aux données extraites un ensemble de règles qui les nettoient, les harmonisent et les enrichissent pour les rendre cohérentes, fiables et conformes au modèle de l'entrepôt. C'est l'étape qui crée l'essentiel de la valeur de l'ETL.

On distingue plusieurs familles de transformations, souvent enchaînées :

### a. Nettoyage des données
Corriger ou écarter les valeurs manquantes, aberrantes ou mal formatées pour éviter les analyses faussées.

**Exemples de nettoyage**
1. Un champ `age = 999` ou négatif : valeur aberrante à corriger ou à rejeter.
2. Une ville vide : remplacée par « Inconnu » ou complétée depuis le code postal.
3. Des espaces parasites et une casse incohérente : `" Rabat "` → normalisé en `"Rabat"`.

### b. Harmonisation des types & formats
Uniformiser dates, nombres et encodages issus de sources différentes vers un format cible unique.

**Exemples d'harmonisation**
1. Dates hétérogènes `12/05/2026` et `2026-05-12` → format ISO unique `AAAA-MM-JJ`.
2. Montant texte `"1 250,50"` → nombre décimal `1250.50` (séparateurs harmonisés).
3. Encodage Latin-1 → UTF-8 pour éviter les caractères corrompus (« Ã© » → « é »).

### c. Dédoublonnage

> **Définition — Dédoublonnage**
> Le dédoublonnage identifie et supprime les enregistrements en double désignant une même entité réelle, selon une ou plusieurs clés de rapprochement, en ne conservant qu'un exemplaire de référence.

**Exemples de dédoublonnage**
1. Deux lignes avec le même email : on ne garde que la plus récente.
2. « Jean Dupont » et « Dupont Jean » avec la même date de naissance : rapprochés comme un seul client.
3. Un même produit importé de deux systèmes sous des codes différents : fusionnés via un référentiel.

### d. Enrichissement & standardisation
Ajouter de l'information (champs calculés, jointures avec des référentiels) et appliquer des règles métier communes.

**Exemples d'enrichissement**
1. Créer `nom_complet = prenom + " " + nom` à partir de deux colonnes.
2. Déduire la région à partir de la ville via une table de correspondance.
3. Standardiser les pays : `"Maroc"`, `"MA"`, `"MAR"` → code ISO unique `MA`.

> **Principe « garbage in, garbage out »**
> Un entrepôt alimenté de données non fiabilisées produira des analyses fausses. La qualité de la restitution dépend directement de la rigueur des transformations.

### e. Illustration — avant / après transformation

**Données brutes extraites (source)**

| prenom | nom | ville | date_insc |
|---|---|---|---|
| anas | HAMDI | rabat | 12/01/2025 |
| Anas | Hamdi | Rabat | 2025-01-12 |
| youssef | ALAOUI | | 2025-05-18 |
| Rania | Benali | Fès | 2026-01-24 |

**Après transformation (cible)**

| nom_complet | ville | date_inscription |
|---|---|---|
| Anas Hamdi | Rabat | 2025-01-12 |
| Youssef Alaoui | Inconnu | 2025-05-18 |
| Rania Benali | Fès | 2026-01-24 |

Les deux lignes « Anas Hamdi » en double sont fusionnées ; la casse et les espaces sont normalisés ; les dates sont mises au format ISO ; la ville vide est remplacée ; `nom_complet` est calculé.

## 3.4 Load — le chargement

> **Définition — Chargement**
> Le chargement insère les données transformées dans les tables cibles de l'entrepôt (dimensions puis faits), en préservant l'intégrité référentielle : aucune ligne de faits ne doit référencer une dimension inexistante.

L'ordre est donc essentiel : on charge d'abord les dimensions (pour disposer de leurs clés), puis les faits. Comme pour l'extraction, le chargement peut être complet (on vide et recharge) ou incrémental (on ajoute/met à jour les nouveautés — approche « upsert »).

> **Définition — Intégrité référentielle**
> Règle garantissant que toute clé étrangère d'une table de faits pointe vers une ligne réellement existante dans la table de dimension correspondante. Elle empêche les « faits orphelins » et fiabilise les jointures d'analyse.

> **Définition — Clé de substitution (surrogate key)**
> Clé technique interne, sans signification métier (un simple compteur), générée pour chaque ligne de dimension. On l'utilise à la place de la clé métier de la source, susceptible de changer ou d'entrer en collision entre systèmes. Elle assure la stabilité des liens et rend possible l'historisation SCD de type 2.

**Exemples de chargement**
1. **Ordre respecté**. Charger `Dim_Client` avant `Faits_Ventes` pour que chaque vente trouve son `client_sk`.
2. **Upsert incrémental**. Un client existant est mis à jour, un nouveau client est inséré (sans tout recharger).
3. **Clé de substitution**. Le client métier `CLI-0042` devient `client_sk = 178` dans la dimension ; les faits référencent 178.

## 3.5 ETL ou ELT ?

> **Définition — ELT**
> Variante où l'on inverse les deux dernières étapes : on charge d'abord les données brutes dans l'entrepôt (Load), puis on les transforme sur place (Transform) en exploitant sa puissance de calcul.

Avec la montée en puissance des entrepôts cloud, l'ELT s'est répandu. L'ETL classique reste privilégié quand la transformation est lourde, sensible ou soumise à une gouvernance stricte (la donnée est nettoyée avant d'entrer dans l'entrepôt).

| Critère | ETL | ELT |
|---|---|---|
| Transformation | Avant le chargement | Dans l'entrepôt |
| Lieu de calcul | Serveur ETL dédié | Moteur du DW |
| Adapté à | Règles complexes, gouvernance | Gros volumes, cloud |

> **Complément : l'outil dbt (data build tool)** s'est imposé comme standard de la couche « T » de l'ELT moderne : il permet de versionner les transformations SQL dans le DW comme du code (tests, documentation, dépendances), en s'intégrant à des entrepôts cloud comme Snowflake, BigQuery ou Redshift.

## 3.6 Architecture d'un flux ETL

Un flux industriel ne va pas directement de la source à l'entrepôt : il traverse des zones successives qui isolent et fiabilisent le traitement.

```
Sources (systèmes métier) → Staging (données brutes) → ODS (nettoyées) → Data Warehouse (modélisées)
```

> **Définition — ODS (Operational Data Store)**
> Zone intermédiaire contenant des données intégrées et nettoyées mais encore proches du détail opérationnel, avant leur modélisation dimensionnelle dans l'entrepôt. Elle sert de tampon et de point de consolidation.

## 3.7 La qualité des données

La qualité se mesure selon plusieurs dimensions. Un bon ETL les surveille activement.

| Dimension | Question posée |
|---|---|
| Complétude | Les valeurs obligatoires sont-elles toutes renseignées ? |
| Exactitude | Les valeurs reflètent-elles la réalité ? |
| Cohérence | Les données concordent-elles entre les sources ? |
| Unicité | Chaque entité n'est-elle présente qu'une fois ? |
| Validité | Les valeurs respectent-elles le format et les règles attendus ? |
| Fraîcheur | Les données sont-elles suffisamment à jour ? |

**Exemples de contrôles qualité**
1. **Complétude**. Rejeter toute ligne sans email vers un fichier d'erreurs.
2. **Validité**. Vérifier qu'une date d'inscription n'est pas dans le futur.
3. **Cohérence**. Contrôler que `date_derniere_connexion ≥ date_inscription`.

## 3.8 Orchestration & planification

> **Définition — Job & orchestration**
> Un job est un traitement ETL exécutable. L'orchestration enchaîne plusieurs jobs selon un ordre et des conditions (dépendances, planification, reprise sur erreur), le plus souvent la nuit lors d'une fenêtre de faible activité.

**Exemples d'orchestration**
1. Planifier le flux chaque nuit à 2h (traitement « batch »).
2. N'exécuter le chargement des faits qu'après le succès du chargement des dimensions.
3. Envoyer une alerte e-mail si un job échoue.

> **Outils d'orchestration modernes** : Apache Airflow, Dagster et Prefect sont aujourd'hui les standards pour orchestrer des pipelines complexes en Python, avec gestion fine des dépendances, retries et monitoring visuel — au-delà des simples tâches planifiées (cron) historiques.

## 3.9 Gestion des erreurs & bonnes pratiques
- **Journalisation** — tracer volumes lus/écrits/rejetés à chaque exécution.
- **Rejets isolés** — dérouter les lignes invalides sans bloquer tout le flux.
- **Idempotence** — pouvoir relancer un flux sans créer de doublons.
- **Reprise** — repartir de la staging plutôt que de re-solliciter la source.
- **Paramétrage** — externaliser chemins et connexions (pas de valeurs en dur).

## 3.10 Panorama des outils ETL

| Outil | Positionnement |
|---|---|
| Talend | Composants visuels, riche connectivité ; utilisé dans les TP. |
| Informatica | Solution d'entreprise historique, très complète. |
| Microsoft SSIS | Intégré à l'écosystème SQL Server. |
| Apache NiFi | Flux de données temps réel, open source. |
| *dbt* | *(complément)* Transformation SQL versionnée pour l'approche ELT moderne. |
| *Fivetran / Airbyte* | *(complément)* Connecteurs managés pour l'extraction (E) « clé en main » vers le cloud. |

## 3.11 Cas pratique — consolider des contacts

Fil rouge du TP 02 : quatre fichiers (CSV, Excel, XML, JSON) décrivant les mêmes contacts doivent être unifiés.

**Résolution guidée**
1. **Extract** : un composant de lecture par format, tous ramenés à 6 champs communs.
2. **Transform** : regrouper les flux, dédoublonner sur `email`, créer `nom_complet`.
3. **Load** : écrire un CSV, un TXT et un CSV téléversé sur Google Drive.

## À retenir — Chapitre 3
- L'ETL = Extract (collecter) → Transform (fiabiliser) → Load (charger).
- La transformation crée l'essentiel de la valeur : nettoyage, harmonisation, dédoublonnage, enrichissement.
- Les clés de substitution et l'ordre dimensions-puis-faits garantissent l'intégrité référentielle.
- Un flux robuste s'appuie sur des zones (staging, ODS), des contrôles qualité et une orchestration.

## Exercices
1. Citez les trois étapes de l'ETL et donnez un exemple concret pour chacune.
2. Différenciez extraction complète et incrémentale ; donnez un cas d'usage de chaque.
3. Proposez trois contrôles qualité pour un fichier clients (nom, email, date de naissance).
4. Pourquoi charge-t-on les dimensions avant les faits ? Que risque-t-on sinon ?
5. Expliquez l'intérêt d'une clé de substitution par rapport à la clé métier.

---

# CHAPITRE 4 · Stockage & Requêtage : le Data Warehouse (6h)

## Objectif
Déployer physiquement l'entrepôt sur un SGBD et l'interroger de manière performante à l'aide du SQL analytique.

## Compétences visées
- Générer les scripts DDL de création physique de la base décisionnelle.
- Rédiger des requêtes analytiques avec les fonctions de fenêtrage (OVER, PARTITION BY, RANK) et les agrégations avancées (CUBE, ROLLUP).
- Optimiser le temps d'exécution des requêtes.

## 4.1 Déploiement physique de l'entrepôt

Le modèle logique (ch. 2) est traduit en objets physiques sur un SGBD : tables, colonnes typées, clés et contraintes, à l'aide du langage de définition de données (DDL).

## 4.2 Génération du DDL

Exemple de création d'une dimension et d'une table de faits avec clés de substitution :

```sql
CREATE TABLE Dim_Produit (
  produit_sk INT PRIMARY KEY,       -- clé de substitution
  produit_id VARCHAR(20),           -- clé métier source
  libelle VARCHAR(120),
  categorie VARCHAR(60)
);

CREATE TABLE Faits_Ventes (
  temps_sk INT REFERENCES Dim_Temps(temps_sk),
  produit_sk INT REFERENCES Dim_Produit(produit_sk),
  client_sk INT REFERENCES Dim_Client(client_sk),
  montant DECIMAL(12,2),
  quantite INT
);
```

## 4.3 SQL analytique : les fonctions de fenêtrage

Les fonctions de fenêtrage calculent une valeur sur un groupe de lignes lié à la ligne courante, sans réduire le résultat (contrairement à `GROUP BY`). Elles sont indispensables aux classements et cumuls.

```sql
-- Classer les produits par CA au sein de chaque catégorie
SELECT categorie, libelle, ca,
       RANK() OVER (PARTITION BY categorie ORDER BY ca DESC) AS rang
FROM ventes_par_produit;
```

La clause `OVER` définit la fenêtre ; `PARTITION BY` la découpe en groupes ; `ORDER BY` l'ordonne.

**Exemples de fonctions de fenêtrage**
1. **Classement**. `RANK() OVER (ORDER BY ca DESC)` — classer les vendeurs par CA.
2. **Cumul**. `SUM(ca) OVER (ORDER BY mois)` — chiffre d'affaires cumulé mois après mois.
3. **Comparaison**. `LAG(ca) OVER (ORDER BY mois)` — récupérer le CA du mois précédent pour calculer la variation.

## 4.4 Agrégations avancées : ROLLUP, CUBE, GROUPING SETS

Ces extensions de `GROUP BY` produisent plusieurs niveaux de sous-totaux en une seule requête — parfait pour les rapports multidimensionnels.

```sql
-- Sous-totaux par région, puis par région+produit, plus le total général
SELECT region, produit, SUM(montant) AS ca
FROM Faits_Ventes JOIN Dim_Geo USING(geo_sk)
GROUP BY ROLLUP (region, produit);
```

- **ROLLUP** — sous-totaux hiérarchiques (région, puis total).
- **CUBE** — toutes les combinaisons possibles de sous-totaux.
- **GROUPING SETS** — un contrôle fin des regroupements souhaités.

## 4.5 Optimisation des performances

- **Index** — notamment sur les clés étrangères de la table de faits.
- **Partitionnement** — découper une grande table de faits (souvent par date) pour ne lire que le nécessaire.
- **Vues matérialisées / agrégats** — précalculer les résultats fréquents.
- **Analyse du plan d'exécution** — repérer les opérations coûteuses.

```sql
-- Index sur une clé étrangère fréquemment jointe
CREATE INDEX idx_faits_produit ON Faits_Ventes(produit_sk);

-- Partitionner la table de faits par année
CREATE TABLE Faits_Ventes (...)
PARTITION BY RANGE (temps_sk);

-- Vue matérialisée : CA mensuel précalculé
CREATE MATERIALIZED VIEW mv_ca_mensuel AS
SELECT t.annee, t.mois, SUM(f.montant) AS ca
FROM Faits_Ventes f JOIN Dim_Temps t USING(temps_sk)
GROUP BY t.annee, t.mois;
```

> **Définition — Vue matérialisée**
> Requête dont le résultat est stocké physiquement et rafraîchi périodiquement. Contrairement à une vue classique (recalculée à chaque appel), elle accélère fortement les rapports récurrents au prix d'un léger décalage de fraîcheur.

> **Bonne pratique** : Dans un entrepôt, on optimise pour la lecture : la dénormalisation, les index et les agrégats précalculés priment sur l'économie d'espace.

## 4.6 Data Warehouse, Data Mart & Data Lake

Ces trois notions coexistent souvent ; il faut les distinguer.

> **Définition — Data Warehouse**
> Entrepôt centralisé et modélisé regroupant les données décisionnelles de toute l'organisation, historisées et structurées pour l'analyse.

> **Définition — Data Mart**
> Sous-ensemble de l'entrepôt dédié à un domaine métier (ex. le marketing) ou à un service, plus petit et plus ciblé, pour des analyses spécifiques.

> **Définition — Data Lake**
> Réservoir stockant des données brutes de tout type (structurées ou non : logs, images, texte) sans modélisation préalable, exploitées plus tard selon les besoins (souvent en data science).

| Critère | Data Warehouse | Data Lake |
|---|---|---|
| Données | Structurées, modélisées | Brutes, tout format |
| Schéma | À l'écriture | À la lecture |
| Usage | BI, reporting | Data science, exploration |

> **Complément — Data Lakehouse** : architecture hybride récente (ex. Databricks, Delta Lake, Apache Iceberg) qui combine la souplesse de stockage brut d'un Data Lake avec les garanties transactionnelles et le schéma structuré d'un Data Warehouse, permettant de faire du reporting BI ET du machine learning sur une même plateforme de données.

## 4.7 Cas pratique — Top 3 produits par région

Combinons fenêtrage et jointures sur le fil rouge des ventes.

```sql
-- Les 3 meilleurs produits (par CA) dans chaque région
WITH ventes AS (
  SELECT g.region, p.libelle,
         SUM(f.montant) AS ca
  FROM Faits_Ventes f
  JOIN Dim_Geo g USING(geo_sk)
  JOIN Dim_Produit p USING(produit_sk)
  GROUP BY g.region, p.libelle
)
SELECT region, libelle, ca
FROM (
  SELECT region, libelle, ca,
         RANK() OVER (PARTITION BY region ORDER BY ca DESC) AS rg
  FROM ventes
) t
WHERE rg <= 3;
```

## À retenir — Chapitre 4
- Le DDL matérialise physiquement le modèle (tables, clés, contraintes).
- Les fonctions de fenêtrage (OVER, PARTITION BY, RANK, LAG) calculent sans réduire les lignes.
- ROLLUP / CUBE produisent des sous-totaux multi-niveaux en une requête.
- On optimise par index, partitionnement et agrégats ; on distingue DW, Data Mart, Data Lake et Lakehouse.

## Exercices
1. Écrivez le DDL d'une table `Dim_Temps` (clé de substitution, date, mois, année).
2. Rédigez une requête donnant le CA cumulé mois par mois sur 2025.
3. Quelle différence entre `GROUP BY` et une fonction `OVER` ? Illustrez.
4. Un Data Lake peut-il remplacer un Data Warehouse ? Argumentez.

---

# CHAPITRE 5 · Restitution, Analyse OLAP & Data Visualisation (6h)

## Objectif
Créer des tableaux de bord interactifs professionnels permettant aux décideurs de naviguer intuitivement dans les données.

## Compétences visées
- Sélectionner le bon type de représentation graphique (sémiologie graphique) selon le message métier.
- Développer un modèle sémantique et des mesures dynamiques (ex. langage DAX sous Power BI).
- Scénariser l'information (Data Storytelling) en respectant les règles de l'UI/UX et la navigation OLAP.

## 5.1 L'analyse OLAP & ses opérations

L'analyse OLAP considère les données comme un cube multidimensionnel que l'utilisateur explore de façon interactive selon plusieurs axes.

| Opération | Description |
|---|---|
| Drill-down | Descendre dans le détail d'une hiérarchie (Année → Trimestre → Mois). |
| Roll-up | Remonter vers un niveau agrégé (Mois → Année). |
| Slice | Isoler une « tranche » du cube en fixant une dimension (ex. année = 2025). |
| Dice | Extraire un sous-cube en filtrant plusieurs dimensions à la fois. |
| Pivot | Faire pivoter les axes pour changer la perspective d'analyse. |

> **Définition — Cube OLAP**
> Représentation des données selon plusieurs dimensions simultanées (ex. produit × temps × région), chaque cellule contenant une mesure agrégée. L'utilisateur « navigue » dans ce cube pour explorer l'information sous différents angles.

### Exemple — un décideur explore les ventes
1. Il part du CA national 2025, puis fait un drill-down pour voir le détail par région.
2. Il applique un slice sur « Région = Rabat » pour isoler ce marché.
3. Il fait un pivot pour croiser cette fois produits × trimestres.

## 5.2 Modèle sémantique & mesures (DAX)

> **Définition — Mesure (modèle sémantique)**
> Calcul dynamique défini une fois dans le modèle et recalculé automatiquement selon le contexte de filtre du visuel (période, région sélectionnée…). À distinguer d'une colonne calculée, figée ligne par ligne.

Avant de visualiser, on construit un modèle sémantique : relations entre tables, hiérarchies et surtout mesures. Sous Power BI, on les exprime en DAX (Data Analysis Expressions).

```dax
-- Chiffre d'affaires total
CA = SUM(Faits_Ventes[montant])

-- Croissance vs année précédente
Croissance % =
VAR ca_n1 = CALCULATE([CA], SAMEPERIODLASTYEAR(Dim_Temps[date]))
RETURN DIVIDE([CA] - ca_n1, ca_n1)
```

## 5.3 Sémiologie graphique : choisir la bonne représentation

Chaque type de graphique répond à un message précis. Un mauvais choix trompe le lecteur.

| Message à transmettre | Graphique adapté |
|---|---|
| Comparer des catégories | Barres / colonnes |
| Évolution dans le temps | Courbe (ligne) |
| Répartition d'un tout | Camembert (peu de parts) / barres empilées |
| Corrélation entre 2 mesures | Nuage de points |
| Valeur unique à suivre | Carte KPI / jauge |
| Données géographiques | Carte (map) |

## 5.4 Data Storytelling & UI/UX du tableau de bord

Un tableau de bord n'est pas une collection de graphiques : c'est un récit guidant le décideur du général au particulier.

- **Hiérarchie visuelle** — KPI clés en haut, détail plus bas.
- **Sobriété** — éliminer le superflu (« data-ink ratio »), une idée par visuel.
- **Cohérence** — mêmes couleurs pour les mêmes concepts, légendes claires.
- **Interactivité** — filtres et forage (drill-down) pour l'exploration autonome.
- **Contexte** — comparaisons, objectifs et variations plutôt que valeurs isolées.

## 5.5 Les types de tableaux de bord

Selon l'audience et l'horizon de décision, on distingue trois familles de tableaux de bord.

| Type | Rôle & audience |
|---|---|
| Stratégique | Vue synthétique long terme pour la direction (KPI globaux, objectifs). |
| Tactique | Suivi des processus par les managers (comparaisons, tendances). |
| Opérationnel | Pilotage au quotidien, souvent en temps réel (alertes, détail). |

## 5.6 Erreurs de visualisation à éviter

**Exemples de pièges courants**
1. **Camembert surchargé**. Trop de parts illisibles : préférer un diagramme à barres.
2. **Axe tronqué**. Un axe qui ne part pas de zéro exagère les écarts et trompe le lecteur.
3. **Excès de couleurs / 3D**. Décorations inutiles qui nuisent à la lecture du message.

> **Règle d'or** : Chaque visuel doit répondre à une seule question. Si le lecteur hésite sur le message, le graphique est à revoir.

## 5.7 Panorama des outils de restitution

| Outil | Points forts |
|---|---|
| Qlik Cloud | Moteur associatif, exploration libre ; utilisé dans les TP. |
| Power BI | Langage DAX, intégration Microsoft, large diffusion. |
| Tableau | Réputé pour la richesse et l'esthétique des visualisations. |
| Looker | Modélisation centralisée (LookML), orienté cloud. |

## 5.8 Méthode — Concevoir un tableau de bord

Une démarche en cinq temps évite le « mur de graphiques » et produit un support réellement décisionnel.

1. **Cadrer**. Qui est l'audience ? Quelles décisions doit-elle prendre ? Quelles questions clés ?
2. **Choisir les KPI**. 3 à 5 indicateurs essentiels, chacun avec sa cible et sa période de référence.
3. **Structurer**. KPI en haut, tendances au centre, détail en bas ; regrouper par thème.
4. **Choisir les visuels**. Un graphique par message, en respectant la sémiologie graphique.
5. **Rendre interactif**. Filtres, forage (drill-down), infobulles pour l'exploration autonome.

### Exemple — Tableau de bord « Suivi des ventes »
1. **KPI** : CA total, croissance vs N-1, panier moyen.
2. **Tendance** : courbe du CA sur 12 mois.
3. **Répartition** : barres du CA par région ; top 5 produits.
4. **Filtres** : année, région, catégorie de produit.

## À retenir — Chapitre 5
- L'analyse OLAP explore un cube via drill-down, roll-up, slice, dice, pivot.
- Une mesure (DAX) est un calcul dynamique sensible au contexte de filtre.
- La sémiologie graphique associe chaque message au bon type de graphique.
- Un tableau de bord est un récit : hiérarchie visuelle, sobriété, interactivité.

## Exercices
1. Définissez et illustrez les opérations drill-down, slice et pivot.
2. Pour chaque besoin, choisissez le graphique : évolution du CA sur 12 mois ; répartition des ventes par canal ; corrélation prix/quantité.
3. Citez trois erreurs de visualisation et proposez une correction pour chacune.
4. Écrivez une mesure (pseudo-DAX) calculant la part d'un produit dans le CA total.

---

# CHAPITRE 6 · Intelligence Artificielle & Business Intelligence (4h)
### *(Chapitre ajouté — complément au module original)*

## Objectif
Comprendre comment l'IA (machine learning, IA générative) transforme aujourd'hui chaque maillon de la chaîne décisionnelle, et savoir situer les nouveaux usages par rapport aux fondamentaux BI vus dans les chapitres 1 à 5.

## Compétences visées
- Distinguer BI descriptive, BI prédictive et BI générative.
- Identifier où l'IA s'insère dans la chaîne décisionnelle (ETL, DW, restitution).
- Utiliser un copilote IA (langage naturel → requête / visuel) de façon critique.
- Comprendre les enjeux de gouvernance des données à l'ère de l'IA (qualité, biais, confidentialité).

## 6.1 De la BI descriptive à la BI augmentée

Le chapitre 1 distinguait Reporting (« que s'est-il passé ? »), Analyse OLAP (« pourquoi ? ») et Data mining (« que va-t-il se passer ? »). L'IA ajoute un quatrième niveau :

| Niveau | Question type | Technologie |
|---|---|---|
| Reporting | Que s'est-il passé ? | SQL, tableaux de bord statiques |
| Analyse (OLAP) | Pourquoi ? | Cubes, drill-down, DAX |
| BI prédictive | Que va-t-il se passer ? | Machine learning (régression, séries temporelles, scoring) |
| **BI générative / augmentée** | **Que devrais-je faire, et pourquoi, en langage naturel ?** | **LLM (Large Language Models), copilotes IA, NL2SQL** |

> **Définition — BI augmentée (Augmented Analytics)**
> Utilisation de l'intelligence artificielle (machine learning, traitement du langage naturel) pour automatiser la préparation des données, générer automatiquement des insights, et permettre l'interrogation des données en langage naturel plutôt qu'en SQL ou DAX.

## 6.2 L'IA à chaque étape de la chaîne décisionnelle

L'IA ne remplace pas la chaîne Sources → ETL → DW → Restitution vue au chapitre 1 : elle vient l'augmenter à chaque étape.

```
Sources → ETL (IA : nettoyage auto, mapping intelligent)
       → Data Warehouse (IA : détection d'anomalies, catalogage automatique)
       → Restitution (IA : NL2SQL, copilotes, génération auto d'insights)
```

### a. IA dans l'ETL
- **Nettoyage intelligent** : détection automatique d'outliers et de formats incohérents par des modèles de machine learning, au-delà des règles écrites manuellement (§3.3).
- **Mapping de schéma assisté** : suggestion automatique de correspondances entre champs sources et cibles lors de l'intégration de nouvelles sources.
- **Déduplication probabiliste** : au-delà du dédoublonnage par clé exacte (§3.3.c), des modèles de similarité (fuzzy matching, embeddings) rapprochent « Jean Dupont » et « J. Dupont » même sans clé commune explicite.

### b. IA dans le Data Warehouse
- **Détection d'anomalies** : identification automatique de valeurs ou tendances suspectes dans les faits (ex. un pic de vente anormal) sans règle prédéfinie.
- **Catalogage & gouvernance automatisés** : classification automatique des données sensibles (PII) pour appliquer les bonnes politiques de sécurité.

### c. IA dans la restitution — le cœur des nouveaux usages
- **NL2SQL (Natural Language to SQL)** : traduire une question en langage naturel (« quel est le CA par région ce trimestre ? ») en requête SQL exécutable sur l'entrepôt.
- **Copilotes intégrés aux outils BI** : Copilot pour Power BI, Tableau Pulse / Tableau Agent, Qlik Answers — génèrent automatiquement des résumés de tableaux de bord, suggèrent des visuels, répondent à des questions en langage naturel sur les données déjà modélisées.
- **Génération automatique d'insights** : les outils repèrent seuls les variations significatives (« les ventes en région Sud ont baissé de 12% ce mois, principalement dû au produit X ») sans que l'analyste ait posé la question.
- **Data Storytelling automatisé** : génération de commentaires en langage naturel accompagnant un graphique pour en expliquer le message (complément au §5.4).

## 6.3 Pourquoi la modélisation dimensionnelle reste indispensable

Point clé à retenir : **plus l'IA est utilisée en restitution, plus la qualité du modèle dimensionnel (chapitre 2) et de l'ETL (chapitre 3) devient critique.** Un copilote NL2SQL ne peut traduire correctement une question en langage naturel que si :
- les dimensions et mesures sont clairement nommées et documentées (un modèle sémantique propre, cf. §5.2) ;
- la granularité (§2.2) est explicite et cohérente ;
- les données sont fiables (garbage in, garbage out reste vrai — l'IA amplifie une mauvaise donnée au lieu de la corriger).

> **À retenir** : l'IA ne dispense pas de la rigueur de modélisation Kimball. Elle en dépend directement — un modèle sémantique bien structuré est le prérequis d'un copilote BI fiable.

## 6.4 Machine learning & data mining appliqués à la BI

Pour aller au-delà de la simple restitution, quelques familles de modèles fréquemment couplées à un entrepôt de données :

| Cas d'usage | Type de modèle | Exemple |
|---|---|---|
| Prévision des ventes | Séries temporelles (ARIMA, Prophet, régression) | Prévoir le CA du trimestre prochain par région |
| Scoring / classification | Régression logistique, arbres de décision, gradient boosting | Prédire le risque de churn d'un client |
| Segmentation client | Clustering (k-means) | Regrouper les clients par comportement d'achat |
| Détection d'anomalies | Isolation forest, modèles statistiques | Repérer une fraude ou une erreur de saisie |
| Recommandation | Filtrage collaboratif | Suggérer des produits complémentaires |

Ces modèles s'appuient typiquement sur les mêmes tables de faits et dimensions que la BI classique — un signe de plus que la modélisation dimensionnelle (chapitre 2) sert autant la BI descriptive que la data science.

## 6.5 Gouvernance, qualité des données et IA responsable

L'introduction de l'IA dans la chaîne décisionnelle soulève des enjeux qui prolongent le chapitre 3 (qualité des données) :

- **Biais des données** : un modèle entraîné sur des données historiques biaisées reproduit ce biais dans ses prédictions ou recommandations.
- **Explicabilité** : contrairement à une mesure DAX transparente, un modèle de machine learning peut être une « boîte noire » — importance des approches d'IA explicable (XAI) en contexte décisionnel.
- **Confidentialité & sécurité** : les copilotes IA connectés à l'entrepôt doivent respecter les mêmes règles d'accès (RLS, sensibilité des données) que les outils BI classiques.
- **Hallucination en NL2SQL** : un copilote peut générer une requête SQL syntaxiquement correcte mais sémantiquement fausse (mauvaise jointure, mauvaise agrégation) — la validation humaine reste nécessaire, en particulier pour les décisions à enjeu.

## 6.6 Panorama des outils IA appliqués à la BI (2026)

| Catégorie | Outils représentatifs |
|---|---|
| Copilotes BI intégrés | Microsoft Copilot pour Power BI / Fabric, Tableau Agent, Qlik Answers |
| Plateformes ML pour la donnée d'entreprise | Azure Machine Learning, Google Vertex AI, Amazon SageMaker |
| NL2SQL / agents de requêtage | Vanna AI, Text2SQL open source, agents construits sur des LLM (Claude, GPT) |
| Automatisation ETL assistée par IA | Data pipelines avec suggestions ML (Talend, Fivetran, dbt + IA) |

## À retenir — Chapitre 6
- L'IA augmente chaque étape de la chaîne décisionnelle sans la remplacer.
- La BI générative (NL2SQL, copilotes) dépend directement d'un modèle dimensionnel propre et bien documenté.
- Le machine learning (prévision, scoring, segmentation) s'appuie sur les mêmes faits et dimensions que la BI classique.
- La gouvernance des données (qualité, sécurité, biais) devient encore plus critique avec l'IA.

## Exercices
1. Expliquez pourquoi un copilote NL2SQL a besoin d'un modèle sémantique bien nommé pour fonctionner correctement.
2. Proposez un cas d'usage de machine learning s'appuyant sur le modèle `Faits_Ventes` du fil rouge (ventes) développé au chapitre 2.
3. Citez deux risques spécifiques à l'utilisation de copilotes IA dans un outil de BI, et une mesure de mitigation pour chacun.
4. Différenciez BI prédictive et BI générative avec un exemple concret pour chaque.

---

# ANNEXE A · Glossaire général & ressources

## A.1 Glossaire général

| Terme | Définition |
|---|---|
| BI | Business Intelligence : démarche de transformation des données en aide à la décision. |
| SID | Système d'Information Décisionnel : infrastructure supportant la BI. |
| KPI | Indicateur clé de performance, chiffré et aligné sur un objectif. |
| OLTP | Base de production orientée transactions. |
| OLAP | Analyse multidimensionnelle des données historisées. |
| ETL / ELT | Processus d'alimentation : Extract, Transform, Load (ou l'inverse pour ELT). |
| Staging | Zone de dépôt des données brutes extraites. |
| ODS | Operational Data Store : zone de données nettoyées intermédiaires. |
| Data Warehouse | Entrepôt central modélisé pour l'analyse. |
| Data Mart | Sous-ensemble métier de l'entrepôt. |
| Data Lake | Réservoir de données brutes, tout format. |
| Data Lakehouse | Architecture hybride combinant Data Lake et Data Warehouse. |
| Table de faits | Table centrale des mesures et clés de dimensions. |
| Dimension | Axe d'analyse descriptif (temps, produit, client…). |
| Granularité | Niveau de détail d'une ligne de faits. |
| Schéma en étoile | Faits au centre, dimensions dénormalisées autour. |
| Schéma en flocon | Dimensions normalisées en sous-tables. |
| Schéma en constellation | Plusieurs tables de faits partageant des dimensions conformées. |
| SCD | Slowly Changing Dimension : gestion de l'historique des dimensions. |
| Clé de substitution | Clé technique interne remplaçant la clé métier. |
| Fenêtrage | Calcul SQL sur un groupe de lignes lié à la ligne courante (OVER). |
| Cube OLAP | Représentation multidimensionnelle des mesures. |
| DAX | Langage de formules de Power BI pour les mesures dynamiques. |
| NL2SQL | Traduction automatique d'une question en langage naturel vers une requête SQL. |
| Augmented Analytics | BI augmentée par l'IA : automatisation de la préparation et de la génération d'insights. |
| dbt | Outil de transformation SQL versionnée, standard de la couche T en ELT moderne. |

## A.2 Corrigés des exercices

**Chapitre 1**
1. BI : Business Intelligence · SID : Système d'Information Décisionnel · KPI : Key Performance Indicator · ETL : Extract-Transform-Load · OLTP : OnLine Transaction Processing · OLAP : OnLine Analytical Processing.
2. (a) OLTP · (b) OLAP · (c) OLTP · (d) OLAP.
3. Ex. : CA par région et trimestre ; produits en déclin ; canaux recrutant les clients les plus fidèles.
4. Sources → ETL (Talend) → Data Warehouse → Restitution (Qlik).

**Chapitre 2**
1. `Faits_Emprunts` (clés vers `Dim_Temps`, `Dim_Livre`, `Dim_Adhérent`) ; mesures : nb_emprunts, durée.
2. Grain conseillé : une ligne = un emprunt, pour toute analyse fine.
3. Nombre d'emprunts : additive · durée moyenne : non additive · stock disponible : semi-additive.
4. SCD Type 2 si l'on veut conserver l'historique du nom ; Type 1 sinon.

**Chapitre 3**
1. Extract (lire un CSV), Transform (dédoublonner sur email), Load (insérer dans le DW).
2. Complète : tout relire (petit volume). Incrémentale : ne lire que les nouveautés via date de maj (gros volume).
3. Ex. : email non vide (complétude) ; format email valide (validité) ; date de naissance passée (exactitude).
4. Pour respecter l'intégrité référentielle : sinon un fait pourrait référencer une dimension inexistante (fait orphelin).
5. La clé de substitution est stable et neutre ; la clé métier peut changer ou entrer en collision entre systèmes.

**Chapitre 4**
1. `CREATE TABLE Dim_Temps (temps_sk INT PRIMARY KEY, date DATE, mois INT, annee INT);`
2. `SUM(ca) OVER (ORDER BY mois)` filtré sur l'année 2025.
3. `GROUP BY` réduit les lignes en agrégats ; `OVER` calcule sans les réduire (chaque ligne conservée).
4. Non : le Data Lake stocke le brut sans modélisation ; il complète le DW mais ne le remplace pas pour le reporting structuré.

**Chapitre 5**
1. Drill-down : descendre dans le détail ; slice : fixer une dimension ; pivot : intervertir les axes.
2. Évolution : courbe · répartition par canal : barres (ou camembert si peu de parts) · corrélation : nuage de points.
3. Ex. : camembert surchargé → barres ; axe tronqué → axe à zéro ; excès de 3D → visuel plat.
4. `Part % = DIVIDE([CA produit], [CA total])`.

**Chapitre 6**
1. Un copilote NL2SQL fait correspondre les mots de la question aux noms des tables/colonnes/mesures : si le modèle est mal nommé ou non documenté, la traduction en SQL sera erronée ou impossible.
2. Ex. : prévision du CA par région pour le trimestre suivant (série temporelle) à partir de `Faits_Ventes` × `Dim_Temps` × `Dim_Géo`.
3. Ex. : hallucination de requête (mitigation : validation humaine systématique des requêtes générées) ; fuite de données sensibles (mitigation : appliquer les mêmes règles RLS/sécurité au copilote qu'aux outils BI classiques).
4. BI prédictive : « quel sera le CA du mois prochain ? » (modèle statistique) ; BI générative : « explique-moi pourquoi le CA a baissé en région Sud » en langage naturel, avec réponse et visuel générés automatiquement.

---

# ANNEXE B · Certifications professionnelles reconnues

Ces certifications permettent de valider et faire reconnaître les compétences développées dans ce cours, chapitre par chapitre.

## B.1 Certifications généralistes BI / Data Analyst

| Certification | Éditeur | Lien officiel |
|---|---|---|
| Microsoft Certified: Power BI Data Analyst Associate (PL-300) | Microsoft | https://learn.microsoft.com/fr-fr/credentials/certifications/data-analyst-associate/ |
| Tableau Certified Data Analyst | Salesforce/Tableau | https://www.tableau.com/learn/certification/data-analyst |
| Tableau Certified Consultant | Salesforce/Tableau | https://www.tableau.com/learn/certification |
| Qlik Certified Data Analyst — Qlik Sense | Qlik | https://www.qlik.com/us/services/training/certification |
| Google Data Analytics Professional Certificate | Google (Coursera) | https://www.coursera.org/professional-certificates/google-data-analytics |
| IBM Data Analyst Professional Certificate | IBM (Coursera) | https://www.coursera.org/professional-certificates/ibm-data-analyst |

## B.2 Certifications Data Engineering / ETL / Data Warehouse

| Certification | Éditeur | Lien officiel |
|---|---|---|
| Microsoft Certified: Fabric Data Engineer Associate (DP-700) | Microsoft | https://learn.microsoft.com/fr-fr/credentials/certifications/fabric-data-engineer-associate/ |
| Microsoft Certified: Azure Data Engineer Associate (DP-203 / successeur) | Microsoft | https://learn.microsoft.com/fr-fr/credentials/certifications/azure-data-engineer/ |
| Google Cloud Professional Data Engineer | Google Cloud | https://cloud.google.com/learn/certification/data-engineer |
| AWS Certified Data Engineer – Associate | Amazon Web Services | https://aws.amazon.com/fr/certification/certified-data-engineer-associate/ |
| SnowPro Core Certification | Snowflake | https://www.snowflake.com/en/certifications/ |
| Talend Certification (Data Integration) | Qlik (ex-Talend) | https://www.qlik.com/us/services/training/certification |
| dbt Analytics Engineering Certification | dbt Labs | https://www.getdbt.com/certifications |

## B.3 Certifications SQL & bases de données

| Certification | Éditeur | Lien officiel |
|---|---|---|
| Oracle Database SQL Certified Associate | Oracle | https://education.oracle.com/database-sql-certified-associate/trackp_333 |
| Microsoft Certified: Azure Database Administrator Associate (DP-300) | Microsoft | https://learn.microsoft.com/fr-fr/credentials/certifications/azure-database-administrator-associate/ |
| PostgreSQL Certified Professional (EDB) | EnterpriseDB | https://www.enterprisedb.com/education/certification |

## B.4 Certifications IA appliquée aux données / Machine Learning

| Certification | Éditeur | Lien officiel |
|---|---|---|
| Microsoft Certified: Azure AI Engineer Associate (AI-102) | Microsoft | https://learn.microsoft.com/fr-fr/credentials/certifications/azure-ai-engineer/ |
| Microsoft Certified: Azure Data Scientist Associate (DP-100) | Microsoft | https://learn.microsoft.com/fr-fr/credentials/certifications/azure-data-scientist/ |
| Google Cloud Professional Machine Learning Engineer | Google Cloud | https://cloud.google.com/learn/certification/machine-learning-engineer |
| AWS Certified Machine Learning – Specialty | Amazon Web Services | https://aws.amazon.com/fr/certification/certified-machine-learning-specialty/ |
| IBM AI Engineering Professional Certificate | IBM (Coursera) | https://www.coursera.org/professional-certificates/ai-engineer |
| DeepLearning.AI — Generative AI for Data Analysis | DeepLearning.AI (Coursera) | https://www.coursera.org/learn/generative-ai-for-data-analysis |

> 1. **PL-300** (Power BI Data Analyst) — validation directe des chapitres 4 et 5 de ce cours, forte reconnaissance sur le marché francophone africain et international.
> 2. **SnowPro Core** ou **DP-700 (Fabric Data Engineer)** — valorise les chapitres 3 et 4 (ETL, Data Warehouse cloud), pertinent pour les rôles visés (CNIN, ASIN) où l'infrastructure data est de plus en plus cloud-native.
> 3. **DP-100 (Azure Data Scientist)** — pont naturel vers le chapitre 6 (IA & BI), complémentaire du profil cybersécurité/data science déjà engagé à l'ENSA.

*Note : les tarifs, formats d'examen et prérequis évoluent régulièrement — toujours vérifier les informations à jour sur le site officiel de l'éditeur avant inscription.*

---

# SYNTHÈSE DU COURS

La chaîne décisionnelle boucle ici : les données modélisées (ch. 2), alimentées par l'ETL (ch. 3) et stockées dans l'entrepôt (ch. 4) deviennent enfin des décisions grâce à une restitution soignée (ch. 5), aujourd'hui augmentée par l'intelligence artificielle (ch. 6). La maîtrise de ces fondamentaux, validée par des certifications reconnues (annexe B), constitue une base solide pour toute carrière en informatique décisionnelle, du Data Analyst au Data Engineer en passant par le BI Developer.

---
