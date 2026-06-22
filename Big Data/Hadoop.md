
# Chapitre 2 : Hadoop

## Introduction à Hadoop

Hadoop est une plateforme open-source conçue pour le **traitement distribué de très grands ensembles de données** (Big Data) sur des clusters de machines. Son objectif principal est de faciliter la création d'applications distribuées et évolutives (scalables) pour gérer des volumes de données massifs, de l'ordre de plusieurs pétaoctets.

Hadoop s'inscrit pleinement dans l'écosystème du Big Data et est géré sous l'égide de la fondation Apache. Il est principalement écrit en Java.

### Historique rapide

*   **2002**: Doug Cutting et Mike Cafarella développent Nutch, un moteur de recherche open-source exploitant le calcul distribué, mais avec des limitations.
*   **2003/2004**: Google publie deux *whitepapers* fondamentaux sur GFS (Google File System) et le paradigme MapReduce. Ces publications inspireront directement Hadoop.
*   **2004**: Doug Cutting et Mike Cafarella développent un *framework* inspiré des travaux de Google, sur lequel ils portent le projet Nutch.
*   **2006**: Doug Cutting, chez Yahoo, améliore ce *framework* pour l'indexation de leur moteur de recherche. Il le nomme **Hadoop**, en référence à l'éléphant en peluche de son fils.
*   **2008**: Le développement de Hadoop est mature, et il est massivement exploité par Yahoo et d'autres entreprises.
*   **2011**: Hadoop est largement adopté, avec des clusters comme celui de Yahoo atteignant 42 000 machines et des centaines de pétaoctets de stockage.

## Critères des solutions Big Data assurés par Hadoop

Hadoop excelle à répondre aux exigences fondamentales des solutions Big Data :

*   **Performance**: Traite des *datasets* énormes (millions de fichiers, Go à To) en exploitant le **parallélisme** et la mémoire des clusters de calcul.
*   **Économie**: Réduit les coûts en utilisant du matériel de calcul standard et peu coûteux (commodité hardware).
*   **Évolutivité (Scalabilité)**: Un ajout de nœuds au cluster se traduit par une amélioration des performances et de la capacité de stockage/traitement.
*   **Tolérance aux pannes**: La défaillance d'un nœud n'entraîne pas l'échec du calcul. Les données sont répliquées et les tâches peuvent être relancées ailleurs.
*   **Parallélisme de données**: Le même calcul peut être effectué simultanément sur différentes parties des données, accélérant ainsi le traitement global.

## Composants fondamentaux de Hadoop

Hadoop est traditionnellement composé de deux parties principales :

1.  **Hadoop Distributed File System (HDFS)** :
    *   Destiné au **stockage distribué des données**.
    *   Permet de manipuler un système de fichiers distribué comme s'il s'agissait d'un disque dur unique.
    *   Gère la localisation des données et la tolérance aux pannes.
    *   Inspiré de Google File System (GFS).

2.  **MapReduce** :
    *   Un *framework* de programmation distribuée destiné au **traitement distribué des données**.
    *   Permet de paralléliser les calculs sur de grands ensembles de données.
    *   Inspiré des publications MapReduce de Google.

    

## HDFS : Présentation détaillée

HDFS est le système de fichiers distribué de Hadoop. C'est un système :

*   **Distribué**: Les données sont stockées sur plusieurs machines d'un cluster.
*   **Extensible**: Sa capacité peut être augmentée en ajoutant de nouvelles machines.
*   **Portable**: Fonctionne sur différents systèmes d'exploitation (déployable sur Linux, Windows, etc.).
*   **Tolérant aux pannes**: Grâce à la réplication des données.
*   **Conçu pour de très gros volumes**: Stocke des données sur des milliers de machines peu coûteuses équipées de disques durs banalisés.

### Caractéristiques clés de HDFS

