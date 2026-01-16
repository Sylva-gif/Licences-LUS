## CONTENU DU COURS

### Chapitre 1 : Introduction aux systèmes RAID (Redundant Array of Independent Disks)
- Chapitre 2 : Base de données Oracle Server
  1. Composants de l'architecture Oracle  
  2. Initiation à Oracle Server  
  3. Gérer une instance et BD Oracle  
  4. Gérer les fichiers de BD Oracle  

#### Manipulation de stockage SGBDR Oracle
1. Gérer des tablespaces  
2. Gérer des données en annulation  
3. Gérer des segments, Index, Tables  

#### Sécurité de serveur Oracle
1. Gérer des utilisateurs  
2. Gérer des privilèges  
3. Gérer les rôles  
4. Sauvegarde, Export et Import d'une BD Oracle  

---

## Objectifs du cours DBA et sécurité des données
- Connaître les systèmes RAID et les principes de la sécurité des serveurs.  
- Identifier différents composants de l'architecture Oracle.  
- Installer logiciels Oracle et créer une base opérationnelle.  
- Démarrer et arrêter une base Oracle.  
- Optimiser les performances et automatiser les tâches.  
- Gérer utilisateurs, privilèges et ressources.  
- Protéger les données avec chiffrement et politiques d'accès.  
- Auditer les activités et prévenir les attaques (SQL injection, etc.).  
- Appliquer mises à jour et correctifs de sécurité.  
- Sauvegarder, restaurer et sécuriser une base Oracle.  

---

## Tâches de l'administrateur DBA
- Installer les systèmes RAID des serveurs  
- Planification et création de bases  
- Gestion de la disponibilité des bases  
- Gestion des structures physiques et logiques  
- Gestion du stockage  
- Gestion de la sécurité et surveillance des accès  
- Contrôle des privilèges et authentification  
- Protéger les données contre menaces internes/externes  
- Administration réseau  
- Sauvegarde et récupération  
- Réglage des bases  

---

## Bases de données avancées
### Définition
Les bases avancées dépassent les bases relationnelles classiques, intégrant des concepts modernes pour gérer gros volumes, performance et cas spécifiques.

### Types
- Relationnelles (SQL)  
- NoSQL : MongoDB, Cassandra, Redis, Couchbase  
- Graphes : Neo4j, OrientDB  
- Orientées objets  

### Caractéristiques
- Indexation avancée (B-trees, R-trees, full-text)  
- Partitionnement et sharding  
- Bases multimédia et spatiales (PostGIS, Oracle Spatial)  
- Bases temps réel et transactionnelles (support ACID)  

### Exemples
- PostgreSQL (ACID, transactions complexes)  
- Oracle Database (OLTP, bancaire/financier)  
- Cassandra (scalabilité horizontale, haute dispo, utilisé par Netflix, Facebook, Uber)  

---

## Oracle Database avancée
- Oracle Big Data SQL (intégration Hadoop, NoSQL)  
- Compression avancée (Advanced Compression)  
- Indexation fonctionnelle et de domaine  
- Multi-plateformes (UNIX, Linux, Windows)  
- Support Java embarqué, Corba  
- Outils : Oracle 11g, 18c, 21c, RAC, Enterprise Manager Packs Security  

---

## Chapitre 1 : Systèmes RAID et Sécurité des serveurs
### Objectifs
Regrouper plusieurs disques physiques en une unité logique pour :  
- Améliorer les performances  
- Offrir tolérance aux pannes  
- Assurer redondance des données  

### Niveaux RAID
- RAID 0 : Stripping, performance, pas de sécurité  
- RAID 1 : Mirroring, sécurité maximale, duplexing  
- RAID 2 : Correction d’erreurs, fiabilité accrue  
- RAID 3 : Performance + tolérance, min. 3 disques  
- RAID 4 : Segments variables, proche RAID 3  
- RAID 5 : Parité répartie, tolérance à une panne  
- RAID 6 : Double parité, tolérance à deux pannes  

# Systèmes RAID : Caractéristiques, Avantages et Inconvénients

## RAID 0 (Stripping)
### Caractéristiques
- Données réparties sur plusieurs disques.
- Minimum : 2 disques.
- Pas de redondance.

### Avantages
- Performances élevées en lecture/écriture.
- Capacité totale = somme des disques.

### Inconvénients
- Aucune tolérance aux pannes : perte totale si un disque tombe en panne.
- Pas adapté aux données critiques.

---

## RAID 1 (Mirroring)
### Caractéristiques
- Données dupliquées sur 2 disques ou plus.
- Capacité utile = taille d’un seul disque.

### Avantages
- Sécurité maximale : tolérance à la panne d’un disque.
- Lecture plus rapide (les deux disques peuvent être lus en parallèle).

### Inconvénients
- Coût élevé (capacité divisée par 2).
- Capacité utile limitée.

---

## RAID 2
### Caractéristiques
- Similaire au RAID 1 mais avec correction d’erreurs.
- Lecture : un seul disque actif, les autres « au repos ».

### Avantages
- Fiabilité accrue grâce à la correction d’erreurs.
- Données protégées contre corruption.

### Inconvénients
- Performances réduites en lecture.
- Peu utilisé aujourd’hui.

---

## RAID 3
### Caractéristiques
- Minimum : 3 disques.
- Données réparties + disque dédié à la parité.

### Avantages
- Performances améliorées (comme RAID 0).
- Tolérance à une panne (grâce au disque de parité).

### Inconvénients
- Dépendance forte au disque de parité.
- Risque de goulot d’étranglement.

---

## RAID 4
### Caractéristiques
- Proche du RAID 3.
- Segments de taille variable.
- Minimum : 3 disques.

### Avantages
- Lecture rapide.
- Parité centralisée.

### Inconvénients
- Disque de parité surchargé.
- Moins performant que RAID 5.

---

## RAID 5
### Caractéristiques
- Minimum : 3 disques.
- Parité répartie sur tous les disques.
- Capacité utile = (N-1) × taille disque.

### Avantages
- Bonne performance en lecture.
- Tolérance à une panne.
- Utilisation efficace de l’espace.

### Inconvénients
- Reconstruction longue en cas de panne.
- Perte totale si 2 disques tombent en panne.

---

## RAID 6
### Caractéristiques
- Minimum : 4 disques.
- Double parité répartie.
- Capacité utile = (N-2) × taille disque.

### Avantages
- Tolérance à 2 pannes simultanées.
- Sécurité renforcée pour gros systèmes.

### Inconvénients
- Performances inférieures au RAID 5.
- Capacité utile réduite.
- Reconstruction plus complexe.

---

## Comparatif rapide

| Niveau | Min. disques | Capacité utile | Tolérance aux pannes | Performance |
|--------|--------------|----------------|----------------------|-------------|
| RAID 0 | 2            | Somme totale   | 0                    | Très élevée |
| RAID 1 | 2            | Taille d’un disque | 1 disque         | Lecture rapide |
| RAID 2 | ≥2           | Taille d’un disque | 1 disque         | Lecture réduite |
| RAID 3 | ≥3           | (N-1) × taille | 1 disque             | Bonne       |
| RAID 4 | ≥3           | (N-1) × taille | 1 disque             | Lecture rapide |
| RAID 5 | ≥3           | (N-1) × taille | 1 disque             | Équilibrée  |
| RAID 6 | ≥4           | (N-2) × taille | 2 disques            | Moyenne     |

---


---
