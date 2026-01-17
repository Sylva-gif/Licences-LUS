 Import et Export de base Oracle 21c

## Objectifs
- Comprendre l’export et l’import de données dans Oracle 21c/22c.
- Maîtriser **Data Pump (expdp / impdp)** et les outils classiques (**exp / imp**).
- Créer et utiliser un **répertoire Oracle (Directory)** sur Windows et Unix.
- Exporter et importer : base complète, schéma ou tables spécifiques.
- Utiliser les options avancées : parallélisme, remappage de schéma/tablespace, gestion des tables existantes.
- Appliquer les bonnes pratiques pour sauvegarde et restauration fiables.

---

## Introduction
- **Export** = sauvegarde des données et objets dans un fichier *dump*.
- **Import** = restauration ou migration depuis un fichier *dump*.

### Outils disponibles
- **Data Pump (expdp / impdp)** → recommandé pour Oracle 21c/22c.
- **Outils classiques (exp / imp)** → compatibilité avec anciennes versions.

---

## Comparatif Data Pump vs Exp/Imp

| Fonctionnalité   | Data Pump (expdp/impdp) | Exp/Imp classique |
|------------------|--------------------------|-------------------|
| Performance      | Très rapide              | Moyenne           |
| Parallélisme     | Oui                      | Non               |
| Reprise          | Oui                      | Non               |
| Mode réseau      | Oui                      | Non               |

**Avantages Data Pump :**
- Parallélisme (plusieurs processus simultanés).
- Import/export direct entre deux bases (mode réseau).
- Reprise possible après interruption.

---

## Création de répertoire Oracle (Windows & Unix)

```sql
CREATE OR REPLACE DIRECTORY dpump_dir AS 'C:\oracle\data';
GRANT READ, WRITE ON DIRECTORY dpump_dir TO SYSTEM;
GRANT EXP_FULL_DATABASE TO SYSTEM;
##Export avec Data Pump (EXPDP)
--Export d’un schéma entier
expdp USER_LUS/MyPassword@PDB1 DIRECTORY=dp_dir \
DUMPFILE=USER_LUS.dmp LOGFILE=USER_LUS_exp.log SCHEMAS=USER_LUS
--Exportation de tables spécifiques
expdp USER_LUS/MyPassword@PDB1 DIRECTORY=dp_dir \
DUMPFILE=Tables_lus.dmp LOGFILE=Tables_lus_exp.log TABLES=EMP,DEPT,SALES
--expdp SYSTEM/MyPassword@PDB1 DIRECTORY=dp_dir \
DUMPFILE=FULL_DB.dmp LOGFILE=FULL_DB_exp.log FULL=Y
##Export classique (EXP)
--Export complet
exp system/MyPassword@XEPDB1 FILE=C:\oracle\data\FULL_DB.dmp \
LOG=C:\oracle\data\FULL_DB_exp.log FULL=Y
--Export d’un schéma
exp USER_LUS/123@XEPDB1 FILE=C:\oracle\data\user_lus_DB.dmp \
LOG=C:\oracle\data\user_lus_exp.log OWNER=USER_LUS
--Export de tables spécifiques
exp USER_LUS/123@XEPDB1 FILE=C:\oracle\data\user_lus_tables.dmp \
LOG=C:\oracle\data\user_lus_tables.log TABLES=EMP,DEPT


CREATE OR REPLACE DIRECTORY dpump_dir AS 'C:\oracle\lus_data.dbf';
GRANT READ, WRITE ON DIRECTORY dpump_dir TO lus_db;
