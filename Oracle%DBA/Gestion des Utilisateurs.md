#  Gestion des Utilisateurs et Sécurité

Ce chapitre détaille l'administration des accès, la sécurité des données et la gestion des schémas sous Oracle Database 21c.

---

## 🏗️ 1. Concepts de Sécurité et Schémas

### Utilisateur vs Schéma
*   **Utilisateur** : Compte permettant de se connecter (Identifiant/Mot de passe).
*   **Schéma** : Ensemble d'objets (Tables, Index, Vues, Séquences) appartenant à un utilisateur. 
    *   *Note DBA :* Dans Oracle, l'utilisateur et le schéma sont créés simultanément.

### Domaines de Sécurité
L'administration d'un utilisateur repose sur plusieurs piliers :
1.  **Mécanisme d'authentification** (Base de données ou OS).
2.  **Quotas de tablespace** (Limite d'espace disque).
3.  **Statut du compte** (Ouvert, Verrouillé, Expiré).
4.  **Privilèges et Rôles** (Droits d'action).

---

## 🔑 2. Les Privilèges (Système et Objet)

### A. Privilèges Système
Ils permettent de réaliser des actions générales dans la base de données.
*   `CREATE SESSION` : Droit de se connecter.
*   `CREATE TABLE` : Droit de créer des tables dans son propre schéma.
*   `CREATE ANY TABLE` : Droit de créer des tables dans n'importe quel schéma (Très puissant).
*   **Option ADMIN (`WITH ADMIN OPTION`)** : Permet à l'utilisateur de transmettre ce privilège à d'autres.

### B. Privilèges Objet
Ils permettent d'accéder à des données spécifiques appartenant à un autre utilisateur.
*   `SELECT`, `INSERT`, `UPDATE`, `DELETE` sur une table précise.
*   `EXECUTE` sur une procédure ou un package.
*   **Option GRANT (`WITH GRANT OPTION`)** : Permet au bénéficiaire de transmettre le droit sur cet objet.

---

## 👥 3. Les Rôles
Un rôle est un conteneur de privilèges utilisé pour simplifier la gestion des droits.
*   **Rôles prédéfinis** : 
    *   `CONNECT` : Accès de base.
    *   `RESOURCE` : Création d'objets.
    *   `DBA` : Tous les privilèges d'administration.

---

# 🛠️ Centre de Ressources : Lignes de Commande (SQL)

## 🚀 A. Gestion des Comptes Utilisateurs

### Création d'un utilisateur (Authentification par la base)
```sql
CREATE USER user_lus_2026
IDENTIFIED BY "P@ssword123"
DEFAULT TABLESPACE users_tbs
TEMPORARY TABLESPACE temp
QUOTA 20M ON users_tbs
PASSWORD EXPIRE; -- Force le changement au premier login
-- Augmenter un quota
ALTER USER user_lus_2026 QUOTA 100M ON users_tbs;

-- Verrouiller ou déverrouiller un compte
ALTER USER user_lus_2026 ACCOUNT LOCK;   -- Verrouillage
ALTER USER user_lus_2026 ACCOUNT UNLOCK; -- Déverrouillage

-- Accorder le droit de connexion et création
GRANT CREATE SESSION, CREATE TABLE TO user_lus_2026;

-- Accorder avec possibilité de re-donner le droit
GRANT CREATE TABLE TO user_lus_2026 WITH ADMIN OPTION;

-- Révoquer un privilège
REVOKE CREATE TABLE FROM user_lus_2026;

-- Accorder la lecture sur une table spécifique (Ex: Table EMPLOYES de User_A)
GRANT SELECT ON user_a.employes TO user_lus_2026;

-- Accorder la modification avec droit de transfert
GRANT UPDATE ON user_a.employes TO user_lus_2026 WITH GRANT OPTION;
-- 1. Liste des utilisateurs et état de leur compte
SELECT username, account_status, expiry_date FROM dba_users;

-- 2. Vérifier les quotas de stockage par utilisateur
SELECT tablespace_name, username, bytes/1024/1024 AS Used_MB, max_bytes/1024/1024 AS Max_MB 
FROM dba_ts_quotas;

-- 3. Voir les privilèges système d'un utilisateur précis
SELECT * FROM dba_sys_privs WHERE grantee = 'USER_LUS_2026';

-- 4. Voir les privilèges sur les objets (tables) accordés
SELECT * FROM dba_tab_privs WHERE grantee = 'USER_LUS_2026';

-- 5. Voir les rôles possédés par un utilisateur
SELECT * FROM dba_role_privs WHERE grantee = 'USER_LUS_2026';
