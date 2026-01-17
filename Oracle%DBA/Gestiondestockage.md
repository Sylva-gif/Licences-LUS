# Gestion du Stockage (Tablespaces, Tables & Index)

Ce chapitre traite de la manière dont Oracle gère l'espace de stockage, de la structure logique des tablespaces jusqu'à l'optimisation des performances via les index.

---

## 🏗️ 1. Concepts de Stockage : Logique vs Physique

L'administration Oracle repose sur la séparation entre ce que voit l'utilisateur (logique) et ce qui est écrit sur le disque (physique).

### La Hiérarchie de Stockage
| Niveau | Type | Description |
| :--- | :--- | :--- |
| **Tablespace** | Logique | Conteneur principal regroupant les objets (Tables, Index). |
| **Datafile** | Physique | Fichier réel sur le disque dur (`.dbf`). |
| **Segment** | Logique | Espace alloué à un objet spécifique (ex: une Table entière). |
| **Extent** | Logique | Ensemble de blocs contigus alloués lors de l'extension d'un segment. |
| **Block** | Physique | Plus petite unité (8 Ko par défaut). C'est là que résident les lignes. |

**Schéma de relation :**
`Tablespace` ➡️ `Datafile` ➡️ `Segment` ➡️ `Extent` ➡️ `Block`

---

## 💾 2. Les Tablespaces

### Types de Tablespaces
1.  **SYSTEM** : Créé à l'installation, il contient le dictionnaire de données (obligatoire).
2.  **SYSAUX** : Auxiliaire au système (statistiques, options).
3.  **TEMPORARY** : Dédié aux opérations de tri (`ORDER BY`, `GROUP BY`).
4.  **UNDO** : Gère l'annulation des transactions.
5.  **USER DATA** : Stockage des données utilisateurs et applicatives.

### Gestion de l'espace (Dimensions)
*   **SIZE** : Taille initiale du fichier.
*   **AUTOEXTEND** : Permet au fichier de grandir tout seul si la base manque de place.
*   **MAXSIZE** : La limite de sécurité pour ne pas saturer le disque dur physique.

---

## 📊 3. Tables et Index

### Les Tables
*   **Types de données courants** : `VARCHAR2` (Texte), `NUMBER` (Chiffres), `DATE`.
*   **TRUNCATE vs DROP** : 
    *   `TRUNCATE` : Vide la table et libère l'espace instantanément (très rapide).
    *   `DROP` : Supprime la table et sa structure de la base.

### Les Index
Un index est une structure de données qui accélère les recherches.
*   **Index Simple** : Sur une colonne.
*   **Index Composite** : Sur plusieurs colonnes (ex: Nom + Prénom).
*   **REBUILD** : Action de reconstruire un index pour le "nettoyer" et regagner en performance après beaucoup de modifications.

---

# 🛠️ Centre de Ressources : Lignes de Commande (SQL)

Voici les commandes détaillées pour l'administration quotidienne en milieu professionnel.

## 🚀 A. Gestion des Tablespaces

### Création d'un Tablespace professionnel
```sql
-- Création avec auto-extension pour éviter les pannes de stockage
CREATE TABLESPACE tbs_lus_data
DATAFILE 'C:\oracle\oradata\tbs_lus01.dbf' 
SIZE 100M 
AUTOEXTEND ON NEXT 10M 
MAXSIZE 500M;

-- Ajouter un deuxième fichier pour augmenter la capacité
ALTER TABLESPACE tbs_lus_data 
ADD DATAFILE 'C:\oracle\oradata\tbs_lus02.dbf' 
SIZE 200M;

-- Protéger les données contre les modifications (archivage)
ALTER TABLESPACE tbs_lus_data READ ONLY;

-- Remettre en mode normal (Lecture/Écriture)
ALTER TABLESPACE tbs_lus_data READ WRITE;

-- Mettre hors ligne pour maintenance physique
ALTER TABLESPACE tbs_lus_data OFFLINE;

CREATE TABLE users1.etudiants (
    id_etudiant NUMBER(5) PRIMARY KEY,
    nom VARCHAR2(30) NOT NULL,
    prenom VARCHAR2(30),
    date_naissance DATE
) TABLESPACE tbs_lus_data;
-- Supprimer une colonne et libérer l'espace par paquets de 1000 lignes
ALTER TABLE etudiants 
DROP COLUMN adresse 
CASCADE CONSTRAINTS CHECKPOINT 1000;

-- 1. Voir la liste des tablespaces et leur état
SELECT tablespace_name, status, contents FROM dba_tablespaces;

-- 2. Voir les fichiers physiques et leur taille réelle sur disque
SELECT file_name, tablespace_name, bytes/1024/1024 AS SIZE_MB 
FROM dba_data_files;

-- 3. Vérifier l'espace libre restant par tablespace
SELECT tablespace_name, SUM(bytes)/1024/1024 AS FREE_MB 
FROM dba_free_space 
GROUP BY tablespace_name;