*   **Abstraction de l'architecture physique**: HDFS présente le cluster de stockage comme un disque dur unique, simplifiant la manipulation des données.
*   **Concepts hérités des systèmes de fichiers classiques**: Il réutilise des notions comme les blocs, les métadonnées, les droits et l'arborescence des répertoires.
*   **Indépendance du noyau de l'OS**: Il n'est pas solidaire du noyau du système d'exploitation, offrant une grande portabilité.
*   **Système distribué par essence**: Chaque nœud du cluster stocke un sous-ensemble du volume global de données. Pour augmenter ce volume, il suffit d'ajouter de nouveaux nœuds.
*   **Taille des blocs supérieure**: Par défaut, les blocs HDFS sont de 64 Mo (configurable jusqu'à 1 Go), bien plus grands que les 4 Ko des systèmes classiques. Cela réduit le temps d'accès aux blocs.
*   **Réplication des blocs**: HDFS réplique chaque bloc de données sur plusieurs nœuds (configurable, souvent 3 par défaut) pour assurer la tolérance aux pannes. Si un nœud devient indisponible, les copies du bloc sont accessibles sur d'autres nœuds.

### Architecture de HDFS

Un cluster HDFS repose sur trois types de composants majeurs :

1.  **NameNode (nœud de nom)** :
    *   Le **service central** qui gère l'état du système de fichiers.
    *   Il maintient l'**arborescence des répertoires** et toutes les **métadonnées** des fichiers.
    *   Il connaît l'emplacement de chaque bloc de données sur les DataNodes.
    *   Historiquement un **point unique de défaillance (SPOF)**, mais Hadoop 2 a introduit le Secondary NameNode pour pallier ce problème.

2.  **Secondary NameNode** :
    *   Dans Hadoop 2, il est introduit pour gérer le problème du SPOF du NameNode.
    *   Il vérifie périodiquement l'état du NameNode principal et copie ses métadonnées.
    *   En cas d'indisponibilité du NameNode principal, le Secondary NameNode peut prendre sa place (bien que la récupération ne soit pas instantanée et puisse nécessiter une intervention).

3.  **DataNode (nœud de données)** :
    *   Ce sont les **workers** qui stockent les blocs de données eux-mêmes.
    *   Il y a un DataNode par machine au sein du cluster.
    *   Ils reçoivent les ordres du NameNode pour les opérations de lecture et d'écriture.


#### Remarque sur l'architecture HDFS 2.x

Hadoop 2 introduit des améliorations significatives :

*   **Federation HDFS**: Permet à plusieurs NameNodes de gérer différents "namespaces" (espaces de noms) au sein du même cluster. Cela résout le problème du NameNode comme goulot d'étranglement pour un grand nombre de petits fichiers. Par exemple, un NameNode peut gérer `/user` et un autre `/share`.
*   **High Availability (HA) NameNode**: Avec Hadoop 2, il est possible d'avoir deux NameNodes en mode actif/passif avec un mécanisme de *failover* automatique pour une meilleure résilience.

### Écriture d'un fichier sur HDFS

Voici le processus simplifié d'écriture d'un fichier sur HDFS :

1.  **Client Hadoop**: L'utilisateur (ou l'application) lance une commande Hadoop (ex: `hadoop fs -put fichier.txt /chemin/hdfs/fichier.txt`).
2.  **Contact NameNode**: Le client contacte le NameNode pour lui indiquer qu'il souhaite écrire un fichier et le divise en blocs (par défaut 64 Mo).
3.  **Attribution des DataNodes**: Le NameNode répond en indiquant au client sur quels DataNodes les blocs doivent être stockés (en tenant compte de la réplication).
4.  **Écriture directe aux DataNodes**: Le client envoie directement les blocs aux DataNodes désignés.
5.  **Réplication inter-DataNodes**: Chaque DataNode, après avoir reçu un bloc, le réplique sur d'autres DataNodes (selon la politique de réplication) et informe le NameNode.
6.  **Confirmation**: Une fois tous les blocs stockés et répliqués, le NameNode confirme l'opération au client.

    

### Lecture d'un fichier sur HDFS

Le processus de lecture est également distribué :

