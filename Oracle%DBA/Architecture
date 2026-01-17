# 📂 Résumé de Cours : Architecture & Administration Oracle Database 21c

## 🏗️ 1. Architecture du Serveur Oracle
Un serveur Oracle est l'association d'une **Instance** et d'une **Base de données**.

*   **L'Instance** : Structure éphémère en mémoire (SGA) + Processus d'arrière-plan. Elle est identifiée par un `SID`.
*   **La Base de Données** : Ensemble de fichiers physiques stockés sur disque.
    *   **Data files** : Contiennent les données réelles.
    *   **Control files** : Contiennent l'état de la base et sa structure.
    *   **Redo Log files** : Enregistrent les changements pour la récupération.

---

## 🧠 2. Structures Mémoire

### A. SGA (System Global Area) - Partagée
Allouée au démarrage de l'instance, elle est commune à tous les utilisateurs.
*   **Shared Pool** : 
    *   *Library Cache* : Stocke les instructions SQL/PLSQL.
    *   *Data Dictionary Cache* : Stocke les définitions d'objets et privilèges.
*   **Database Buffer Cache** : Cache pour les blocs de données lus sur le disque.
*   **Redo Log Buffer** : Journalise les transactions avant écriture sur disque.
*   **Large Pool / Java Pool** : Zones spécialisées (RMAN, serveurs partagés, Java).

### B. PGA (Program Global Area) - Privée
Mémoire dédiée à chaque processus serveur (non partagée). Elle contient les informations de session, les tris et les variables locales.

> **Gestion 21c** : Utilisation du mode **AMM (Automatic Memory Management)** avec les paramètres `MEMORY_TARGET` et `MEMORY_MAX_TARGET`.

---

## ⚙️ 3. Processus d'Arrière-plan (Background Processes)
Ils assurent la maintenance et la liaison Mémoire ↔ Disque.
*   **DBWn (Database Writer)** : Écrit les blocs de données modifiés sur disque.
*   **LGWR (Log Writer)** : Écrit les entrées du Redo Log Buffer dans les fichiers Redo Log (se déclenche au COMMIT, toutes les 3s, ou si le buffer est 1/3 plein).
*   **CKPT (Checkpoint)** : Met à jour les en-têtes des fichiers pour signaler la synchronisation.
*   **SMON (System Monitor)** : Récupération après crash (Instance Recovery).
*   **PMON (Process Monitor)** : Nettoie les sessions utilisateur en échec.

---

## 📑 4. Fichiers de Paramètres (Configuration)
| Caractéristique | **PFILE** (initSID.ora) | **SPFILE** (spfileSID.ora) |
| :--- | :--- | :--- |
| **Format** | Texte (Éditable à la main) | Binaire (Non éditable) |
| **Modification** | Nécessite un redémarrage | Dynamique (`ALTER SYSTEM`) |
| **Priorité** | Secondaire | Prioritaire au démarrage |

---

## 🛠️ 5. Outils d'Administration
*   **SQL*Plus** : L'outil de base en ligne de commande.
*   **OUI (Oracle Universal Installer)** : Pour l'installation du logiciel.
*   **DBCA** : Pour la création et configuration de la base de données.
*   **OEM (Enterprise Manager)** : Interface graphique pour l'administration et le monitoring (gestion 21c : Blockchain tables, AutoML, JSON).

---

## 💼 6. Ressources & Milieu Professionnel (Expert DBA)

### 🚀 Commandes Essentielles (Cheat Sheet)
```sql
-- Connexion admin
sqlplus / as sysdba

-- Vérifier le mode de démarrage (PFILE ou SPFILE)
SHOW PARAMETER spfile;

-- Modifier un paramètre dynamiquement
ALTER SYSTEM SET shared_pool_size = 500M SCOPE=BOTH;

-- Créer un utilisateur et donner des droits
CREATE USER mon_user IDENTIFIED BY mot_de_passe;
GRANT CONNECT, RESOURCE TO mon_user;

-- État de la base
SELECT status FROM v$instance;
