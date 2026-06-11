# 🗄️ Guide Complet SQL — De Zéro à Maître
---

## 📑 Table des Matières

1. [Définitions Fondamentales](#1-définitions-fondamentales)
2. [Les 5 Catégories de Commandes SQL](#2-les-5-catégories-de-commandes-sql)
3. [DDL — Data Definition Language](#3-ddl--data-definition-language)
4. [DML — Data Manipulation Language](#4-dml--data-manipulation-language)
5. [DQL — Data Query Language](#5-dql--data-query-language)
6. [Tableau Récapitulatif Global](#6-tableau-récapitulatif-global)
7. [Ressources en Ligne pour Approfondir](#7-ressources-en-ligne-pour-approfondir)
8. [SQL × Intelligence Artificielle](#8-sql--intelligence-artificielle)

---

## 1. Définitions Fondamentales

### 🔷 Base de Données (BD)
Ensemble **structuré** de données reliées logiquement, accessibles par ordinateur pour satisfaire plusieurs utilisateurs simultanément.

**Buts :**
- Capitaliser les données pour répondre à un besoin spécifique
- Faciliter la gestion des données
- Offrir une vue claire d'une multitude de données liées

### 🔷 Schéma d'une base de données
Description d'une BD obtenue par un modèle de données. Il regroupe : tables, index, vues, contraintes, procédures.

```
Propriétaire du schéma
    ├── tables
    │     ├── vues
    │     └── contraintes
    ├── index
    └── procédures
```

### 🔷 SGBD — Système de Gestion de Base de Données
Logiciel qui assure :
1. **Accès aux fichiers** : intégrité, concurrence, optimisation
2. **Interactions** : langages d'interrogation et de manipulation

> SQL combine les deux approches : **déclarative** (logique mathématique) et **procédurale** (théorie des ensembles)

---

## 2. Les 5 Catégories de Commandes SQL

| Catégorie | Nom complet | Rôle | Commandes |
|-----------|-------------|------|-----------|
| **DDL** | Data Definition Language | Structurer | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| **DML** | Data Manipulation Language | Modifier les données | `INSERT`, `UPDATE`, `DELETE` |
| **DQL** | Data Query Language | Lire/Interroger | `SELECT` |
| **TCL** | Transaction Control Language | Gérer les transactions | `COMMIT`, `ROLLBACK` |
| **DCL** | Data Control Language | Contrôler les accès | `GRANT`, `REVOKE` |

---

## 3. DDL — Data Definition Language

### 3.1 Types de données

#### Numériques
| Type | Description | Taille | Exemple |
|------|-------------|--------|---------|
| `INT` | Entier standard | 4 octets | `15600890` |
| `TINYINT` | Très petit entier | 1 octet | `25` (âge) |
| `SMALLINT` | Petit entier | 2 octets | `1250` (nb pages) |
| `BIGINT` | Très grand entier | 8 octets | `9223372036854775807` |
| `DECIMAL` | Décimal exact | Variable | `19.99` (prix) |
| `FLOAT` | Virgule flottante | 4 octets | `37.5` (température) |
| `DOUBLE` | Virgule double précision | 8 octets | `0.00000000000123` |

#### Chaînes de caractères
| Type | Description | Exemple |
|------|-------------|---------|
| `CHAR(n)` | Taille fixe | Code pays `'MA'` |
| `VARCHAR(n)` | Taille variable | Nom `'Badr ZEROUAL'` |
| `TEXT` | Texte standard | Description produit |
| `LONGTEXT` | Texte quasi illimité | Archive, logs |
| `ENUM` | Liste de choix fixes | `('S','M','L','XL')` |

#### Temporels
| Type | Description | Exemple |
|------|-------------|---------|
| `DATE` | Jour uniquement | `'2026-03-15'` |
| `TIME` | Heure uniquement | `'14:30:00'` |
| `DATETIME` | Jour + Heure | `'2026-03-15 08:30:00'` |
| `TIMESTAMP` | Jour + Heure (UTC) | Date de création compte |
| `YEAR` | Année uniquement | `2026` |

#### Binaires (BLOB)
| Type | Taille max | Usage |
|------|------------|-------|
| `BLOB` | 64 Ko | Photo de profil |
| `LONGBLOB` | 4 Go | Vidéo, PDF |

#### Types Spéciaux
| Type | Usage | Exemple |
|------|-------|---------|
| `JSON` | Données structurées | `{"color":"blue","size":"XL"}` |
| `GEOMETRY` | Cartographie | `POINT(48.8584 2.2945)` |
| `BIT(n)` | Valeurs binaires | `0` ou `1` |

#### ⚠️ NULL — L'absence de donnée
- `NULL` ≠ `0` (zéro est une valeur numérique)
- `NULL` ≠ `""` (la chaîne vide est un texte)
- `NULL` = **valeur inconnue ou non renseignée**

---

### 3.2 Créer une base de données

```sql
CREATE DATABASE nom_de_la_base;
USE nom_de_la_base;
```

---

### 3.3 Conventions de nommage

| Règle | ✅ Correct | ❌ Incorrect |
|-------|-----------|------------|
| **Snake_case** | `date_naissance` | `DateNaissance`, `date naissance` |
| **Singulier** | `utilisateur` | `utilisateurs` |
| **Pas de mots réservés** | `id_client` | `SELECT`, `TABLE` |
| **Pas d'accents** | `prenom`, `ca_annuel` | `prénom`, `ca-annuel` |
| **Préfixer les clés** | `id_client`, `id_commande` | `id` (ambigu) |

> **Astuce backticks :** Si vous *devez* utiliser un mot réservé, entourez-le de backticks `` `select` `` (mauvaise pratique à éviter)

---

### 3.4 Créer une table (CREATE TABLE)

```sql
CREATE TABLE eleves (
    id_eleve INT PRIMARY KEY AUTO_INCREMENT,
    nom      VARCHAR(50) NOT NULL,
    prenom   VARCHAR(50),
    email    VARCHAR(100) UNIQUE,
    age      TINYINT,
    date_naissance DATE
);
```

**Règles de la Clé Primaire (PRIMARY KEY) :**
- Ne peut jamais être vide (`NOT NULL`)
- Ne peut jamais avoir deux fois la même valeur

**AUTO_INCREMENT :** SQL ajoute automatiquement +1 à chaque nouvel enregistrement.

**UNIQUE :** Empêche les doublons (email, téléphone…) — plusieurs colonnes `UNIQUE` possibles par table.

---

### 3.5 Modifier une table (ALTER TABLE)

```sql
-- Ajouter une colonne
ALTER TABLE eleves ADD date_naissance DATE;

-- Supprimer une colonne
ALTER TABLE eleves DROP COLUMN date_naissance;

-- Modifier le type d'une colonne
ALTER TABLE eleves MODIFY COLUMN nom VARCHAR(100);

-- Renommer une colonne
ALTER TABLE eleves RENAME COLUMN nom TO nom_famille;
```

---

### 3.6 Supprimer définitivement (DROP)

```sql
-- Supprimer une table (irréversible !)
DROP TABLE eleves;

-- Supprimer toute la base
DROP DATABASE ecole_numerique;
```

> ⚠️ **DROP est irréversible.** Toujours vérifier deux fois avant d'exécuter.

---

## 4. DML — Data Manipulation Language

### Le concept CRUD

| Opération | SQL | Description |
|-----------|-----|-------------|
| **C**reate | `INSERT` | Ajouter |
| **R**ead | `SELECT` | Lire (DQL) |
| **U**pdate | `UPDATE` | Modifier |
| **D**elete | `DELETE` | Supprimer |

---

### 4.1 Ajouter des données (INSERT INTO)

```sql
-- Insertion simple
INSERT INTO utilisateur (pseudo, email, mot_de_passe, date_inscription)
VALUES ('Alice', 'alice@mail.com', '12345', '2026-03-15');

-- Insertion multi-lignes (plus performant)
INSERT INTO utilisateur (pseudo, email, mot_de_passe, date_inscription)
VALUES ('Bob',     'bob@mail.com',     'azerty', '2026-03-15'),
       ('Charlie', 'charlie@mail.com', 'qwerty', '2026-03-16'),
       ('Damien',  'damien@mail.com',  'pypass', '2026-03-17');
```

**Points clés :**
- Textes et dates entre guillemets simples `' '`
- Ne pas mentionner la colonne `AUTO_INCREMENT`
- L'ordre des valeurs doit correspondre à l'ordre des colonnes

---

### 4.2 Modifier des données (UPDATE)

```sql
UPDATE utilisateur
SET email = 'alice.new@mail.com', est_premium = b'1'
WHERE id_utilisateur = 1;
```

> ⚠️ **Règle d'or :** Ne jamais faire un `UPDATE` sans `WHERE` — sinon TOUTE la table est modifiée.

---

### 4.3 Supprimer des données (DELETE vs TRUNCATE)

```sql
-- Supprimer une ligne spécifique
DELETE FROM utilisateur WHERE id_utilisateur = 3;

-- Vider toute la table (rapide)
TRUNCATE TABLE utilisateur;
```

| | `DELETE` | `TRUNCATE` |
|-|----------|------------|
| Filtre `WHERE` | ✅ Oui | ❌ Non |
| Réinitialise auto-increment | ❌ Non | ✅ Oui |
| Vitesse | Plus lent | Très rapide |

---

## 5. DQL — Data Query Language

### 5.1 Sélection de base (SELECT … FROM)

```sql
-- Tout afficher
SELECT * FROM produit;

-- Colonnes ciblées (recommandé)
SELECT nom_produit, prix_ht FROM produit;
```

---

### 5.2 Alias (AS)

```sql
-- Renommer une colonne à l'affichage
SELECT nom_produit AS 'Nom de l\'article', prix_ht AS 'Prix'
FROM produit;

-- Colonne calculée à la volée
SELECT nom_produit, (prix_ht * 1.20) AS 'Prix TTC'
FROM produit;
```

---

### 5.3 Filtrage avec WHERE

```sql
-- Opérateurs de comparaison : =  <>  !=  >  <  >=  <=
SELECT * FROM produit WHERE prix_ht > 100;

-- Opérateurs logiques : AND, OR, NOT
SELECT * FROM produit WHERE prix_ht > 100 AND etat = 'Neuf';
SELECT * FROM produit WHERE etat = 'Occasion' OR etat = 'Reconditionné';
```

---

### 5.4 Recherche textuelle (LIKE)

```sql
-- % : n'importe quel nombre de caractères
SELECT * FROM produit WHERE nom_produit LIKE 'Sam%';   -- commence par Sam
SELECT * FROM produit WHERE nom_produit LIKE '%phone%'; -- contient phone

-- _ : exactement un caractère
SELECT * FROM produit WHERE code LIKE 'A_B';
```

---

### 5.5 Intervalles et listes

```sql
-- BETWEEN : plage de valeurs
SELECT * FROM produit WHERE prix_ht BETWEEN 50 AND 150;

-- IN : liste de valeurs précises
SELECT * FROM produit WHERE ville_livraison IN ('Paris', 'Lyon', 'Marseille');
```

---

### 5.6 Valeurs NULL

```sql
-- Trouver les lignes sans description
SELECT * FROM produit WHERE description IS NULL;

-- Trouver les lignes avec description
SELECT * FROM produit WHERE description IS NOT NULL;
```

---

### 5.7 Tri des résultats (ORDER BY)

```sql
-- Décroissant (du plus cher au moins cher)
SELECT nom_produit, prix_ht FROM produit ORDER BY prix_ht DESC;

-- Croissant (par défaut)
SELECT nom_produit, prix_ht FROM produit ORDER BY prix_ht ASC;
```

---

### 5.8 Limiter les résultats (LIMIT)

```sql
-- Le produit le moins cher
SELECT * FROM produit ORDER BY prix_ht ASC LIMIT 1;

-- Top 10
SELECT * FROM produit ORDER BY prix_ht DESC LIMIT 10;

-- Pagination : 10 résultats à partir de la ligne 20
SELECT * FROM produit LIMIT 10 OFFSET 20;
```

---

### 5.9 Fonctions d'agrégation

```sql
-- COUNT : nombre de lignes
SELECT COUNT(*) AS 'Nombre total de produits' FROM produit;

-- SUM : somme totale
SELECT SUM(quantite_stock) FROM produit;

-- AVG, MIN, MAX
SELECT
    AVG(prix_ht) AS 'Moyenne des prix',
    MAX(prix_ht) AS 'Prix max',
    MIN(prix_ht) AS 'Prix min'
FROM produit;
```

---

### 5.10 Groupement (GROUP BY + HAVING)

```sql
-- Nombre de produits par catégorie
SELECT categorie, COUNT(*) AS nb_produits
FROM produit
GROUP BY categorie;

-- Filtrer les groupes (HAVING = WHERE pour les agrégats)
SELECT categorie, AVG(prix_ht) AS prix_moyen
FROM produit
GROUP BY categorie
HAVING AVG(prix_ht) > 100;
```

---

### 5.11 Jointures (JOINs)

```sql
-- INNER JOIN : lignes correspondantes des deux tables
SELECT c.nom_client, co.date_commande
FROM client c
INNER JOIN commande co ON c.id_client = co.id_client;

-- LEFT JOIN : toutes les lignes de gauche + correspondances
SELECT c.nom_client, co.date_commande
FROM client c
LEFT JOIN commande co ON c.id_client = co.id_client;
```

---

## 6. Tableau Récapitulatif Global

| Catégorie | Signification | Action | Commandes | Cible |
|-----------|---------------|--------|-----------|-------|
| **DDL** | Définition | Structurer | `CREATE`, `ALTER`, `DROP` | Objets (Tables) |
| **DML** | Manipulation | Modifier | `INSERT`, `UPDATE`, `DELETE` | Lignes (Données) |
| **DQL** | Query | Lire | `SELECT` | Information |
| **TCL** | Transaction | Contrôler | `COMMIT`, `ROLLBACK` | Transactions |
| **DCL** | Contrôle | Sécuriser | `GRANT`, `REVOKE` | Permissions |

---

## 7. Ressources en Ligne pour Approfondir

### 📚 Cours & Tutoriels Gratuits

| Ressource | Lien | Type | Langue |
|-----------|------|------|--------|
| **W3Schools SQL** | https://www.w3schools.com/sql/ | Tutoriel interactif | EN |
| **SQLZoo** | https://sqlzoo.net/ | Exercices en ligne | EN |
| **Mode Analytics SQL Tutorial** | https://mode.com/sql-tutorial/ | Guide complet | EN |
| **SQL.sh** | https://sql.sh/ | Référence complète | 🇫🇷 FR |
| **Grafikart - SQL** | https://grafikart.fr/formations/sql | Vidéos formation | 🇫🇷 FR |
| **Khan Academy SQL** | https://www.khanacademy.org/computing/computer-programming/sql | Cours interactif | EN |
| **The Odin Project** | https://www.theodinproject.com/paths/full-stack-javascript/courses/databases | Parcours complet | EN |

---

### 🎓 Certifications Reconnues

| Certification | Organisme | Lien | Niveau |
|---------------|-----------|------|--------|
| **Oracle Database SQL** | Oracle | https://education.oracle.com | Intermédiaire |
| **Microsoft DP-900** | Microsoft Azure | https://learn.microsoft.com/certifications/azure-data-fundamentals/ | Débutant |
| **IBM Data Analyst** | IBM / Coursera | https://www.coursera.org/professional-certificates/ibm-data-analyst | Débutant |
| **Google Data Analytics** | Google / Coursera | https://www.coursera.org/professional-certificates/google-data-analytics | Débutant |
| **DataCamp SQL Associate** | DataCamp | https://www.datacamp.com/certification | Intermédiaire |
| **HackerRank SQL** | HackerRank | https://www.hackerrank.com/skills-verification/sql_basic | Débutant → Avancé |

---

### 🛠️ Outils pour Pratiquer SQL

| Outil | Lien | Description |
|-------|------|-------------|
| **DB Fiddle** | https://www.db-fiddle.com/ | SQL en ligne, sans installation |
| **SQLite Online** | https://sqliteonline.com/ | Tester SQL dans le navigateur |
| **MySQL Workbench** | https://dev.mysql.com/downloads/workbench/ | IDE officiel MySQL |
| **DBeaver** | https://dbeaver.io/ | Client universel multi-SGBD |
| **pgAdmin** | https://www.pgadmin.org/ | Interface PostgreSQL |
| **TablePlus** | https://tableplus.com/ | Interface moderne multi-SGBD |

---

### 📺 Chaînes YouTube Recommandées

| Chaîne | Lien | Langue |
|--------|------|--------|
| **Bro Code** | https://www.youtube.com/@BroCodez | EN |
| **Alex the Analyst** | https://www.youtube.com/@AlexTheAnalyst | EN |
| **Grafikart** | https://www.youtube.com/@grafikart | 🇫🇷 FR |
| **Tuto.com** | https://www.youtube.com/@tutocom | 🇫🇷 FR |

---

### 📖 Livres de Référence

- **Learning SQL** — Alan Beaulieu (O'Reilly) — https://www.oreilly.com/library/view/learning-sql-3rd/9781492057604/
- **SQL Cookbook** — Anthony Molinaro (O'Reilly)
- **SQL Performance Explained** — Markus Winand — https://use-the-index-luke.com/ *(gratuit en ligne)*

---

## 8. SQL × Intelligence Artificielle

### 🤖 Comment SQL et l'IA se combinent

L'IA ne remplace pas SQL — elle l'**amplifie**. Voici les grandes synergies :

---

### 8.1 Text-to-SQL : Écrire du SQL en langage naturel

Des outils d'IA traduisent vos questions en requêtes SQL automatiquement.

| Outil | Lien | Description |
|-------|------|-------------|
| **ChatGPT / Claude** | https://claude.ai | Générer et déboguer des requêtes SQL |
| **SQLAI.ai** | https://www.sqlai.ai/ | Génération SQL par IA dédiée |
| **Outerbase** | https://www.outerbase.com/ | Interface IA pour bases de données |
| **Vanna AI** | https://vanna.ai/ | Text-to-SQL open source |
| **AI2SQL** | https://www.ai2sql.io/ | Convertisseur langage naturel → SQL |
| **Defog** | https://defog.ai/ | Text-to-SQL pour entreprises |

**Exemple d'usage avec Claude :**
```
Prompt : "Donne-moi une requête SQL pour trouver les 5 clients 
         qui ont dépensé le plus au cours des 30 derniers jours"

→ Claude génère la requête SQL optimisée instantanément
```

---

### 8.2 SQL dans les pipelines de Machine Learning

```python
# Exemple : Extraire des données d'entraînement avec SQL + Python
import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://user:pass@localhost/ma_base')

# Requête SQL pour préparer les données ML
query = """
    SELECT age, salaire, niveau_education, score_credit
    FROM client
    WHERE date_inscription > '2023-01-01'
      AND score_credit IS NOT NULL
"""

df = pd.read_sql(query, engine)

# Les données sont prêtes pour scikit-learn, TensorFlow, etc.
from sklearn.model_selection import train_test_split
X_train, X_test = train_test_split(df, test_size=0.2)
```

---

### 8.3 Outils qui combinent SQL + IA (No-Code / Low-Code)

| Outil | Lien | Usage |
|-------|------|-------|
| **Databricks** | https://www.databricks.com/ | SQL + ML + IA sur données massives |
| **BigQuery ML** | https://cloud.google.com/bigquery-ml | Entraîner des modèles ML directement en SQL |
| **MindsDB** | https://mindsdb.com/ | Faire des prédictions IA avec des requêtes SQL |
| **Snowflake Cortex** | https://www.snowflake.com/en/data-cloud/cortex/ | LLM directement dans Snowflake |
| **Amazon Redshift ML** | https://aws.amazon.com/redshift/features/redshift-ml/ | ML via SQL sur AWS |
| **Mode Analytics** | https://mode.com/ | Analyse de données SQL + visualisation IA |

---

### 8.4 MindsDB — Faire de l'IA directement en SQL

MindsDB permet d'appeler des modèles d'IA **comme si c'étaient des tables SQL** :

```sql
-- Créer un modèle de prédiction directement en SQL
CREATE MODEL prediction_ventes
FROM ma_base (SELECT * FROM ventes)
PREDICT montant_futur;

-- Utiliser le modèle comme une requête SELECT normale
SELECT montant_futur
FROM prediction_ventes
WHERE mois = '2026-07' AND categorie = 'Electronique';
```

---

### 8.5 BigQuery ML — ML en SQL pur (Google Cloud)

```sql
-- Créer un modèle de régression logistique en SQL
CREATE OR REPLACE MODEL `mon_projet.mon_modele`
OPTIONS(model_type='logistic_reg') AS
SELECT
  IF(montant_achat > 1000, 1, 0) AS label,
  age,
  nb_commandes,
  score_satisfaction
FROM `mon_projet.clients`;

-- Faire des prédictions
SELECT *
FROM ML.PREDICT(MODEL `mon_projet.mon_modele`,
  (SELECT age, nb_commandes, score_satisfaction FROM `mon_projet.nouveaux_clients`));
```

---

### 8.6 Utiliser l'IA pour apprendre SQL plus vite

| Stratégie | Exemple de prompt |
|-----------|-------------------|
| **Générer des exercices** | *"Crée-moi 5 exercices SQL de niveau intermédiaire sur les jointures"* |
| **Déboguer une requête** | *"Pourquoi cette requête ne retourne rien ? [coller le SQL]"* |
| **Optimiser** | *"Comment optimiser cette requête SQL qui prend 30 secondes ?"* |
| **Expliquer** | *"Explique-moi INNER JOIN vs LEFT JOIN avec un exemple concret"* |
| **Convertir** | *"Convertis cette requête MySQL en PostgreSQL"* |

---

### 8.7 Ressources SQL × IA

| Ressource | Lien | Description |
|-----------|------|-------------|
| **MindsDB Docs** | https://docs.mindsdb.com/ | IA directement en SQL |
| **BigQuery ML Guide** | https://cloud.google.com/bigquery-ml/docs | ML avec SQL sur Google Cloud |
| **Coursera - SQL for Data Science** | https://www.coursera.org/learn/sql-for-data-science | SQL orienté data science |
| **Fast.ai - Data Foundations** | https://www.fast.ai/ | Bases données + IA pratique |
| **Kaggle Learn SQL** | https://www.kaggle.com/learn/advanced-sql | SQL avancé pour la data science |
| **Towards Data Science** | https://towardsdatascience.com/tagged/sql | Articles SQL + ML/IA |

---

## ✅ Checklist de Révision SQL

- [ ] Je connais la différence entre BD, Schéma et SGBD
- [ ] Je maîtrise les 5 catégories SQL (DDL, DML, DQL, TCL, DCL)
- [ ] Je sais choisir le bon type de données (INT, VARCHAR, DATE…)
- [ ] Je comprends NULL et ses pièges
- [ ] Je sais créer, modifier et supprimer une table
- [ ] Je maîtrise INSERT, UPDATE, DELETE avec WHERE
- [ ] Je sais écrire un SELECT avec filtres, tri, limite
- [ ] Je connais les fonctions d'agrégation (COUNT, SUM, AVG, MIN, MAX)
- [ ] Je comprends GROUP BY et HAVING
- [ ] Je maîtrise les jointures (INNER JOIN, LEFT JOIN)
- [ ] Je suis capable d'utiliser l'IA pour générer et optimiser mes requêtes SQL

---