1.  **Client Hadoop**: L'utilisateur lance une commande de lecture (ex: `hadoop fs -get /chemin/hdfs/fichier.txt fichier_local.txt`).
2.  **Contact NameNode**: Le client contacte le NameNode pour demander la lecture du fichier.
3.  **Localisation des blocs**: Le NameNode répond en indiquant la liste des blocs qui composent le fichier et les DataNodes où ces blocs sont disponibles.
4.  **Lecture directe aux DataNodes**: Le client contacte directement les DataNodes pour récupérer les blocs.
5.  **Tolérance aux pannes**: En cas d'indisponibilité d'un DataNode, le client tente de récupérer le bloc sur une autre copie répliquée.
6.  **Reconstruction du fichier**: Le client assemble les blocs récupérés pour reconstituer le fichier original.

    

### La commande `hadoop fs`

L'utilitaire `hadoop fs` permet d'interagir avec HDFS depuis la console, reproduisant des commandes Unix/Linux classiques.

*   `hadoop fs -put <local_file> <hdfs_path>`: Stocke un fichier local sur HDFS.
*   `hadoop fs -get <hdfs_path> <local_file>`: Récupère un fichier de HDFS vers le système local.
*   `hadoop fs -mkdir <hdfs_path>`: Crée un répertoire sur HDFS.
*   `hadoop fs -rm <hdfs_path>`: Supprime un fichier sur HDFS.
*   `hadoop fs -ls <hdfs_path>`: Liste le contenu d'un répertoire sur HDFS.
*   `hadoop fs -cp <source_hdfs_path> <destination_hdfs_path>`: Copie un fichier/répertoire sur HDFS.
*   `hadoop fs -rmr <hdfs_path>`: Supprime récursivement un répertoire sur HDFS.
*   `hadoop fs -du <hdfs_path>`: Affiche l'utilisation de l'espace disque pour un fichier/répertoire sur HDFS.

## MapReduce : Présentation détaillée

MapReduce est un paradigme de programmation pour le traitement distribué de grands ensembles de données sur des clusters. Il est basé sur les concepts de "divide and conquer" (diviser pour régner).

### Les deux opérations fondamentales

MapReduce se compose de deux opérations distinctes :

1.  **MAP** :
    *   Prend les données d'entrée et les transforme en une série de **couples clef/valeur**.
    *   Les clefs sont choisies pour regrouper des données pertinentes pour le problème à résoudre.
    *   L'opération MAP est hautement **parallélisable** : les données d'entrée sont découpées en fragments, et chaque fragment est traité indépendamment par une machine du cluster.

2.  **REDUCE** :
    *   Applique un traitement à toutes les valeurs associées à une **clef distincte**.
    *   Au terme de l'opération REDUCE, un résultat est obtenu pour chacune des clefs distinctes.
    *   Chaque machine du cluster se voit attribuer une clef unique et la liste des valeurs associées pour effectuer l'opération REDUCE.

### Les 4 étapes d'un traitement MapReduce

1.  **Découper (Split)** : Les données d'entrée sont divisées en plusieurs fragments logiques.
2.  **Mapper** : Chaque fragment est traité par une tâche Map, produisant des couples (clef ; valeur).
3.  **Grouper (Shuffle & Sort)** : Hadoop regroupe automatiquement tous les couples par clef commune. C'est une opération distribuée de tri.
4.  **Réduire (Reduce)** : Pour chaque clef distincte, une tâche Reduce est exécutée, traitant la liste des valeurs associées et produisant un résultat final.

    ### Exemple concret : Comptage de mots

Imaginons que nous voulons compter l'occurrence de chaque mot dans un texte.

**1. Données d'entrée (le texte)** :

```
Celui qui croyait au ciel
Celui qui n'y croyait pas
Fou qui fait le délicat
Fou qui songe à ses querelles
```

*(Pré-traitement : suppression ponctuation, accents, passage en minuscules)*

```
celui qui croyait au ciel
celui qui ny croyait pas
fou qui fait le delicat
fou qui songe a ses querelles
```

Nous obtenons 4 fragments (chaque ligne est un fragment).

**2. Opération MAP** :
La clef sera le mot lui-même. Pour chaque mot rencontré dans un fragment, on génère le couple (MOT ; 1).

*   Fragment 1: `celui qui croyait au ciel`
    *   `(celui ; 1), (qui ; 1), (croyait ; 1), (au ; 1), (ciel ; 1)`
