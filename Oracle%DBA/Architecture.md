# 📂 Résumé de Cours : Architecture & Administration Oracle Database 21c

## 🏗️ 1. Schéma Global de l'Architecture
Voici la structure d'un serveur Oracle (Instance + Base de données) telle qu'étudiée en cours.

![Architecture Oracle Database](architecture.jpg(1).jpg)

---

## 🧠 2. Structures Mémoire (Détails du Schéma)

### A. L'Instance (SGA - System Global Area)
La **SGA** est la mémoire partagée, allouée au démarrage de l'instance.
*   **Zone de mémoire partagée (Shared Pool)** : 
    *   *Cache "library"* : Stocke les dernières instructions SQL et PL/SQL exécutées.
    *   *Cache du dictionnaire* : Contient les définitions des objets (tables, colonnes) et les privilèges.
*   **Cache de tampons (Buffer Cache)** : Stocke les blocs de données lus depuis les fichiers de données pour accélérer les futurs accès.
*   **Tampon de journalisation (Redo Log Buffer)** : Enregistre toutes les modifications apportées à la base pour permettre la récupération en cas de panne.
*   **Zone Java & Large Pool** : Utilisées pour l'analyse des commandes Java et les opérations lourdes (RMAN, serveurs partagés).

### B. La Mémoire Privée (PGA - Program Global Area)
Chaque **Processus Serveur** possède sa propre **PGA**. Contrairement à la SGA, elle n'est pas partagée. Elle sert au tri des données et à la gestion des variables de session utilisateur.

---

## ⚙️ 3. Les Processus d'Arrière-plan
Ils assurent la liaison entre la mémoire vive et le stockage physique :
*   **DBWR (Database Writer)** : Écrit les données modifiées (dirty buffers) du cache vers les fichiers de données.
*   **LGWR (Log Writer)** : Écrit le contenu du Redo Log Buffer dans les fichiers de journalisation sur disque.
*   **CKPT (Checkpoint)** : Met à jour les fichiers de contrôle et déclenche l'écriture des données pour garantir la synchronisation.
*   **PMON (Process Monitor)** : Surveille les processus serveurs et nettoie les ressources des sessions utilisateur défaillantes.
*   **SMON (System Monitor)** : Récupère l'instance automatiquement après une panne et nettoie les segments temporaires.

---

## 💾 4. Structure Physique (La Base de Données)
*   **Fichiers de données (.dbf)** : Stockage réel des informations.
*   **Fichiers de contrôle (.ctl)** : Contient la structure physique de la base (essentiel pour le démarrage).
*   **Fichiers de journalisation (.log)** : Historique des transactions (Redo Logs).
*   **Fichiers de Journalisation archivés** : Copies des journaux permettant une restauration historique (Point-in-Time Recovery).

---

## 💼 5. Ressources & Pratiques pour le Milieu Professionnel

### 🚀 Commandes Essentielles du DBA (SQL*Plus)
```sql
-- Vérifier l'état de l'instance
SELECT instance_name, status FROM v$instance;

-- Identifier si on utilise un SPFILE (binaire) ou PFILE (texte)
SHOW PARAMETER spfile;

-- Voir la configuration de la mémoire automatique (21c)
SHOW PARAMETER memory_target;

-- Créer un utilisateur et lui accorder des droits
CREATE USER dba_admin IDENTIFIED BY password123;
GRANT DBA TO dba_admin;
