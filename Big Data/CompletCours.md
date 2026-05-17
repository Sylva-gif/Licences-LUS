# 📊 Cours Complet : Big Data — Des Fondamentaux à l'Intelligence Artificielle

> **Auteur :** Expert Big Data & Data Engineering  
> **Niveau :** Intermédiaire à Avancé  
> **Durée estimée :** 40–60 heures de formation  
> **Dernière mise à jour :** 2025  

---

## 📋 Table des Matières

1. [Chapitre 1 : Introduction au Big Data](#chapitre-1--introduction-au-big-data)
2. [Chapitre 2 : Hadoop](#chapitre-2--hadoop)
   - [Généralités](#21-généralités)
   - [Architecture HDFS](#22-architecture-hdfs)
   - [Algorithme MapReduce](#23-algorithme-mapreduce)
   - [Installation et Configuration (TP)](#24-tp--installation-et-configuration-de-hadoop)
3. [Chapitre 3 : Utilisation de Hadoop](#chapitre-3--utilisation-de-hadoop)
   - [Manipulation de HDFS](#31-manipulation-de-hdfs)
   - [Développement MapReduce](#32-développement-dune-application-mapreduce)
   - [TP inclus](#33-tp--application-mapreduce-wordcount-avancé)
4. [Chapitre 4 : Apache Spark](#chapitre-4--apache-spark)
   - [TP inclus](#43-tp--analyse-de-données-avec-spark)
5. [Chapitre 5 : NoSQL](#chapitre-5--nosql)
6. [Chapitre 6 : HBase & MongoDB](#chapitre-6--hbase--mongodb)
   - [TP inclus](#63-tp--hbase-et-mongodb)
7. [Chapitre 7 : Big Data & Intelligence Artificielle](#chapitre-7--big-data--intelligence-artificielle)
8. [Certifications Recommandées](#certifications-recommandées)
9. [Ressources et Références](#ressources-et-références)

---

# Chapitre 1 : Introduction au Big Data

## 1.1 Qu'est-ce que le Big Data ?

Le terme **Big Data** désigne des ensembles de données si volumineux, variés et générés si rapidement que les outils traditionnels de gestion de bases de données ne peuvent plus les traiter efficacement.

### Les 5 V du Big Data

| V | Description | Exemple concret |
|---|-------------|-----------------|
| **Volume** | Quantité massive de données | Facebook génère ~4 pétaoctets de données par jour |
| **Vélocité** | Vitesse de génération et traitement | Twitter traite 500 millions de tweets par jour |
| **Variété** | Diversité des formats | Texte, images, vidéos, IoT, logs, JSON... |
| **Véracité** | Fiabilité et qualité des données | Données bruitées, incomplètes, contradictoires |
| **Valeur** | Utilité extraite des données | Recommandations Netflix = +1 milliard $/an d'économie |

> 💡 **Exemple concret :** Une enseigne de grande distribution comme Carrefour collecte chaque seconde : les transactions des caisses, les mouvements de stock, les scans de cartes fidélité, les données des capteurs de température des congélateurs, et les clics sur son application mobile. Tout cela constitue du Big Data.

## 1.2 Histoire et Évolution

```
Années 1990    → Bases de données relationnelles (Oracle, MySQL)
Années 2000    → Explosion d'Internet → naissance du problème
2003-2004      → Google publie ses papiers sur GFS et MapReduce
2006           → Naissance de Hadoop (Yahoo, basé sur les travaux Google)
2010           → Explosion du Cloud Computing (AWS, Azure, GCP)
2012-2014      → Spark, Kafka, Storm émergent
2015-2020      → Lacs de données (Data Lakes), architectures Lambda/Kappa
2020-2025      → Big Data + IA : MLOps, LLMs, Data Mesh
```

## 1.3 Pourquoi le Big Data ?

### Cas d'usage réels

**Santé :** L'hôpital Mount Sinai à New York analyse les données de 4 millions de patients pour prédire les maladies avant les symptômes cliniques.

**Finance :** JPMorgan Chase utilise le Big Data pour détecter les fraudes en moins de 2 millisecondes par transaction.

**Retail :** Amazon génère 35% de ses revenus grâce aux recommandations alimentées par le Big Data.

**Transport :** Uber traite en temps réel les positions GPS de millions de chauffeurs et passagers pour optimiser les itinéraires et les tarifs dynamiques.

## 1.4 Architecture d'un Système Big Data

```
┌─────────────────────────────────────────────────────────────┐
│                    SOURCES DE DONNÉES                        │
│  IoT │ Réseaux Sociaux │ Logs │ Transactions │ Capteurs     │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────┐
│                    INGESTION                                  │
│         Apache Kafka │ Flume │ Sqoop │ NiFi                  │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────┐
│                    STOCKAGE                                   │
│         HDFS │ S3 │ Azure Data Lake │ HBase │ Cassandra      │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────┐
│                    TRAITEMENT                                 │
│         Hadoop MapReduce │ Apache Spark │ Flink │ Storm       │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────┐
│               ANALYSE & VISUALISATION                         │
│         Hive │ Pig │ Tableau │ Power BI │ Kibana │ Superset  │
└─────────────────────────────────────────────────────────────┘
```

## 1.5 Architectures de Référence

### Architecture Lambda
Combine le batch processing (précis) et le stream processing (temps réel) :
- **Batch Layer** : retraite toutes les données (Hadoop)
- **Speed Layer** : traitement temps réel (Spark Streaming, Kafka)
- **Serving Layer** : expose les résultats (HBase, Cassandra)

### Architecture Kappa
Simplifie Lambda en n'utilisant qu'un seul flux de streaming :
- Tout est traité comme un flux d'événements
- Kafka comme source de vérité unique
- Moins complexe, plus facile à maintenir

### Data Lakehouse (moderne)
Combine les avantages des Data Lakes et Data Warehouses :
- Delta Lake, Apache Iceberg, Apache Hudi
- Utilisé par Databricks, Snowflake

---

# Chapitre 2 : Hadoop

## 2.1 Généralités

### Qu'est-ce qu'Hadoop ?

**Apache Hadoop** est un framework open-source permettant le stockage et le traitement distribué de très grands volumes de données sur des clusters de machines ordinaires (commodity hardware).

### Philosophie fondatrice

> *"Plutôt que de déplacer les données vers le calcul, déplacer le calcul vers les données."*
> — Doug Cutting, créateur d'Hadoop

### Histoire d'Hadoop

- **2003** : Google publie le papier sur GFS (Google File System)
- **2004** : Google publie le papier sur MapReduce
- **2006** : Doug Cutting et Mike Cafarella créent Hadoop chez Yahoo!
- **2008** : Hadoop devient un projet Apache de premier niveau
- **2012** : Hadoop 2.x avec YARN (meilleure gestion des ressources)
- **2017** : Hadoop 3.x (Erasure Coding, amélioration des performances)

### Composants du Ecosystème Hadoop

```
┌─────────────────────── ÉCOSYSTÈME HADOOP ───────────────────────────┐
│                                                                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐           │
│  │  Hive    │  │   Pig    │  │  HBase   │  │  Sqoop   │           │
│  │(SQL-like)│  │(scripts) │  │(NoSQL DB)│  │(import)  │           │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘           │
│       └──────────────┴──────────────┴──────────────┘               │
│                              │                                       │
│  ┌───────────────────────────▼──────────────────────────────────┐  │
│  │                    YARN (Gestion des Ressources)              │  │
│  │          ResourceManager │ NodeManager │ ApplicationMaster    │  │
│  └───────────────────────────┬──────────────────────────────────┘  │
│                              │                                       │
│  ┌───────────────────────────▼──────────────────────────────────┐  │
│  │                    HDFS (Stockage Distribué)                  │  │
│  │              NameNode │ DataNode │ Secondary NameNode         │  │
│  └───────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────┘
```

## 2.2 Architecture HDFS

### HDFS (Hadoop Distributed File System)

HDFS est le système de fichiers distribué d'Hadoop. Il divise les fichiers en blocs et les répartit sur plusieurs machines.

### Caractéristiques clés

| Caractéristique | Valeur par défaut | Description |
|----------------|-------------------|-------------|
| Taille de bloc | 128 MB (Hadoop 2+) | Chaque fichier est découpé en blocs de cette taille |
| Facteur de réplication | 3 | Chaque bloc est copié 3 fois |
| Tolérance aux pannes | Automatique | Si un DataNode tombe, les données restent disponibles |

### Composants HDFS

#### NameNode (Maître)
- Gère l'espace de noms du système de fichiers
- Stocke les métadonnées : quels blocs constituent quel fichier, où sont ces blocs
- **Ne stocke pas les données réelles** — seulement la carte
- Point de défaillance unique → solution : HA NameNode (High Availability)

#### DataNode (Esclave)
- Stocke les blocs de données réels
- Envoie des heartbeats au NameNode toutes les 3 secondes
- Rapport de blocs périodique au NameNode

#### Secondary NameNode
- Fusionne les logs de modifications (EditLog) avec l'image du système de fichiers (FsImage)
- **N'est PAS un NameNode de secours** (erreur commune !)

```
Exemple de stockage d'un fichier de 300 MB avec bloc de 128 MB :

Fichier : rapport_ventes_2024.csv (300 MB)
          │
          ├── Bloc 1 (128 MB) → DataNode 1, DataNode 3, DataNode 5
          ├── Bloc 2 (128 MB) → DataNode 2, DataNode 4, DataNode 6
          └── Bloc 3 (44 MB)  → DataNode 1, DataNode 4, DataNode 7
                                   ↑
                             Réplication × 3
```

### Écriture dans HDFS

```
Client → NameNode : "Je veux écrire rapport.csv"
NameNode → Client : "Écris sur DataNode1, réplique sur DN3, DN5"
Client → DataNode1 → DataNode3 → DataNode5 : Pipeline d'écriture
DataNode5 → DataNode3 → DataNode1 → Client : Acknowledgment
Client → NameNode : "Écriture terminée"
```

### Lecture depuis HDFS

```
Client → NameNode : "Je veux lire rapport.csv"
NameNode → Client : "Bloc1 sur DN1, Bloc2 sur DN2, Bloc3 sur DN4"
Client → DataNode1 : lecture du Bloc1 (le plus proche)
Client → DataNode2 : lecture du Bloc2
Client → DataNode4 : lecture du Bloc3
```

### Rack Awareness

HDFS place intelligemment les réplicas :
- Réplica 1 : même DataNode que l'écrivain
- Réplica 2 : DataNode dans un rack différent
- Réplica 3 : DataNode dans le même rack que le réplica 2

Cela optimise la bande passante tout en garantissant la tolérance aux pannes.

## 2.3 Algorithme MapReduce

### Concept Fondamental

MapReduce est un modèle de programmation pour le traitement de données massives en parallèle. Il se décompose en deux phases principales :

```
Données d'entrée → MAP → Shuffle & Sort → REDUCE → Données de sortie
```

### Exemple Classique : Comptage de Mots (WordCount)

**Données d'entrée :**
```
"Hadoop est puissant. Spark est rapide. Hadoop et Spark sont complémentaires."
```

**Phase MAP :**
```
Mapper 1 : "Hadoop est puissant"
  → (Hadoop, 1), (est, 1), (puissant, 1)

Mapper 2 : "Spark est rapide"
  → (Spark, 1), (est, 1), (rapide, 1)

Mapper 3 : "Hadoop et Spark sont complémentaires"
  → (Hadoop, 1), (et, 1), (Spark, 1), (sont, 1), (complémentaires, 1)
```

**Phase SHUFFLE & SORT (automatique) :**
```
(Hadoop, [1, 1])
(Spark, [1, 1])
(est, [1, 1])
(puissant, [1])
(rapide, [1])
(et, [1])
...
```

**Phase REDUCE :**
```
(Hadoop, 2)
(Spark, 2)
(est, 2)
(puissant, 1)
(rapide, 1)
```

### Exemple Avancé : Calcul du Chiffre d'Affaires par Région

**Problème :** Calculer le CA total par région à partir de millions de transactions.

**Données d'entrée :**
```csv
transaction_id,region,montant
T001,Nord,1500.00
T002,Sud,2300.50
T003,Nord,890.25
T004,Est,4500.00
T005,Sud,1200.00
```

**Mapper :**
```java
public class CAMapper extends Mapper<LongWritable, Text, Text, DoubleWritable> {
    public void map(LongWritable key, Text value, Context context) {
        String[] fields = value.toString().split(",");
        if (!fields[0].equals("transaction_id")) { // Skip header
            String region = fields[1];
            double montant = Double.parseDouble(fields[2]);
            context.write(new Text(region), new DoubleWritable(montant));
        }
    }
}
```

**Reducer :**
```java
public class CAReducer extends Reducer<Text, DoubleWritable, Text, DoubleWritable> {
    public void reduce(Text region, Iterable<DoubleWritable> montants, Context context) {
        double total = 0;
        for (DoubleWritable m : montants) {
            total += m.get();
        }
        context.write(region, new DoubleWritable(total));
    }
}
```

**Résultat :**
```
Est    4500.00
Nord   2390.25
Sud    3500.50
```

### Phases Détaillées de MapReduce

```
1. INPUT SPLIT
   ↓ Le fichier est découpé en InputSplits (≈ 1 bloc HDFS)
   
2. MAP
   ↓ Chaque split est traité par un Mapper en parallèle
   ↓ Produit des paires (clé, valeur)
   
3. COMBINER (optionnel, "mini-reducer" local)
   ↓ Réduit les données avant le réseau
   ↓ Économise de la bande passante
   
4. PARTITIONER
   ↓ Détermine quel Reducer reçoit quelle clé
   ↓ hash(clé) % nombre_de_reducers
   
5. SHUFFLE & SORT
   ↓ Transfert réseau des données Map → Reduce
   ↓ Tri par clé
   
6. REDUCE
   ↓ Agrégation finale par clé
   
7. OUTPUT
   ↓ Écriture du résultat dans HDFS
```

### Optimisations MapReduce

**Combiner :** Effectue une réduction locale avant le shuffle réseau. Réduit les données transférées sur le réseau de 50–70%.

**Compression :** Compresser les données intermédiaires avec Snappy ou LZO :
```xml
<property>
  <name>mapreduce.map.output.compress</name>
  <value>true</value>
</property>
<property>
  <name>mapreduce.map.output.compress.codec</name>
  <value>org.apache.hadoop.io.compress.SnappyCodec</value>
</property>
```

## 2.4 TP : Installation et Configuration de Hadoop

### Prérequis
- Ubuntu 20.04 ou supérieur (ou CentOS 7+)
- Java JDK 8 ou 11
- SSH configuré
- Minimum 4 GB RAM (8 GB recommandé)

### Étape 1 : Installation de Java

```bash
# Mise à jour du système
sudo apt update && sudo apt upgrade -y

# Installation de Java 11
sudo apt install openjdk-11-jdk -y

# Vérification
java -version
# Attendu : openjdk version "11.x.x"

# Définir JAVA_HOME
echo 'export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64' >> ~/.bashrc
source ~/.bashrc
```

### Étape 2 : Configuration SSH sans mot de passe

```bash
# Génération de la clé SSH
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa

# Ajout de la clé publique aux hôtes autorisés
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys

# Test de connexion
ssh localhost
# Doit se connecter sans mot de passe
```

### Étape 3 : Création de l'utilisateur Hadoop

```bash
# Créer un utilisateur dédié
sudo addgroup hadoop
sudo adduser --ingroup hadoop hduser
sudo adduser hduser sudo

# Switcher vers l'utilisateur hadoop
su - hduser
```

### Étape 4 : Téléchargement et Installation d'Hadoop

```bash
# Télécharger Hadoop 3.3.6
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz

# Extraction
tar -xzf hadoop-3.3.6.tar.gz
sudo mv hadoop-3.3.6 /opt/hadoop

# Permissions
sudo chown -R hduser:hadoop /opt/hadoop
```

### Étape 5 : Variables d'Environnement

```bash
# Éditer ~/.bashrc
nano ~/.bashrc

# Ajouter ces lignes à la fin :
export HADOOP_HOME=/opt/hadoop
export HADOOP_INSTALL=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

# Recharger la configuration
source ~/.bashrc

# Vérification
hadoop version
```

### Étape 6 : Configuration des Fichiers Hadoop

#### hadoop-env.sh
```bash
nano /opt/hadoop/etc/hadoop/hadoop-env.sh

# Modifier la ligne JAVA_HOME :
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

#### core-site.xml
```xml
<!-- /opt/hadoop/etc/hadoop/core-site.xml -->
<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://localhost:9000</value>
    <description>URI du NameNode</description>
  </property>
  <property>
    <name>hadoop.tmp.dir</name>
    <value>/opt/hadoop/data/tmp</value>
  </property>
</configuration>
```

#### hdfs-site.xml
```xml
<!-- /opt/hadoop/etc/hadoop/hdfs-site.xml -->
<configuration>
  <property>
    <name>dfs.replication</name>
    <value>1</value>
    <!-- 1 pour mode pseudo-distribué (single node) -->
  </property>
  <property>
    <name>dfs.namenode.name.dir</name>
    <value>file:///opt/hadoop/data/namenode</value>
  </property>
  <property>
    <name>dfs.datanode.data.dir</name>
    <value>file:///opt/hadoop/data/datanode</value>
  </property>
  <property>
    <name>dfs.blocksize</name>
    <value>134217728</value>
    <!-- 128 MB en octets -->
  </property>
</configuration>
```

#### mapred-site.xml
```xml
<!-- /opt/hadoop/etc/hadoop/mapred-site.xml -->
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>
  <property>
    <name>mapreduce.application.classpath</name>
    <value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>
  </property>
</configuration>
```

#### yarn-site.xml
```xml
<!-- /opt/hadoop/etc/hadoop/yarn-site.xml -->
<configuration>
  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>
  <property>
    <name>yarn.nodemanager.env-whitelist</name>
    <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_HOME,PATH,LANG,TZ,HADOOP_MAPRED_HOME</value>
  </property>
  <property>
    <name>yarn.resourcemanager.hostname</name>
    <value>localhost</value>
  </property>
</configuration>
```

### Étape 7 : Formatage et Démarrage

```bash
# Créer les répertoires de données
mkdir -p /opt/hadoop/data/{namenode,datanode,tmp}

# Formater le NameNode (UNE SEULE FOIS !)
hdfs namenode -format

# Démarrer HDFS
start-dfs.sh

# Démarrer YARN
start-yarn.sh

# Vérifier que tout tourne
jps
# Doit afficher : NameNode, DataNode, SecondaryNameNode, ResourceManager, NodeManager
```

### Étape 8 : Vérification via Interface Web

```
HDFS NameNode Web UI    : http://localhost:9870
YARN ResourceManager UI  : http://localhost:8088
MapReduce History Server : http://localhost:19888
```

### Étape 9 : Test de Fonctionnement

```bash
# Créer un répertoire dans HDFS
hdfs dfs -mkdir -p /user/hduser/input

# Copier un fichier local vers HDFS
echo "Hadoop est un framework Big Data puissant. Hadoop permet le traitement distribué." > test.txt
hdfs dfs -put test.txt /user/hduser/input/

# Vérifier le fichier
hdfs dfs -ls /user/hduser/input/
hdfs dfs -cat /user/hduser/input/test.txt

# Lancer le WordCount fourni avec Hadoop
hadoop jar /opt/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar \
  wordcount /user/hduser/input /user/hduser/output

# Voir les résultats
hdfs dfs -cat /user/hduser/output/part-r-00000
```

---

# Chapitre 3 : Utilisation de Hadoop

## 3.1 Manipulation de HDFS

### Commandes Essentielles HDFS

HDFS utilise une syntaxe similaire à Unix/Linux, préfixée par `hdfs dfs`.

#### Navigation et Listing

```bash
# Lister le contenu d'un répertoire
hdfs dfs -ls /
hdfs dfs -ls -h /user/hduser/   # -h pour tailles lisibles (KB, MB, GB)
hdfs dfs -ls -R /user/          # -R pour récursif

# Afficher le contenu d'un fichier
hdfs dfs -cat /user/hduser/donnees.txt

# Afficher les premières/dernières lignes
hdfs dfs -head /user/hduser/gros_fichier.csv   # 1 KB par défaut
hdfs dfs -tail /user/hduser/gros_fichier.csv

# Afficher la taille d'un fichier/répertoire
hdfs dfs -du -h /user/hduser/
hdfs dfs -du -s -h /user/hduser/   # -s pour sommaire
```

#### Gestion des Fichiers et Répertoires

```bash
# Créer un répertoire
hdfs dfs -mkdir /user/hduser/projets
hdfs dfs -mkdir -p /user/hduser/projets/2024/Q1   # Créer l'arborescence complète

# Copier un fichier local vers HDFS
hdfs dfs -put fichier_local.csv /user/hduser/donnees/
hdfs dfs -copyFromLocal fichier_local.csv /user/hduser/donnees/   # Équivalent

# Copier depuis HDFS vers local
hdfs dfs -get /user/hduser/resultats/output.txt ./
hdfs dfs -copyToLocal /user/hduser/resultats/ ./resultats_locaux/

# Copier entre chemins HDFS
hdfs dfs -cp /user/hduser/source/ /user/hduser/destination/

# Déplacer/Renommer
hdfs dfs -mv /user/hduser/ancien_nom.txt /user/hduser/nouveau_nom.txt

# Supprimer
hdfs dfs -rm /user/hduser/fichier.txt
hdfs dfs -rm -r /user/hduser/repertoire/        # Répertoire récursif
hdfs dfs -rm -r -skipTrash /user/hduser/tmp/    # Sans passer par la corbeille

# Fusionner plusieurs fichiers HDFS en un fichier local
hdfs dfs -getmerge /user/hduser/output/ resultat_final.txt
```

#### Gestion des Permissions

```bash
# Changer les permissions (syntaxe Unix)
hdfs dfs -chmod 755 /user/hduser/scripts/
hdfs dfs -chmod -R 644 /user/hduser/donnees/

# Changer le propriétaire
hdfs dfs -chown hduser:hadoop /user/hduser/projets/

# Voir les informations détaillées d'un fichier
hdfs dfs -stat %b /user/hduser/gros_fichier.csv   # Taille en octets
hdfs dfs -stat %r /user/hduser/gros_fichier.csv   # Facteur de réplication
```

#### Administration HDFS

```bash
# Rapport de santé du système de fichiers
hdfs dfsadmin -report

# Informations sur les blocs d'un fichier
hdfs fsck /user/hduser/donnees.csv -files -blocks -locations

# Vérification globale du système
hdfs fsck /

# Forcer le rechargement de la configuration
hdfs dfsadmin -refreshNodes

# Passer un DataNode en mode maintenance
hdfs dfsadmin -putDataNodeInMaintenanceMode <hostname> 0

# Équilibrer la distribution des blocs entre DataNodes
hdfs balancer -threshold 10
```

### Comprendre les Blocs HDFS

```bash
# Voir les blocs d'un fichier spécifique
hdfs fsck /user/hduser/rapport.csv -files -blocks -locations

# Sortie typique :
# /user/hduser/rapport.csv 536870912 bytes, 4 block(s)
# Block: BP-xxx-127.0.0.1-xxx:blk_xxx_xxx len=134217728 Live_repl=3
# 0. DN: 192.168.1.101:9866 ... 
# 1. DN: 192.168.1.102:9866 ...
# 2. DN: 192.168.1.103:9866 ...
```

## 3.2 Développement d'une Application MapReduce

### Structure d'un Projet Maven

```
mon-projet-mapreduce/
├── pom.xml
└── src/
    └── main/
        └── java/
            └── com/
                └── bigdata/
                    ├── AnalyseVentesMapper.java
                    ├── AnalyseVentesReducer.java
                    └── AnalyseVentesDriver.java
```

### pom.xml

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.bigdata</groupId>
  <artifactId>analyse-ventes</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>jar</packaging>

  <properties>
    <hadoop.version>3.3.6</hadoop.version>
    <java.version>11</java.version>
  </properties>

  <dependencies>
    <dependency>
      <groupId>org.apache.hadoop</groupId>
      <artifactId>hadoop-client</artifactId>
      <version>${hadoop.version}</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <artifactId>maven-assembly-plugin</artifactId>
        <configuration>
          <archive>
            <manifest>
              <mainClass>com.bigdata.AnalyseVentesDriver</mainClass>
            </manifest>
          </archive>
          <descriptorRefs>
            <descriptorRef>jar-with-dependencies</descriptorRef>
          </descriptorRefs>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

### Mapper

```java
// AnalyseVentesMapper.java
package com.bigdata;

import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.Mapper;
import java.io.IOException;

public class AnalyseVentesMapper extends Mapper<LongWritable, Text, Text, DoubleWritable> {

    private Text categorie = new Text();
    private DoubleWritable montant = new DoubleWritable();

    @Override
    public void map(LongWritable key, Text value, Context context)
            throws IOException, InterruptedException {
        
        String ligne = value.toString();
        
        // Ignorer l'en-tête CSV
        if (ligne.startsWith("id") || ligne.trim().isEmpty()) {
            return;
        }
        
        try {
            // Format CSV: id,date,categorie,produit,quantite,prix_unitaire
            String[] champs = ligne.split(",");
            String cat = champs[2].trim();
            int quantite = Integer.parseInt(champs[4].trim());
            double prix = Double.parseDouble(champs[5].trim());
            double ca = quantite * prix;
            
            categorie.set(cat);
            montant.set(ca);
            context.write(categorie, montant);
            
        } catch (NumberFormatException e) {
            // Incrémenter un compteur pour les lignes malformées
            context.getCounter("Erreurs", "Lignes_invalides").increment(1);
        }
    }
}
```

### Reducer

```java
// AnalyseVentesReducer.java
package com.bigdata;

import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.Reducer;
import java.io.IOException;

public class AnalyseVentesReducer extends Reducer<Text, DoubleWritable, Text, Text> {

    @Override
    public void reduce(Text categorie, Iterable<DoubleWritable> montants, Context context)
            throws IOException, InterruptedException {
        
        double total = 0;
        long count = 0;
        double max = Double.MIN_VALUE;
        double min = Double.MAX_VALUE;
        
        for (DoubleWritable m : montants) {
            double val = m.get();
            total += val;
            count++;
            if (val > max) max = val;
            if (val < min) min = val;
        }
        
        double moyenne = count > 0 ? total / count : 0;
        
        String stats = String.format(
            "Total=%.2f€ | Transactions=%d | Moyenne=%.2f€ | Min=%.2f€ | Max=%.2f€",
            total, count, moyenne, min, max
        );
        
        context.write(categorie, new Text(stats));
    }
}
```

### Driver (Point d'Entrée)

```java
// AnalyseVentesDriver.java
package com.bigdata;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class AnalyseVentesDriver {

    public static void main(String[] args) throws Exception {
        
        if (args.length != 2) {
            System.err.println("Usage: AnalyseVentesDriver <input> <output>");
            System.exit(1);
        }

        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "Analyse des Ventes par Categorie");

        job.setJarByClass(AnalyseVentesDriver.class);
        job.setMapperClass(AnalyseVentesMapper.class);
        job.setReducerClass(AnalyseVentesReducer.class);

        // Types de sortie du Mapper
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(DoubleWritable.class);

        // Types de sortie du Reducer
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);

        // Nombre de Reducers (à adapter selon le cluster)
        job.setNumReduceTasks(3);

        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        // Attendre la fin et afficher les compteurs
        boolean success = job.waitForCompletion(true);
        
        if (success) {
            System.out.println("Job terminé avec succès !");
            System.out.println("Lignes invalides : " + 
                job.getCounters().findCounter("Erreurs", "Lignes_invalides").getValue());
        }
        
        System.exit(success ? 0 : 1);
    }
}
```

## 3.3 TP : Application MapReduce WordCount Avancé

### Objectif
Analyser les logs d'un serveur web Apache pour identifier les pages les plus consultées et les codes d'erreur.

### Données d'Entrée (access.log)
```
192.168.1.100 - - [01/Jan/2024:10:00:01 +0000] "GET /index.html HTTP/1.1" 200 2326
192.168.1.101 - - [01/Jan/2024:10:00:02 +0000] "GET /produits.html HTTP/1.1" 200 5432
192.168.1.102 - - [01/Jan/2024:10:00:03 +0000] "GET /admin HTTP/1.1" 403 287
192.168.1.100 - - [01/Jan/2024:10:00:04 +0000] "GET /produits.html HTTP/1.1" 200 5432
192.168.1.103 - - [01/Jan/2024:10:00:05 +0000] "GET /inconnu.html HTTP/1.1" 404 142
```

### Mapper pour Logs Apache
```java
public class LogMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    
    private static final Pattern LOG_PATTERN = Pattern.compile(
        "^(\\S+) \\S+ \\S+ \\[.+\\] \"\\w+ (\\S+) \\S+\" (\\d{3}) \\d+"
    );
    
    public void map(LongWritable key, Text value, Context context)
            throws IOException, InterruptedException {
        
        Matcher matcher = LOG_PATTERN.matcher(value.toString());
        if (matcher.find()) {
            String page = matcher.group(2);
            String statusCode = matcher.group(3);
            
            // Émettre la page avec son code statut
            context.write(new Text(page + " [" + statusCode + "]"), new IntWritable(1));
        }
    }
}
```

### Reducer avec Top-N
```java
public class LogReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    
    public void reduce(Text key, Iterable<IntWritable> values, Context context)
            throws IOException, InterruptedException {
        
        int total = 0;
        for (IntWritable val : values) {
            total += val.get();
        }
        context.write(key, new IntWritable(total));
    }
}
```

### Exécution du TP
```bash
# 1. Compiler le projet
mvn clean package -DskipTests

# 2. Copier les logs vers HDFS
hdfs dfs -mkdir -p /tp/logs/input
hdfs dfs -put access.log /tp/logs/input/

# 3. Lancer le job
hadoop jar target/analyse-logs-1.0-jar-with-dependencies.jar \
  com.bigdata.LogDriver \
  /tp/logs/input \
  /tp/logs/output

# 4. Voir les résultats
hdfs dfs -cat /tp/logs/output/part-r-00000 | sort -t$'\t' -k2 -rn | head -20

# 5. Récupérer les résultats en local
hdfs dfs -getmerge /tp/logs/output/ resultats_logs.txt
```

### Résultats Attendus
```
/index.html [200]       15420
/produits.html [200]    12350
/contact.html [200]     8930
/inconnu.html [404]     2340
/admin [403]            156
```

---

# Chapitre 4 : Apache Spark

## 4.1 Introduction à Apache Spark

### Pourquoi Spark après Hadoop ?

| Critère | Hadoop MapReduce | Apache Spark |
|---------|-----------------|--------------|
| Vitesse | 1x (référence) | 10x à 100x plus rapide |
| Traitement | Batch seulement | Batch + Streaming + ML + Graph |
| Stockage intermédiaire | Disque HDFS | Mémoire RAM (RDD) |
| Facilité de programmation | Verbose (Java) | APIs Python, Scala, R, Java |
| SQL | Via Hive | SparkSQL natif |
| Machine Learning | Mahout (limité) | MLlib intégré |

**Pourquoi Spark est plus rapide ?**
- **In-Memory Processing** : Les données restent en RAM entre les étapes
- **DAG Optimizer** : Planificateur intelligent qui optimise les calculs
- **Lazy Evaluation** : N'exécute que ce qui est nécessaire

### Architecture Spark

```
┌───────────────────────────────────────────────────────────┐
│                    SPARK DRIVER                            │
│         SparkContext │ DAG Scheduler │ Task Scheduler      │
└───────────────────────────┬───────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
┌───────▼──────┐  ┌─────────▼────┐  ┌──────────▼───┐
│  EXECUTOR 1  │  │  EXECUTOR 2  │  │  EXECUTOR 3  │
│  ┌─────────┐ │  │  ┌─────────┐ │  │  ┌─────────┐ │
│  │  Task 1 │ │  │  │  Task 3 │ │  │  │  Task 5 │ │
│  │  Task 2 │ │  │  │  Task 4 │ │  │  │  Task 6 │ │
│  └─────────┘ │  │  └─────────┘ │  │  └─────────┘ │
│  Cache RAM   │  │  Cache RAM   │  │  Cache RAM   │
└──────────────┘  └──────────────┘  └──────────────┘
```

### Concepts Fondamentaux

#### RDD (Resilient Distributed Dataset)
L'abstraction de données fondamentale de Spark. Un RDD est :
- **Resilient** : Tolérant aux pannes (peut être recalculé)
- **Distributed** : Distribué sur le cluster
- **Dataset** : Collection d'éléments

```python
# Création d'un RDD
sc = SparkContext("local[*]", "MonApplication")

# Depuis une liste Python
rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Depuis un fichier HDFS
rdd = sc.textFile("hdfs://localhost:9000/data/ventes.csv")
```

#### DataFrame et Dataset
Abstraction de niveau supérieur avec optimisation via Catalyst :
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("AnalyseVentes") \
    .config("spark.sql.adaptive.enabled", "true") \
    .getOrCreate()

# DataFrame depuis CSV
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("hdfs://localhost:9000/data/ventes.csv")
```

#### Transformations vs Actions

**Transformations (lazy — ne s'exécutent pas immédiatement) :**
```python
# map, filter, flatMap, groupBy, join, union, distinct...
df_filtre = df.filter(df.montant > 1000)
df_groupe = df_filtre.groupBy("region")
```

**Actions (déclenchent l'exécution) :**
```python
# collect, count, show, save, take, first...
df_groupe.count()    # Déclenche le calcul
df_groupe.show()     # Déclenche le calcul
df_groupe.write.csv("/output")  # Déclenche le calcul
```

## 4.2 APIs Spark en Pratique

### PySpark — Analyse Complète

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import *
from pyspark.sql.window import Window

# Initialisation de la session
spark = SparkSession.builder \
    .appName("Analyse Ventes E-Commerce") \
    .master("local[*]") \
    .config("spark.executor.memory", "2g") \
    .config("spark.driver.memory", "1g") \
    .getOrCreate()

# Schéma explicite pour de meilleures performances
schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("date", DateType(), True),
    StructField("client_id", IntegerType(), True),
    StructField("produit", StringType(), True),
    StructField("categorie", StringType(), True),
    StructField("quantite", IntegerType(), True),
    StructField("prix", DoubleType(), True),
    StructField("region", StringType(), True)
])

# Chargement des données
df = spark.read \
    .schema(schema) \
    .option("dateFormat", "yyyy-MM-dd") \
    .csv("hdfs://localhost:9000/data/ventes.csv", header=True)

print(f"Nombre de lignes : {df.count():,}")
df.printSchema()
df.show(5)

# ─── ANALYSE 1 : CA par Catégorie et Région ───
print("\n=== Chiffre d'Affaires par Catégorie et Région ===")
ca_analyse = df.withColumn("ca", F.col("quantite") * F.col("prix")) \
    .groupBy("categorie", "region") \
    .agg(
        F.sum("ca").alias("ca_total"),
        F.count("id").alias("nb_transactions"),
        F.avg("ca").alias("ca_moyen"),
        F.max("ca").alias("ca_max")
    ) \
    .orderBy(F.desc("ca_total"))

ca_analyse.show(20)

# ─── ANALYSE 2 : Évolution Mensuelle ───
print("\n=== Évolution Mensuelle des Ventes ===")
evolution_mensuelle = df.withColumn("ca", F.col("quantite") * F.col("prix")) \
    .withColumn("mois", F.date_format("date", "yyyy-MM")) \
    .groupBy("mois") \
    .agg(F.sum("ca").alias("ca_mensuel")) \
    .orderBy("mois")

evolution_mensuelle.show()

# ─── ANALYSE 3 : Top 10 Produits ───
print("\n=== Top 10 Produits par CA ===")
top_produits = df.withColumn("ca", F.col("quantite") * F.col("prix")) \
    .groupBy("produit", "categorie") \
    .agg(F.sum("ca").alias("ca_total")) \
    .orderBy(F.desc("ca_total")) \
    .limit(10)

top_produits.show()

# ─── ANALYSE 4 : Fenêtres et Ranking ───
print("\n=== Classement des Produits par Catégorie ===")
window_categorie = Window.partitionBy("categorie").orderBy(F.desc("ca_total"))

top_par_categorie = df.withColumn("ca", F.col("quantite") * F.col("prix")) \
    .groupBy("produit", "categorie") \
    .agg(F.sum("ca").alias("ca_total")) \
    .withColumn("rang", F.rank().over(window_categorie)) \
    .filter(F.col("rang") <= 3) \
    .orderBy("categorie", "rang")

top_par_categorie.show()

# ─── SPARK SQL ───
df.createOrReplaceTempView("ventes")

resultats_sql = spark.sql("""
    SELECT 
        region,
        categorie,
        ROUND(SUM(quantite * prix), 2) AS ca_total,
        COUNT(*) AS nb_transactions,
        ROUND(AVG(quantite * prix), 2) AS ca_moyen
    FROM ventes
    WHERE prix > 0 AND quantite > 0
    GROUP BY region, categorie
    HAVING SUM(quantite * prix) > 10000
    ORDER BY ca_total DESC
""")

resultats_sql.show()

# ─── MACHINE LEARNING avec MLlib ───
from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.regression import LinearRegression
from pyspark.ml import Pipeline

print("\n=== Prédiction du CA avec LinearRegression ===")

# Encoder les catégories
indexer = StringIndexer(inputCol="categorie", outputCol="categorie_index")

# Assembler les features
assembler = VectorAssembler(
    inputCols=["categorie_index", "quantite"],
    outputCol="features"
)

# Modèle de régression
lr = LinearRegression(featuresCol="features", labelCol="ca", maxIter=10)

# Pipeline
pipeline = Pipeline(stages=[indexer, assembler, lr])

# Préparer les données
ml_data = df.withColumn("ca", F.col("quantite") * F.col("prix")) \
    .na.drop()

train_data, test_data = ml_data.randomSplit([0.8, 0.2], seed=42)

# Entraîner
model = pipeline.fit(train_data)

# Prédictions
predictions = model.transform(test_data)
predictions.select("produit", "quantite", "ca", "prediction").show(10)

# ─── SAUVEGARDE ───
ca_analyse.write \
    .mode("overwrite") \
    .partitionBy("region") \
    .parquet("hdfs://localhost:9000/output/ca_par_region_categorie")

print("Analyse terminée. Résultats sauvegardés en format Parquet partitionné.")
spark.stop()
```

### Spark Streaming avec Kafka

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("StreamingVentes") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0") \
    .getOrCreate()

# Lire depuis Kafka
df_stream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "ventes-temps-reel") \
    .option("startingOffsets", "latest") \
    .load()

# Schéma du message JSON
schema_vente = StructType([
    StructField("produit", StringType()),
    StructField("montant", DoubleType()),
    StructField("region", StringType()),
    StructField("timestamp", TimestampType())
])

# Parser les messages JSON
df_parsed = df_stream \
    .select(F.from_json(F.col("value").cast("string"), schema_vente).alias("data")) \
    .select("data.*")

# Agrégation sur une fenêtre de 5 minutes
df_aggregate = df_parsed \
    .withWatermark("timestamp", "10 minutes") \
    .groupBy(
        F.window("timestamp", "5 minutes"),
        "region"
    ) \
    .agg(
        F.sum("montant").alias("ca_5min"),
        F.count("*").alias("nb_ventes_5min")
    )

# Écrire les résultats (ici en console pour le TP)
query = df_aggregate.writeStream \
    .outputMode("update") \
    .format("console") \
    .option("truncate", False) \
    .trigger(processingTime="30 seconds") \
    .start()

query.awaitTermination()
```

## 4.3 TP : Analyse de Données avec Spark

### Objectif du TP
Analyser un dataset de 10 millions de transactions e-commerce pour extraire des insights business.

### Étape 1 : Préparation de l'Environnement

```bash
# Installation de PySpark
pip install pyspark==3.5.0 pandas matplotlib

# Vérification
python -c "import pyspark; print(pyspark.__version__)"

# Lancer le shell interactif PySpark
pyspark --master local[4] --driver-memory 4g
```

### Étape 2 : Génération de Données de Test

```python
# generate_data.py
import random
import csv
from datetime import datetime, timedelta

produits = {
    "Électronique": ["Smartphone", "Laptop", "Tablette", "Écouteurs", "Montre Connectée"],
    "Vêtements": ["T-Shirt", "Jean", "Robe", "Veste", "Sneakers"],
    "Alimentaire": ["Café Premium", "Chocolat Bio", "Huile d'Olive", "Vin", "Fromage"],
    "Sport": ["Vélo", "Tapis de Course", "Haltères", "Yoga Mat", "Casque Vélo"]
}
regions = ["Île-de-France", "PACA", "Occitanie", "Grand Est", "Bretagne", "Nouvelle-Aquitaine"]

with open("ventes_10M.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "date", "client_id", "produit", "categorie", "quantite", "prix", "region"])
    
    date_debut = datetime(2023, 1, 1)
    for i in range(10_000_000):
        categorie = random.choice(list(produits.keys()))
        produit = random.choice(produits[categorie])
        date = date_debut + timedelta(days=random.randint(0, 364))
        writer.writerow([
            i + 1,
            date.strftime("%Y-%m-%d"),
            random.randint(1, 500_000),
            produit,
            categorie,
            random.randint(1, 10),
            round(random.uniform(5.99, 2999.99), 2),
            random.choice(regions)
        ])

print("Données générées : ventes_10M.csv")
```

### Étape 3 : Analyse avec Spark

```bash
# Mettre les données dans HDFS
hdfs dfs -mkdir -p /tp/spark/input
hdfs dfs -put ventes_10M.csv /tp/spark/input/

# Lancer l'analyse Spark
spark-submit \
  --master local[*] \
  --driver-memory 4g \
  --executor-memory 2g \
  analyse_ventes.py /tp/spark/input/ventes_10M.csv /tp/spark/output
```

### Résultats Attendus

```
=== Performance Spark vs MapReduce ===
Volume de données : 10 000 000 lignes
MapReduce (estimé) : ~8-15 minutes
Spark (observé)    : ~45-90 secondes
Gain de vitesse    : ~10x-20x

=== Top 3 Catégories par CA ===
+---------------+------------------+-------------------+
|categorie      |ca_total          |nb_transactions    |
+---------------+------------------+-------------------+
|Électronique   |7,234,891,234.50  |2,487,234          |
|Sport          |3,892,341,123.20  |2,503,891          |
|Vêtements      |1,234,891,023.80  |2,498,234          |
+---------------+------------------+-------------------+
```

---

# Chapitre 5 : NoSQL

## 5.1 Introduction aux Bases de Données NoSQL

### Pourquoi NoSQL ?

Le modèle relationnel a des limites face au Big Data :
- **Scalabilité horizontale difficile** : Les BDD SQL scalent verticalement (+ de RAM, + de CPU)
- **Schéma rigide** : Difficile d'intégrer des données semi-structurées ou non-structurées
- **Performances** : Les JOINs sur des milliards de lignes sont prohibitifs
- **CAP Theorem** : Impossible d'avoir à la fois Consistance, Disponibilité et Tolérance au partitionnement

### Le Théorème CAP

```
         Consistance (C)
              △
             / \
            /   \
           /     \
          /  RDBMS \
         /    MySQL  \
        /   Postgres   \
       /_______________\
      /                 \
     /    NoSQL          \
    /                     \
Disponibilité ─────────── Tolérance au
     (A)                  Partitionnement (P)
    Cassandra           HBase, MongoDB
    CouchDB             Redis
```

### Les 4 Familles NoSQL

#### 1. Bases Clé-Valeur
**Exemples :** Redis, DynamoDB, Riak

```
Clé                    →  Valeur
"session:user:12345"   →  {"token": "abc123", "expire": 3600}
"product:SKU-001"      →  {"name": "iPhone 15", "price": 999.99}
"cache:homepage"       →  "<html>...</html>"
```

**Cas d'usage :** Cache, gestion de sessions, compteurs en temps réel

#### 2. Bases Orientées Documents
**Exemples :** MongoDB, CouchDB, Elasticsearch

```json
{
  "_id": "64a9f1b2c3d4e5f6a7b8c9d0",
  "client": {
    "nom": "Martin",
    "prenom": "Sophie",
    "email": "sophie.martin@email.com",
    "adresse": {
      "rue": "12 rue de la Paix",
      "ville": "Paris",
      "code_postal": "75001"
    }
  },
  "commande": {
    "date": "2024-01-15T14:30:00Z",
    "articles": [
      {"produit": "Laptop Pro", "quantite": 1, "prix": 1299.99},
      {"produit": "Souris Sans Fil", "quantite": 2, "prix": 49.99}
    ],
    "total": 1399.97,
    "statut": "expédiée"
  }
}
```

**Cas d'usage :** CMS, catalogues produits, profils utilisateurs

#### 3. Bases en Colonnes (Wide-Column)
**Exemples :** Apache Cassandra, HBase, Google Bigtable

```
Rowkey  │ Famille:Colonne │ Valeur          │ Timestamp
────────┼─────────────────┼─────────────────┼──────────────────
user001 │ info:nom        │ "Dupont"        │ 2024-01-15 10:00
user001 │ info:email      │ "j@email.com"   │ 2024-01-15 10:00
user001 │ stats:achats    │ 42              │ 2024-01-15 15:30
user001 │ stats:panier    │ 1250.00         │ 2024-01-15 15:30
user002 │ info:nom        │ "Martin"        │ 2024-01-16 09:00
```

**Cas d'usage :** IoT, séries temporelles, logs, analytics

#### 4. Bases de Graphes
**Exemples :** Neo4j, Amazon Neptune, JanusGraph

```
(Alice)─[CONNAIT]→(Bob)
  │                 │
  └─[ACHETE]→      └─[RECOMMANDE]→(Produit X)
  (Produit Y)
```

**Cas d'usage :** Réseaux sociaux, systèmes de recommandation, détection de fraudes

## 5.2 Cassandra — Base de Données Distribuée Haute Disponibilité

### Architecture Cassandra

```
        ┌──────────┐
        │  Client  │
        └────┬─────┘
             │
     ┌───────▼────────────────────────────┐
     │         Ring Cassandra              │
     │                                     │
     │  Node1─────Node2─────Node3          │
     │   │  \   /  │  \  /  │             │
     │   │   \ /   │   \/   │             │
     │  Node6  X  Node4  Node5             │
     │                                     │
     │  Chaque nœud = 1/N des données      │
     │  Pas de maître → Full P2P           │
     └─────────────────────────────────────┘
```

### CQL (Cassandra Query Language)

```sql
-- Créer un keyspace
CREATE KEYSPACE ecommerce
WITH replication = {
  'class': 'NetworkTopologyStrategy',
  'datacenter1': 3
};

USE ecommerce;

-- Créer une table optimisée pour les requêtes
CREATE TABLE commandes_par_client (
  client_id UUID,
  date_commande TIMESTAMP,
  commande_id UUID,
  produits LIST<TEXT>,
  total DECIMAL,
  statut TEXT,
  PRIMARY KEY (client_id, date_commande, commande_id)
) WITH CLUSTERING ORDER BY (date_commande DESC);

-- Insérer des données
INSERT INTO commandes_par_client (
  client_id, date_commande, commande_id, produits, total, statut
) VALUES (
  uuid(), toTimestamp(now()), uuid(),
  ['Laptop', 'Souris'], 1349.98, 'confirmée'
);

-- Requête optimisée (par partition key)
SELECT * FROM commandes_par_client
WHERE client_id = 550e8400-e29b-41d4-a716-446655440000
  AND date_commande > '2024-01-01'
LIMIT 10;
```

### Quand choisir Cassandra ?
- Écriture à haute fréquence (millions/seconde)
- Données de séries temporelles
- Haute disponibilité requise (99.999%)
- Distribution géographique (multi-datacenter)

## 5.3 Redis — Cache In-Memory

### Structures de Données Redis

```bash
# String - Compteur en temps réel
SET vues:article:1234 0
INCR vues:article:1234
GET vues:article:1234  # → 1

# Hash - Profil utilisateur
HSET user:1001 nom "Alice" age 30 ville "Paris"
HGET user:1001 nom  # → Alice
HGETALL user:1001   # → tous les champs

# List - File de messages
LPUSH notifications:user:1001 "Votre commande est expédiée"
RPOP notifications:user:1001

# Set - Gestion des sessions actives
SADD sessions:actives "sess_abc123"
SISMEMBER sessions:actives "sess_abc123"  # → 1 (existe)
SMEMBERS sessions:actives

# Sorted Set - Classement temps réel
ZADD leaderboard 9500 "joueur_alice"
ZADD leaderboard 8200 "joueur_bob"
ZREVRANGE leaderboard 0 9 WITHSCORES  # Top 10

# TTL - Expiration automatique (cache)
SET cache:produit:1234 '{"nom":"Laptop","prix":999}' EX 3600
TTL cache:produit:1234  # → 3599 secondes restantes
```

---

# Chapitre 6 : HBase & MongoDB

## 6.1 Apache HBase

### Qu'est-ce que HBase ?

HBase est une base de données NoSQL orientée colonnes, construite sur HDFS. Inspirée de Google Bigtable, elle permet l'accès aléatoire en temps réel à de très grands ensembles de données.

### Modèle de Données HBase

```
Table: capteurs_iot

RowKey          │ CF: mesures              │ CF: meta
────────────────┼──────────────────────────┼─────────────────
capteur_001     │ temp: 23.5              │ localisation: Lyon
2024-01-15T10:00│ humidite: 65.2          │ type: DHT22
                │ pression: 1013.25       │ version: 2.1
────────────────┼──────────────────────────┼─────────────────
capteur_002     │ temp: 18.9              │ localisation: Paris
2024-01-15T10:01│ humidite: 72.1          │ type: BME280
                │ co2: 412                │ version: 3.0
```

**Concepts clés :**
- **RowKey** : Identifiant unique de la ligne — doit être conçu soigneusement pour éviter les "hot spots"
- **Column Family** : Groupe de colonnes, défini à la création de la table
- **Cell** : Intersection RowKey + Column Family + Qualifier + Timestamp
- **Versioning** : HBase conserve plusieurs versions d'une cellule par timestamp

### Architecture HBase

```
┌─────────────────────────────────────────────────────────┐
│                    HMASTER                               │
│  Gère la topologie, équilibrage de charge, compaction   │
└───────────────────────────┬─────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
┌───────▼───────┐  ┌────────▼──────┐  ┌────────▼──────┐
│  RegionServer │  │  RegionServer │  │  RegionServer │
│  ┌──────────┐ │  │  ┌──────────┐│  │  ┌──────────┐ │
│  │ Region 1 │ │  │  │ Region 3 ││  │  │ Region 5 │ │
│  │ MemStore │ │  │  │ MemStore ││  │  │ MemStore │ │
│  │ HFile    │ │  │  │ HFile    ││  │  │ HFile    │ │
│  └──────────┘ │  │  └──────────┘│  │  └──────────┘ │
└───────────────┘  └──────────────┘  └──────────────┘
                            │
         ┌─────────────────────────────────┐
         │              HDFS               │
         │  (Stockage persistant des HFiles)│
         └─────────────────────────────────┘
```

### Opérations HBase avec l'API Java

```java
import org.apache.hadoop.hbase.*;
import org.apache.hadoop.hbase.client.*;
import org.apache.hadoop.hbase.util.Bytes;

public class HBaseExemple {
    
    public static void main(String[] args) throws Exception {
        Configuration conf = HBaseConfiguration.create();
        conf.set("hbase.zookeeper.quorum", "localhost");
        conf.set("hbase.zookeeper.property.clientPort", "2181");
        
        Connection connection = ConnectionFactory.createConnection(conf);
        Admin admin = connection.getAdmin();
        
        // ─── CRÉER UNE TABLE ───
        TableName tableName = TableName.valueOf("capteurs_iot");
        
        if (!admin.tableExists(tableName)) {
            HTableDescriptor tableDescriptor = new HTableDescriptor(tableName);
            tableDescriptor.addFamily(new HColumnDescriptor("mesures").setMaxVersions(5));
            tableDescriptor.addFamily(new HColumnDescriptor("meta"));
            admin.createTable(tableDescriptor);
            System.out.println("Table créée : " + tableName);
        }
        
        Table table = connection.getTable(tableName);
        
        // ─── INSÉRER DES DONNÉES ───
        String rowKey = "capteur_001|2024-01-15T10:00:00";
        Put put = new Put(Bytes.toBytes(rowKey));
        put.addColumn(Bytes.toBytes("mesures"), Bytes.toBytes("temperature"), 
                      Bytes.toBytes("23.5"));
        put.addColumn(Bytes.toBytes("mesures"), Bytes.toBytes("humidite"), 
                      Bytes.toBytes("65.2"));
        put.addColumn(Bytes.toBytes("meta"), Bytes.toBytes("localisation"), 
                      Bytes.toBytes("Lyon"));
        table.put(put);
        
        // ─── LIRE UNE LIGNE ───
        Get get = new Get(Bytes.toBytes(rowKey));
        Result result = table.get(get);
        
        byte[] temp = result.getValue(Bytes.toBytes("mesures"), Bytes.toBytes("temperature"));
        System.out.println("Température : " + Bytes.toString(temp));
        
        // ─── SCAN (LECTURE PLAGE) ───
        Scan scan = new Scan();
        scan.withStartRow(Bytes.toBytes("capteur_001|2024-01-15T00:00:00"));
        scan.withStopRow(Bytes.toBytes("capteur_001|2024-01-15T23:59:59"));
        scan.addColumn(Bytes.toBytes("mesures"), Bytes.toBytes("temperature"));
        
        ResultScanner scanner = table.getScanner(scan);
        System.out.println("\n=== Températures de la journée ===");
        for (Result r : scanner) {
            System.out.println(
                Bytes.toString(r.getRow()) + " → " +
                Bytes.toString(r.getValue(Bytes.toBytes("mesures"), Bytes.toBytes("temperature")))
            );
        }
        scanner.close();
        
        // ─── SUPPRIMER ───
        Delete delete = new Delete(Bytes.toBytes(rowKey));
        table.delete(delete);
        
        table.close();
        connection.close();
    }
}
```

### HBase Shell — Commandes Essentielles

```bash
# Démarrer le shell HBase
hbase shell

# Créer une table
create 'capteurs_iot', {NAME => 'mesures', VERSIONS => 5}, {NAME => 'meta'}

# Lister les tables
list

# Insérer des données
put 'capteurs_iot', 'capteur_001|2024-01-15T10:00', 'mesures:temp', '23.5'
put 'capteurs_iot', 'capteur_001|2024-01-15T10:00', 'mesures:humidite', '65.2'
put 'capteurs_iot', 'capteur_001|2024-01-15T10:00', 'meta:localisation', 'Lyon'

# Lire une ligne
get 'capteurs_iot', 'capteur_001|2024-01-15T10:00'

# Scanner une plage
scan 'capteurs_iot', {STARTROW => 'capteur_001|2024-01-15', STOPROW => 'capteur_001|2024-01-16'}

# Compter les lignes
count 'capteurs_iot'

# Supprimer une cellule
delete 'capteurs_iot', 'capteur_001|2024-01-15T10:00', 'mesures:temp'

# Infos sur la table
describe 'capteurs_iot'

# Statistiques de la région
status 'detailed'
```

### Conception du RowKey — Bonnes Pratiques

```
❌ MAUVAIS RowKey (créera un "hot spot" sur un seul RegionServer)
capteur_001|20240115100000
capteur_001|20240115100001
capteur_001|20240115100002
→ Toutes les écritures vont sur la même région !

✅ BON RowKey (distribué)
Option 1 - Salting (préfixe aléatoire)
3|capteur_001|20240115100000
1|capteur_001|20240115100001
7|capteur_001|20240115100002

Option 2 - Inversion du timestamp
capteur_001|9999999999-timestamp_inversé
→ Données récentes au début, lectures chronologiques inversées
```

## 6.2 MongoDB

### Introduction

MongoDB est la base de données NoSQL orientée documents la plus populaire. Elle stocke les données en BSON (Binary JSON) et offre une API riche de requêtes.

### Installation MongoDB

```bash
# Ubuntu 22.04
wget -qO - https://www.mongodb.org/static/pgp/server-7.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | \
  sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo systemctl start mongod
sudo systemctl enable mongod
```

### Opérations CRUD MongoDB

```javascript
// Connexion au shell MongoDB
mongosh

// Créer/Utiliser une base de données
use ecommerce_db

// ─── CREATE ───
db.clients.insertOne({
  nom: "Dupont",
  prenom: "Jean",
  email: "jean.dupont@email.com",
  age: 35,
  ville: "Paris",
  commandes: [],
  tags: ["premium", "fidele"],
  date_inscription: new Date()
})

// Insérer plusieurs documents
db.produits.insertMany([
  { nom: "Laptop Pro X", categorie: "Électronique", prix: 1299.99, stock: 150 },
  { nom: "Clavier Mécanique", categorie: "Électronique", prix: 149.99, stock: 500 },
  { nom: "Tapis de Souris XXL", categorie: "Accessoires", prix: 29.99, stock: 1000 }
])

// ─── READ ───
// Trouver tous les documents
db.produits.find()

// Avec filtres
db.produits.find({ categorie: "Électronique", prix: { $lt: 500 } })

// Projection (sélection de champs)
db.produits.find(
  { categorie: "Électronique" },
  { nom: 1, prix: 1, _id: 0 }
)

// Tri, limite, skip (pagination)
db.produits.find()
  .sort({ prix: -1 })   // Décroissant
  .skip(10)             // Sauter les 10 premiers
  .limit(5)             // Retourner 5 résultats

// Requêtes avancées
db.clients.find({
  age: { $gte: 25, $lte: 40 },      // Entre 25 et 40 ans
  ville: { $in: ["Paris", "Lyon"] }, // Dans ces villes
  tags: "premium"                    // Contient ce tag
})

// ─── UPDATE ───
// Mettre à jour un document
db.produits.updateOne(
  { nom: "Laptop Pro X" },
  { 
    $set: { prix: 1199.99, solde: true },
    $inc: { stock: -10 }  // Décrémenter le stock
  }
)

// Mettre à jour plusieurs documents
db.clients.updateMany(
  { ville: "Paris" },
  { $push: { tags: "region-idf" } }  // Ajouter un tag
)

// ─── DELETE ───
db.produits.deleteOne({ nom: "Tapis de Souris XXL" })
db.produits.deleteMany({ stock: { $lte: 0 } })
```

### Agrégation MongoDB — Le Cœur de l'Analyse

```javascript
// Pipeline d'agrégation : Analyse des Ventes par Catégorie
db.commandes.aggregate([
  // Étape 1 : Filtrer les commandes de 2024
  { $match: { 
    date: { $gte: new Date("2024-01-01"), $lte: new Date("2024-12-31") },
    statut: "livree"
  }},
  
  // Étape 2 : Déconstruire le tableau d'articles
  { $unwind: "$articles" },
  
  // Étape 3 : Ajouter un champ calculé
  { $addFields: {
    ca_article: { $multiply: ["$articles.quantite", "$articles.prix"] }
  }},
  
  // Étape 4 : Regrouper par catégorie
  { $group: {
    _id: "$articles.categorie",
    ca_total: { $sum: "$ca_article" },
    nb_transactions: { $sum: 1 },
    ca_moyen: { $avg: "$ca_article" },
    produit_le_plus_vendu: { $first: "$articles.nom" }
  }},
  
  // Étape 5 : Trier par CA décroissant
  { $sort: { ca_total: -1 } },
  
  // Étape 6 : Renommer les champs de sortie
  { $project: {
    categorie: "$_id",
    ca_total: { $round: ["$ca_total", 2] },
    nb_transactions: 1,
    ca_moyen: { $round: ["$ca_moyen", 2] },
    _id: 0
  }}
])
```

### Index MongoDB — Performance

```javascript
// Index simple
db.produits.createIndex({ categorie: 1 })

// Index composé (pour les requêtes sur categorie ET prix)
db.produits.createIndex({ categorie: 1, prix: -1 })

// Index unique
db.clients.createIndex({ email: 1 }, { unique: true })

// Index texte pour la recherche full-text
db.produits.createIndex({ 
  nom: "text", 
  description: "text" 
}, {
  weights: { nom: 10, description: 1 }  // Pondération
})

// Utiliser la recherche textuelle
db.produits.find({ $text: { $search: "laptop gaming" } })

// Index TTL (expiration automatique)
db.sessions.createIndex(
  { created_at: 1 }, 
  { expireAfterSeconds: 86400 }  // Expire après 24h
)

// Voir les index
db.produits.getIndexes()

// Analyser une requête avec EXPLAIN
db.produits.find({ categorie: "Électronique" }).explain("executionStats")
```

### PyMongo — MongoDB avec Python

```python
from pymongo import MongoClient, ASCENDING, DESCENDING
from datetime import datetime, timedelta
import json

# Connexion
client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce_db"]
commandes = db["commandes"]

# ─── Exemple : Système de Recommandation Simple ───
def recommander_produits(client_id, limite=5):
    """
    Recommande des produits basés sur l'historique d'achats.
    Algorithme : Collaborative Filtering simplifié
    """
    # 1. Trouver les produits achetés par ce client
    pipeline_client = [
        {"$match": {"client_id": client_id}},
        {"$unwind": "$articles"},
        {"$group": {"_id": "$articles.categorie"}}
    ]
    categories_client = [r["_id"] for r in commandes.aggregate(pipeline_client)]
    
    # 2. Trouver les best-sellers dans ces catégories
    pipeline_recommandations = [
        {"$unwind": "$articles"},
        {"$match": {"articles.categorie": {"$in": categories_client}}},
        {"$group": {
            "_id": "$articles.nom",
            "nb_achats": {"$sum": 1},
            "categorie": {"$first": "$articles.categorie"}
        }},
        {"$sort": {"nb_achats": -1}},
        {"$limit": limite}
    ]
    
    return list(commandes.aggregate(pipeline_recommandations))

recommandations = recommander_produits("client_12345")
print(json.dumps(recommandations, indent=2, default=str))
```

## 6.3 TP : HBase et MongoDB

### TP HBase — Système de Monitoring IoT

**Scénario :** Stocker et analyser les mesures de 10 000 capteurs IoT qui envoient des données toutes les 30 secondes.

```python
# hbase_iot.py
import happybase
import time
import random
import struct
from datetime import datetime, timedelta

# Connexion HBase
connection = happybase.Connection('localhost', port=9090)
connection.open()

# Créer la table
table_name = b'capteurs_iot'
if table_name not in connection.tables():
    connection.create_table(
        table_name,
        {
            b'mesures': dict(max_versions=10, compression='SNAPPY'),
            b'meta': dict(max_versions=1)
        }
    )
    print("Table créée : capteurs_iot")

table = connection.table(table_name)

# ─── Ingestion de Données IoT ───
def ingerer_mesures(nb_capteurs=100, nb_mesures=1000):
    """Simule l'ingestion de données IoT."""
    batch = table.batch(batch_size=500)
    
    for i in range(nb_mesures):
        capteur_id = f"capteur_{random.randint(1, nb_capteurs):05d}"
        timestamp = datetime.now() - timedelta(seconds=random.randint(0, 86400))
        
        # RowKey conçu pour éviter les hot spots
        # Format : salt|capteur_id|timestamp_inversé
        salt = hash(capteur_id) % 10
        ts_inverse = 99999999999 - int(timestamp.timestamp())
        row_key = f"{salt}|{capteur_id}|{ts_inverse:011d}".encode()
        
        mesures = {
            b'mesures:temperature': str(round(random.uniform(-10, 45), 2)).encode(),
            b'mesures:humidite': str(round(random.uniform(30, 95), 1)).encode(),
            b'mesures:pression': str(round(random.uniform(970, 1050), 2)).encode(),
            b'mesures:co2': str(random.randint(350, 1500)).encode(),
            b'meta:localisation': random.choice([b'Lyon', b'Paris', b'Marseille', b'Bordeaux']),
            b'meta:actif': b'true'
        }
        
        batch.put(row_key, mesures)
    
    batch.send()
    print(f"Ingestion terminée : {nb_mesures} mesures pour {nb_capteurs} capteurs")

# ─── Requêtes Analytiques ───
def analyser_capteur(capteur_id, periode_heures=24):
    """Récupère les mesures récentes d'un capteur."""
    salt = hash(capteur_id) % 10
    now = int(time.time())
    ts_debut_inverse = 99999999999 - now
    ts_fin_inverse = 99999999999 - (now - periode_heures * 3600)
    
    start_row = f"{salt}|{capteur_id}|{ts_debut_inverse:011d}".encode()
    stop_row = f"{salt}|{capteur_id}|{ts_fin_inverse:011d}".encode()
    
    temperatures = []
    for key, data in table.scan(row_start=start_row, row_stop=stop_row):
        if b'mesures:temperature' in data:
            temperatures.append(float(data[b'mesures:temperature']))
    
    if temperatures:
        return {
            "capteur": capteur_id,
            "nb_mesures": len(temperatures),
            "temp_min": min(temperatures),
            "temp_max": max(temperatures),
            "temp_moyenne": round(sum(temperatures) / len(temperatures), 2)
        }

# Exécution du TP
ingerer_mesures(nb_capteurs=100, nb_mesures=5000)
stats = analyser_capteur("capteur_00042")
print(f"\nStatistiques capteur_00042 : {stats}")

connection.close()
```

### TP MongoDB — Plateforme E-Commerce

```python
# mongodb_ecommerce.py
from pymongo import MongoClient, ASCENDING, DESCENDING
from pymongo.errors import BulkWriteError
from datetime import datetime, timedelta
import random
import string

client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce_tp"]

# ─── Setup des collections et index ───
db.clients.create_index([("email", ASCENDING)], unique=True)
db.produits.create_index([("categorie", ASCENDING), ("prix", DESCENDING)])
db.produits.create_index([("nom", "text"), ("description", "text")])
db.commandes.create_index([("client_id", ASCENDING), ("date", DESCENDING)])

# ─── Génération de données réalistes ───
categories = {
    "Électronique": [
        ("Smartphone Galaxy S24", 899.99),
        ("Laptop Dell XPS 15", 1499.99),
        ("Tablette iPad Pro", 1099.99),
        ("Écouteurs Sony WH-1000XM5", 349.99)
    ],
    "Vêtements": [
        ("Jean Slim Bleu", 79.99),
        ("T-Shirt Col V", 29.99),
        ("Veste en Cuir", 299.99)
    ],
    "Sport": [
        ("Tapis de Course ProFit 3000", 1299.99),
        ("Vélo Électrique CityRider", 2499.99),
        ("Yoga Mat Premium", 89.99)
    ]
}

# Insérer des produits
produits_docs = []
for cat, items in categories.items():
    for nom, prix in items:
        produits_docs.append({
            "nom": nom,
            "categorie": cat,
            "prix": prix,
            "stock": random.randint(10, 500),
            "note_moyenne": round(random.uniform(3.5, 5.0), 1),
            "nb_avis": random.randint(10, 5000),
            "date_ajout": datetime.now() - timedelta(days=random.randint(0, 365))
        })

db.produits.insert_many(produits_docs)
print(f"Produits insérés : {len(produits_docs)}")

# Insérer des clients
villes = ["Paris", "Lyon", "Marseille", "Bordeaux", "Nantes", "Toulouse"]
clients_docs = []
for i in range(1000):
    clients_docs.append({
        "client_id": f"C{i+1:05d}",
        "nom": f"Client_{i+1}",
        "email": f"client{i+1}@test.com",
        "ville": random.choice(villes),
        "age": random.randint(18, 70),
        "premium": random.random() > 0.7,
        "date_inscription": datetime.now() - timedelta(days=random.randint(30, 1095))
    })

db.clients.insert_many(clients_docs)
print(f"Clients insérés : {len(clients_docs)}")

# ─── Requêtes Analytics ───
print("\n=== TOP 3 PRODUITS PAR CATÉGORIE (CA) ===")
pipeline = [
    {"$unwind": "$articles"},
    {"$group": {
        "_id": {"categorie": "$articles.categorie", "produit": "$articles.nom"},
        "ca_total": {"$sum": {"$multiply": ["$articles.quantite", "$articles.prix_unitaire"]}},
        "nb_ventes": {"$sum": "$articles.quantite"}
    }},
    {"$sort": {"ca_total": -1}},
    {"$group": {
        "_id": "$_id.categorie",
        "top_produits": {"$push": {
            "produit": "$_id.produit",
            "ca": "$ca_total",
            "nb_ventes": "$nb_ventes"
        }}
    }},
    {"$project": {
        "categorie": "$_id",
        "top3": {"$slice": ["$top_produits", 3]},
        "_id": 0
    }}
]

for r in db.commandes.aggregate(pipeline):
    print(f"\nCatégorie: {r.get('categorie', 'N/A')}")
    for p in r.get("top3", []):
        print(f"  {p.get('produit', 'N/A')}: {p.get('ca', 0):.2f}€ ({p.get('nb_ventes', 0)} ventes)")

print("\n=== CLIENTS PREMIUM PAR VILLE ===")
pipeline_clients = [
    {"$match": {"premium": True}},
    {"$group": {
        "_id": "$ville",
        "nb_premium": {"$sum": 1},
        "age_moyen": {"$avg": "$age"}
    }},
    {"$sort": {"nb_premium": -1}},
    {"$project": {
        "ville": "$_id",
        "nb_premium": 1,
        "age_moyen": {"$round": ["$age_moyen", 0]},
        "_id": 0
    }}
]

for r in db.clients.aggregate(pipeline_clients):
    print(f"  {r.get('ville', 'N/A')}: {r.get('nb_premium', 0)} clients premium (âge moyen: {r.get('age_moyen', 0)})")

client.close()
print("\nTP MongoDB terminé.")
```

---

# Chapitre 7 : Big Data & Intelligence Artificielle

## 7.1 La Convergence Big Data & IA

Le Big Data et l'Intelligence Artificielle sont inextricablement liés :

> **"Les données sont le pétrole de l'IA, et l'IA est le moteur qui transforme ce pétrole en valeur."**

```
┌─────────────────────────────────────────────────────────────────┐
│                      CYCLE VERTUEUX                              │
│                                                                   │
│  BIG DATA ────→ Entraîne ────→ MODÈLES IA                       │
│     ↑                              │                             │
│     │                              ↓                             │
│  Nouvelles               Génère des Insights                     │
│  Données ←────── Décisions ←────── & Prédictions                │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

## 7.2 Comment l'IA s'Intègre dans le Workflow Big Data

### Le Pipeline MLOps

```
Données Brutes
    │
    ▼ Feature Engineering (Spark MLlib, Pandas)
Features Préparées
    │
    ▼ Entraînement (Scikit-learn, TensorFlow, PyTorch)
Modèle Entraîné
    │
    ▼ Validation & Tests (MLflow, DVC)
Modèle Validé
    │
    ▼ Déploiement (Kubernetes, FastAPI, SageMaker)
API de Prédiction
    │
    ▼ Monitoring (Prometheus, Grafana, Evidently)
Détection de Dérive
    │
    ▼ Ré-entraînement automatique (boucle)
```

### Spark MLlib pour le Machine Learning Distribué

```python
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import *
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder

spark = SparkSession.builder.appName("MLlib-Classification").getOrCreate()

# Chargement des données (10 millions de transactions)
df = spark.read.parquet("hdfs://localhost:9000/data/transactions/")

# Feature Engineering
indexer_region = StringIndexer(inputCol="region", outputCol="region_idx")
indexer_cat = StringIndexer(inputCol="categorie", outputCol="categorie_idx")

encoder = OneHotEncoder(
    inputCols=["region_idx", "categorie_idx"],
    outputCols=["region_enc", "categorie_enc"]
)

assembler = VectorAssembler(
    inputCols=["region_enc", "categorie_enc", "montant", "nb_articles", "heure"],
    outputCol="features"
)

scaler = StandardScaler(inputCol="features", outputCol="features_scaled")

# Modèle Random Forest
rf = RandomForestClassifier(
    featuresCol="features_scaled",
    labelCol="fraude",
    numTrees=100,
    maxDepth=10,
    seed=42
)

# Pipeline complet
pipeline = Pipeline(stages=[indexer_region, indexer_cat, encoder, assembler, scaler, rf])

# Tuning des hyperparamètres
paramGrid = ParamGridBuilder() \
    .addGrid(rf.numTrees, [50, 100, 200]) \
    .addGrid(rf.maxDepth, [5, 10, 15]) \
    .build()

evaluator = BinaryClassificationEvaluator(labelCol="fraude", metricName="areaUnderROC")

cv = CrossValidator(
    estimator=pipeline,
    estimatorParamMaps=paramGrid,
    evaluator=evaluator,
    numFolds=5,
    parallelism=4
)

# Entraînement
train_data, test_data = df.randomSplit([0.8, 0.2], seed=42)
model = cv.fit(train_data)

# Évaluation
predictions = model.transform(test_data)
auc = evaluator.evaluate(predictions)
print(f"AUC-ROC : {auc:.4f}")

# Importance des features
best_rf = model.bestModel.stages[-1]
feature_importance = sorted(
    zip(assembler.getInputCols(), best_rf.featureImportances),
    key=lambda x: x[1],
    reverse=True
)

print("\n=== Importance des Features ===")
for feature, importance in feature_importance[:10]:
    print(f"  {feature}: {importance:.4f}")

# Sauvegarde du modèle
model.bestModel.write().overwrite().save("hdfs://localhost:9000/models/fraude_detector")
```

## 7.3 Outils IA dans l'Ecosystème Big Data

### MLflow — Tracking des Expériences

```python
import mlflow
import mlflow.sklearn
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, roc_auc_score

mlflow.set_experiment("Détection de Fraudes")

with mlflow.start_run(run_name="GBM_v1"):
    # Paramètres
    params = {
        "n_estimators": 200,
        "max_depth": 6,
        "learning_rate": 0.1,
        "subsample": 0.8
    }
    
    # Entraînement
    model = GradientBoostingClassifier(**params)
    model.fit(X_train, y_train)
    
    # Métriques
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
    
    # Log dans MLflow
    mlflow.log_params(params)
    mlflow.log_metrics({"accuracy": acc, "auc_roc": auc})
    mlflow.sklearn.log_model(model, "model")
    
    print(f"Accuracy: {acc:.4f} | AUC-ROC: {auc:.4f}")
    print(f"Run ID: {mlflow.active_run().info.run_id}")
```

### Apache Kafka + IA Temps Réel

```python
# Système de recommandation en temps réel
from kafka import KafkaConsumer, KafkaProducer
import json
import joblib
import numpy as np

# Charger le modèle pré-entraîné
modele_reco = joblib.load("model_recommendations.pkl")

consumer = KafkaConsumer(
    "clics-utilisateurs",
    bootstrap_servers=["localhost:9092"],
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

print("Système de recommandation démarré...")
for message in consumer:
    clic = message.value
    user_id = clic["user_id"]
    produit_vu = clic["produit_id"]
    
    # Prédiction en temps réel (< 10ms)
    features = extraire_features(user_id, produit_vu)
    recommandations = modele_reco.predict(features)
    
    # Envoyer les recommandations
    producer.send("recommandations", {
        "user_id": user_id,
        "recommandations": recommandations.tolist(),
        "timestamp": clic["timestamp"]
    })
```

## 7.4 LLMs et Big Data — La Révolution Actuelle

### Cas d'Usage des LLMs dans le Big Data

**1. Text-to-SQL / NL2SQL**
```python
# Interroger une base Big Data en langage naturel
from anthropic import Anthropic

client = Anthropic()

def nl_to_sql(question_naturelle: str, schema: str) -> str:
    """Convertit une question naturelle en requête SQL."""
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[{
            "role": "user",
            "content": f"""Tu es un expert SQL Big Data. 
Schéma de la base : {schema}
Question : {question_naturelle}
Génère uniquement la requête SQL optimisée, sans explication."""
        }]
    )
    return response.content[0].text

schema = """
Tables : ventes(id, date, produit, categorie, montant, region)
         clients(id, nom, email, ville, age, premium)
"""
question = "Quels sont les 5 produits qui ont le plus de ventes en Île-de-France ce trimestre ?"
sql = nl_to_sql(question, schema)
print(sql)
```

**2. Analyse Automatique de Rapports**
```python
# Analyser des milliers de documents avec l'IA
import anthropic

client = anthropic.Anthropic()

def analyser_avis_clients(avis: list[str]) -> dict:
    """Analyse le sentiment et extrait les thèmes des avis clients."""
    
    batch_text = "\n---\n".join(avis[:50])  # Batch de 50 avis
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        messages=[{
            "role": "user",
            "content": f"""Analyse ces avis clients et retourne un JSON avec :
- sentiment_global (positif/neutre/négatif)
- score_moyen (0-10)
- themes_positifs (liste)
- themes_negatifs (liste)
- suggestions_amelioration (liste)

Avis :
{batch_text}

Retourne uniquement le JSON, sans texte supplémentaire."""
        }]
    )
    
    import json
    return json.loads(response.content[0].text)

avis = [
    "Livraison rapide, produit conforme à la description. Très satisfait !",
    "Service client décevant, 3 jours pour avoir une réponse.",
    "Excellent rapport qualité-prix, je recommande vivement.",
]

analyse = analyser_avis_clients(avis)
print(json.dumps(analyse, indent=2, ensure_ascii=False))
```

**3. Détection d'Anomalies avec Explication**
```python
def expliquer_anomalie(transaction: dict, contexte: dict) -> str:
    """Utilise un LLM pour expliquer pourquoi une transaction est suspecte."""
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=500,
        messages=[{
            "role": "user",
            "content": f"""En tant qu'analyste fraude, explique en 3 phrases 
pourquoi cette transaction est suspecte :

Transaction : {transaction}
Contexte client (30 derniers jours) : {contexte}

Sois précis et actionnable."""
        }]
    )
    
    return response.content[0].text
```

## 7.5 L'Impact Concret de l'IA sur le Travail Big Data

### Ce que l'IA Change Aujourd'hui

| Tâche Traditionnelle | Avec l'IA | Gain |
|---------------------|-----------|------|
| Rédiger des requêtes SQL | Text-to-SQL (GitHub Copilot, Claude) | -70% de temps |
| Analyser des logs d'erreur | LLMs pour diagnostiquer automatiquement | -60% de temps de debug |
| Écrire de la documentation | Génération automatique (Claude, GPT-4) | -80% de temps |
| Nettoyage de données | AutoML + suggestions intelligentes | -50% de temps |
| Détection d'anomalies | Modèles auto-apprenants | Précision +40% |
| Création de pipelines ETL | AI-assisted coding | -65% de développement |

### Outils IA à Maîtriser pour un Data Engineer

```
Catégorie              Outil                          Usage
───────────────────────────────────────────────────────────────
Coding Assistant     GitHub Copilot, Cursor            Écrire du code Spark/Python
                     Tabnine, Claude in VSCode
                     
Data Platform        Databricks AI Assistant            SQL, notebooks intelligents
                     Snowflake Cortex                   Requêtes NL, anomalies
                     
MLOps                MLflow, DVC, Weights & Biases     Traçabilité des modèles
                     
Monitoring           Grafana + LLM Alerting            Alertes intelligentes
                     
Orchestration        Apache Airflow + AI               Auto-réparation de pipelines
                     Prefect, Dagster
                     
Vector Databases     Pinecone, Weaviate, Milvus        RAG, recherche sémantique
                     Chroma, pgvector
```

## 7.6 Le Futur du Big Data et de l'IA

### Tendances 2025–2030

**1. Data Mesh**
Décentralisation de la propriété des données par domaine métier. Chaque équipe produit publie ses propres "data products".

**2. Lakehouse Universel**
Convergence des Data Lakes, Data Warehouses et bases OLTP dans une architecture unifiée (Apache Iceberg, Delta Lake).

**3. IA Générative dans le Data Engineering**
- Génération automatique de pipelines ETL
- Auto-correction des erreurs de pipeline
- Documentation auto-générée et maintenue

**4. Real-Time Everything**
Latence sub-seconde comme standard, Kafka remplacé par des solutions plus performantes (Redpanda, WarpStream).

**5. Confidential Computing**
Traitement de données sensibles chiffrées même pendant l'analyse (Health, Finance, Legal).

**6. Green Data Engineering**
Optimisation de l'empreinte carbone des clusters Big Data. Apache Spark adopte des optimisations éco-conscientes.

### Compétences du Data Engineer 2025+

```
                    CORE SKILLS
         ┌─────────────────────────────┐
         │  Python │ SQL │ Cloud (AWS/ │
         │  Azure/GCP) │ Linux        │
         └───────────────┬─────────────┘
                         │
            ┌────────────┼────────────┐
            │            │            │
      DATA LAYER    PROCESSING   AI/ML LAYER
      ─────────     ──────────   ──────────
      HDFS/S3       Spark 3.x    MLlib
      Delta Lake    Flink        MLflow
      Iceberg       Kafka        Feature Store
      HBase         dbt          LLM APIs
      MongoDB       Airflow      Vector DB
```

---

# Certifications Recommandées

Les certifications suivantes valorisent les compétences acquises dans ce cours et sont reconnues par l'industrie :

## Certifications Fondamentales

### 1. Cloudera Certified Data Engineer (CDE)
- **Éditeur :** Cloudera
- **Niveau :** Intermédiaire
- **Couvre :** Hadoop, Spark, HDFS, Hive, Kafka
- **Durée de préparation :** 3–6 mois
- **Site :** https://www.cloudera.com/about/training/certification.html
- **Valeur marché :** ★★★★★

### 2. Databricks Certified Associate Developer for Apache Spark
- **Éditeur :** Databricks
- **Niveau :** Débutant-Intermédiaire
- **Couvre :** Spark Core, DataFrames, SparkSQL, MLlib
- **Durée de préparation :** 1–3 mois
- **Site :** https://www.databricks.com/learn/certification/apache-spark-developer-associate
- **Valeur marché :** ★★★★★

### 3. Databricks Certified Data Engineer Professional
- **Éditeur :** Databricks
- **Niveau :** Avancé
- **Couvre :** Architecture Lakehouse, Delta Lake, MLflow, Production
- **Durée de préparation :** 4–6 mois
- **Site :** https://www.databricks.com/learn/certification/data-engineer-professional
- **Valeur marché :** ★★★★★

## Certifications Cloud

### 4. AWS Certified Data Engineer – Associate (DEA-C01)
- **Éditeur :** Amazon Web Services
- **Niveau :** Intermédiaire
- **Couvre :** EMR (Hadoop/Spark sur AWS), S3, Glue, Kinesis, Redshift, DynamoDB
- **Durée de préparation :** 2–4 mois
- **Site :** https://aws.amazon.com/certification/certified-data-engineer-associate/
- **Valeur marché :** ★★★★★

### 5. Google Professional Data Engineer
- **Éditeur :** Google Cloud
- **Niveau :** Avancé
- **Couvre :** BigQuery, Dataflow, Pub/Sub, Dataproc (Hadoop/Spark)
- **Durée de préparation :** 3–5 mois
- **Site :** https://cloud.google.com/certification/data-engineer
- **Valeur marché :** ★★★★★

### 6. Microsoft Azure Data Engineer Associate (DP-203)
- **Éditeur :** Microsoft
- **Niveau :** Intermédiaire
- **Couvre :** Azure Synapse, Data Factory, HDInsight, Databricks on Azure
- **Durée de préparation :** 2–4 mois
- **Site :** https://learn.microsoft.com/en-us/certifications/azure-data-engineer/
- **Valeur marché :** ★★★★☆

## Certifications Spécialisées

### 7. MongoDB Certified Developer Associate (C100DEV)
- **Éditeur :** MongoDB
- **Niveau :** Intermédiaire
- **Couvre :** CRUD, Aggregation, Indexing, Data Modeling, Performance
- **Durée de préparation :** 1–2 mois
- **Site :** https://learn.mongodb.com/pages/certification
- **Valeur marché :** ★★★★☆

### 8. Confluent Certified Developer for Apache Kafka (CCDAK)
- **Éditeur :** Confluent
- **Niveau :** Intermédiaire
- **Couvre :** Kafka Architecture, Producers, Consumers, Streams, Connect
- **Durée de préparation :** 2–3 mois
- **Site :** https://www.confluent.io/certification/
- **Valeur marché :** ★★★★☆

### 9. Cloudera Certified Associate (CCA) - Spark and Hadoop Developer
- **Éditeur :** Cloudera
- **Niveau :** Intermédiaire
- **Couvre :** Spark, HDFS, Sqoop, Hive, Pig, Impala
- **Site :** https://www.cloudera.com/about/training/certification.html
- **Valeur marché :** ★★★★☆

## Parcours de Certification Recommandé

```
DÉBUTANT                    INTERMÉDIAIRE               AVANCÉ
────────                    ──────────────              ──────
                                                        
MongoDB Certified    →    Databricks Spark   →    Databricks Data
Developer                 Developer                Engineer Pro
(1-2 mois)               (2-3 mois)               (4-6 mois)
                                │
                                ▼
                         AWS Data Engineer  →   Google Professional
                         Associate               Data Engineer
                         (2-4 mois)             (3-5 mois)
                                │
                                ▼
                         Confluent Kafka
                         Developer
                         (2-3 mois)
                                │
                                ▼
                         Cloudera Data
                         Engineer
                         (3-6 mois)
```

---

# Ressources et Références

## Documentation Officielle

| Outil | Documentation |
|-------|--------------|
| Apache Hadoop | https://hadoop.apache.org/docs/ |
| Apache Spark | https://spark.apache.org/docs/latest/ |
| Apache HBase | https://hbase.apache.org/book.html |
| Apache Kafka | https://kafka.apache.org/documentation/ |
| MongoDB | https://www.mongodb.com/docs/ |
| Apache Cassandra | https://cassandra.apache.org/doc/ |
| MLflow | https://mlflow.org/docs/ |
| Delta Lake | https://docs.delta.io/ |

## Livres Recommandés

1. **"Designing Data-Intensive Applications"** – Martin Kleppmann (O'Reilly)
   → La bible du Big Data et des systèmes distribués

2. **"Hadoop: The Definitive Guide"** – Tom White (O'Reilly)
   → Référence complète sur Hadoop

3. **"Learning Spark, 2nd Edition"** – Jules Damji et al. (O'Reilly)
   → Spark moderne avec DataFrames et Delta Lake

4. **"Kafka: The Definitive Guide"** – Neha Narkhede et al. (O'Reilly)
   → Architecture et implémentation Kafka

5. **"MongoDB: The Definitive Guide"** – Shannon Bradshaw et al. (O'Reilly)
   → De la modélisation à la production

## Plateformes de Formation

| Plateforme | Contenu | URL |
|-----------|---------|-----|
| Coursera | Spécialisations Big Data (UC San Diego) | https://www.coursera.org |
| edX | MicroMasters en Data Science | https://www.edx.org |
| DataCamp | Python, Spark, Data Engineering | https://www.datacamp.com |
| Databricks Academy | Spark, Delta Lake, MLflow (gratuit) | https://customer-academy.databricks.com |
| A Cloud Guru | AWS/Azure/GCP certifications | https://acloudguru.com |
| Udemy | Cours pratiques à prix réduits | https://www.udemy.com |

## Communautés et Veille

- **Awesome Big Data** (GitHub) : https://github.com/newTendermint/awesome-bigdata
- **Apache Software Foundation** : https://www.apache.org
- **Databricks Engineering Blog** : https://www.databricks.com/blog/engineering
- **Netflix Tech Blog** : https://netflixtechblog.com
- **Uber Engineering Blog** : https://www.uber.com/en-US/blog/engineering/
- **LinkedIn Engineering** : https://engineering.linkedin.com/blog

## Environnements Pratiques Gratuits

| Environnement | Description | URL |
|--------------|-------------|-----|
| Google Colab | PySpark en ligne (GPU gratuit) | https://colab.research.google.com |
| Databricks Community | Cluster Spark gratuit | https://community.cloud.databricks.com |
| MongoDB Atlas | Cluster MongoDB gratuit (512 MB) | https://www.mongodb.com/atlas |
| Confluent Cloud | Kafka cluster gratuit (30 jours) | https://www.confluent.io/confluent-cloud/ |
| GitHub Codespaces | IDE cloud avec Hadoop/Spark | https://github.com/codespaces |

---

## 📌 Résumé et Prochaines Étapes

```
✅ Vous maîtrisez maintenant :
   → L'architecture Big Data et les 5V
   → HDFS : stockage distribué et tolérance aux pannes  
   → MapReduce : parallélisation du calcul
   → Spark : traitement in-memory, SQL, ML, Streaming
   → NoSQL : clé-valeur, documents, colonnes, graphes
   → HBase : base de données temps-réel sur HDFS
   → MongoDB : base documentaire flexible et puissante
   → IA + Big Data : MLOps, LLMs, temps réel

🎯 Prochaines étapes recommandées :
   1. Pratiquer avec Databricks Community Edition (gratuit)
   2. Passer la certification Databricks Spark Associate
   3. Construire un projet end-to-end sur GitHub
   4. Contribuer à un projet Apache open source
   5. Rejoindre des meetups Big Data (Meetup.com)
```

---

*Ce cours est vivant : le domaine Big Data évolue rapidement. Restez à jour via les blogs techniques des GAFAM et les papiers de recherche sur arxiv.org (catégorie cs.DB et cs.DC).*

*Formation réalisée avec ❤️ pour la communauté Data Engineering francophone.*