*   Fragment 2: `celui qui ny croyait pas`
    *   `(celui ; 1), (qui ; 1), (ny ; 1), (croyait ; 1), (pas ; 1)`
*   Fragment 3: `fou qui fait le delicat`
    *   `(fou ; 1), (qui ; 1), (fait ; 1), (le ; 1), (delicat ; 1)`
*   Fragment 4: `fou qui songe a ses querelles`
    *   `(fou ; 1), (qui ; 1), (songe ; 1), (a ; 1), (ses ; 1), (querelles ; 1)`

**3. Groupement (Shuffle & Sort)** :
Hadoop regroupe automatiquement les couples par clef commune.

*   `celui`: `[1, 1]`
*   `qui`: `[1, 1, 1, 1]`
*   `croyait`: `[1, 1]`
*   `au`: `[1]`
*   `ciel`: `[1]`
*   `ny`: `[1]`
*   `pas`: `[1]`
*   `fou`: `[1, 1]`
*   `fait`: `[1]`
*   `le`: `[1]`
*   `delicat`: `[1]`
*   `songe`: `[1]`
*   `a`: `[1]`
*   `ses`: `[1]`
*   `querelles`: `[1]`

**4. Opération REDUCE** :
Pour chaque clef, on somme les valeurs associées.

*   `celui`: `2`
*   `qui`: `4`
*   `croyait`: `2`
*   `fou`: `2`
*   `au`: `1`
*   `ciel`: `1`
*   `ny`: `1`
*   `pas`: `1`
*   `fait`: `1`
*   `le`: `1`
*   `delicat`: `1`
*   `songe`: `1`
*   `a`: `1`
*   `ses`: `1`
*   `querelles`: `1`

Le mot le plus utilisé est "qui" (4 occurrences).

### Schéma général de MapReduce


    

### Déroulement de l'exécution d'une tâche Hadoop avec YARN

1.  **Soumission par le client**: Le client Hadoop soumet le job (le `.jar` de l'application) au ResourceManager.
2.  **Allocation ApplicationMaster**: Le ResourceManager alloue un Container et y lance l'ApplicationMaster spécifique au job.
3.  **Lancement AM**: L'ApplicationMaster démarre et se confirme au ResourceManager.
4.  **Demande de ressources**: L'ApplicationMaster demande des Containers au ResourceManager pour exécuter les tâches Map et Reduce de son job, en spécifiant les données sur lesquelles travailler.
5.  **Lancement des tâches**: Le ResourceManager attribue des Containers sur différents NodeManagers. L'ApplicationMaster lance ensuite les tâches (Map/Reduce) dans ces Containers.
6.  **Communication inter-composants**:
    *   Les tâches communiquent avec leur ApplicationMaster pour le statut et la progression.
    *   Les NodeManagers communiquent avec le ResourceManager pour l'état des ressources.
7.  **Fin du job**: Une fois toutes les tâches terminées, l'ApplicationMaster s'arrête et ses Containers sont libérés.
### Avantages majeurs de YARN

*   **Scalabilité accrue**: Le découplage des responsabilités permet de gérer des clusters beaucoup plus grands.
*   **Flexibilité**: Hadoop n'est plus limité à MapReduce. D'autres *frameworks* de traitement (Spark, Tez, Flink, Storm, etc.) peuvent s'exécuter sur YARN, partageant les mêmes ressources du cluster.
*   **Meilleure utilisation des ressources**: Le Scheduler de YARN alloue dynamiquement les ressources (RAM, CPU) aux applications en fonction de leurs besoins, optimisant l'utilisation du cluster.
*   **Tolérance aux pannes améliorée**: L'ApplicationMaster gère les échecs au niveau de l'application, tandis que le ResourceManager gère les échecs des nœuds.

## Hadoop 2 : Une évolution architecturale majeure (Résumé)

Hadoop 2 (avec YARN et HDFS 2.x) représente une transformation profonde :

*   **Découplage de HDFS et MapReduce**: Permet à d'autres *frameworks* de traitement de s'appuyer directement sur HDFS.
*   **Hadoop devient un "OS de la donnée"**: Une plateforme générique capable d'exécuter une multitude d'applications Big Data (batch, interactif, streaming, in-memory, etc.).

    
    
