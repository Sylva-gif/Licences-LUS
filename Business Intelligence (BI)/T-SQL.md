# 🗄️ Guide Complet T-SQL — Maîtriser le Transact-SQL

---

## 📋 Table des Matières

1. [Introduction au T-SQL](#1-introduction-au-t-sql)
2. [Variables et Types de Données](#2-variables-et-types-de-données)
3. [Conversion de Types](#3-conversion-de-types)
4. [Structures de Contrôle de Flux](#4-structures-de-contrôle-de-flux)
5. [Gestion des Erreurs](#5-gestion-des-erreurs)
6. [Procédures Stockées](#6-procédures-stockées)
7. [Fonctions (UDF)](#7-fonctions-udf)
8. [Curseurs](#8-curseurs)
9. [Triggers (Déclencheurs)](#9-triggers-déclencheurs)
10. [Transactions et Concurrence](#10-transactions-et-concurrence)
11. [📚 Ressources en Ligne pour Approfondir](#11-ressources-en-ligne-pour-approfondir)
12. [🤖 T-SQL × Intelligence Artificielle](#12-t-sql--intelligence-artificielle)

---

## 1. Introduction au T-SQL

**Définition :** Le Transact-SQL (T-SQL) est l'**extension procédurale propriétaire de Microsoft** pour SQL Server. Il transforme SQL (statique) en un vrai langage de programmation (dynamique).

### Les 4 raisons clés d'utiliser T-SQL

| Avantage | Description |
|---|---|
| **Logique Métier Centralisée** | Règle écrite une seule fois sur le serveur, utilisable par toutes les interfaces |
| **Performance Réseau** | Calculs faits côté serveur, seul le résultat final transite |
| **Sécurité Accrue** | Accès contrôlé via des scripts, sans exposition directe des tables |
| **Automatisation** | Les Triggers réagissent en temps réel aux événements |

### Analogies utiles
- 🍴 **Chef de cuisine** : SQL = liste de courses / T-SQL = Chef qui adapte la recette selon les stocks
- 🗺️ **GPS vs Carte** : SQL = carte fixe / T-SQL = GPS qui recalcule selon les conditions

---

## 2. Variables et Types de Données

### 2.1 Déclaration et Affectation

```sql
-- Déclaration
DECLARE @nomVariable Type_de_donnée;

-- Affectation statique (SET)
SET @bonus = 2;
SET @bonus = @bonus + 1;

-- Affectation dynamique depuis une table (SELECT)
SELECT @moyenne = AVG(Note) FROM Notes WHERE EtudiantId = 101;
```

> ⚠️ Toute variable doit **obligatoirement** commencer par `@`.

### 2.2 Exemple complet (synthèse)

```sql
DECLARE @prixHT MONEY, @TVA DECIMAL(4,2), @prixTTC MONEY;

SELECT @prixHT = PrixUnitaire FROM Produits WHERE Id = 50;  -- Récupération
SET @TVA = 1.20;
SET @prixTTC = @prixHT * @TVA;                              -- Calcul

PRINT 'Prix final : ' + CAST(@prixTTC AS VARCHAR);          -- Affichage
```

### 2.3 Référentiel des Types de Données

#### Numérique
| Type | Description | Taille | Usage |
|---|---|---|---|
| `INT` | Entier standard | 4 octets | Nombre d'inscrits |
| `BIGINT` | Entier très long | 8 octets | ID de transaction globale |
| `DECIMAL(p,s)` | Nombre exact | Variable | Moyenne (ex: 14.75) |
| `FLOAT` | Nombre approché | 4–8 octets | Calculs scientifiques |

#### Texte
| Type | Description | Taille | Usage |
|---|---|---|---|
| `CHAR(n)` | Texte fixe | n octets | Code ISO Pays ('MA') |
| `VARCHAR(n)` | Texte variable | n+2 octets | Email étudiant |
| `NVARCHAR(n)` | Unicode | 2n+2 octets | Noms avec accents/Arabe |

#### Temporel
| Type | Description | Usage |
|---|---|---|
| `DATE` | Date pure | Date de naissance |
| `TIME` | Heure pure | Heure de cours |
| `DATETIME2` | Date + Heure précise | Log système |

#### Monnaie & Spécial
| Type | Description | Usage |
|---|---|---|
| `MONEY` | 8 octets | Salaire, budget |
| `SMALLMONEY` | 4 octets | Prix d'un article |
| `BIT` | Booléen (0 ou 1) | Admis ? Oui/Non |
| `UNIQUEIDENTIFIER` | ID universel (GUID) | `NEWID()` |
| `XML` | Données structurées | Fichiers de configuration |

---

## 3. Conversion de Types

### CAST — Norme ANSI (simple)
```sql
DECLARE @Age INT = 21;
PRINT 'L''étudiant a ' + CAST(@Age AS VARCHAR(3)) + ' ans.';
```

### CONVERT — Puissance T-SQL (avec formatage)
```sql
-- Style 103 = Format Européen JJ/MM/AAAA
SELECT CONVERT(VARCHAR, GETDATE(), 103) AS DateFrançaise;
-- Résultat : '11/06/2026'
```

> 💡 **Règle** : Utilisez `CAST` pour les conversions simples, `CONVERT` quand vous avez besoin d'un format spécifique (dates, monnaie).

---

## 4. Structures de Contrôle de Flux

### 4.1 Blocs de code — BEGIN...END

```sql
-- Sans BEGIN...END : seule la 1ère ligne est conditionnée
-- Avec BEGIN...END : toutes les instructions sont groupées
IF @note < 10
BEGIN
    PRINT 'Statut : Ajourné';
    UPDATE Etudiants SET Etat = 'Rattrapage' WHERE Id = @id;
END
```

### 4.2 IF / ELSE

```sql
DECLARE @moyenne DECIMAL(4,2) = 14.5;

IF @moyenne >= 10
    PRINT 'Résultat : Admis';
ELSE
    PRINT 'Résultat : Ajourné';
```

> ⚠️ En T-SQL, **pas de mot-clé `THEN`** (contrairement à Pascal ou VB).

### 4.3 CASE — Expression "en ligne"

```sql
DECLARE @codeStatut INT = 1;
DECLARE @libelle VARCHAR(20);

SET @libelle = CASE @codeStatut
    WHEN 1 THEN 'Actif'
    WHEN 2 THEN 'Inactif'
    WHEN 3 THEN 'Autre'
    ELSE 'Inconnu'
END;

PRINT @libelle;  -- Affiche : Actif
```

> 💡 `IF` contrôle le **flux** (quel bloc exécuter). `CASE` choisit une **valeur** (dans un SELECT, SET, UPDATE).

### 4.4 Boucle WHILE

```sql
DECLARE @compteur INT = 1;

WHILE @compteur <= 5
BEGIN
    PRINT 'Itération : ' + CAST(@compteur AS VARCHAR);
    SET @compteur = @compteur + 1;  -- ⚠️ OBLIGATOIRE pour éviter boucle infinie
END
```

### 4.5 BREAK et CONTINUE

```sql
-- BREAK : sortie immédiate de la boucle
WHILE @compteur < 100
BEGIN
    SET @compteur = @compteur + 1;
    IF @compteur = 50 BREAK;   -- Arrêt à 50
    PRINT @compteur;
END

-- CONTINUE : saute le reste du bloc, retourne au test
DECLARE @c INT = 0;
WHILE @c <= 5
BEGIN
    SET @c = @c + 1;
    IF @c = 3 CONTINUE;   -- Saute l'affichage pour c=3
    PRINT 'Valeur : ' + CAST(@c AS VARCHAR);
END
-- Résultat : 1, 2, 4, 5  (le 3 est sauté)
```

---

## 5. Gestion des Erreurs

### TRY...CATCH

```sql
BEGIN TRY
    SELECT 1/0;   -- Provoque une erreur de division par zéro
END TRY
BEGIN CATCH
    PRINT 'Erreur interceptée !';
    PRINT 'Message : ' + ERROR_MESSAGE();
    PRINT 'Ligne   : ' + CAST(ERROR_LINE() AS VARCHAR);
END CATCH
```

### Fonctions système disponibles dans le CATCH

| Fonction | Description | Exemple de valeur |
|---|---|---|
| `ERROR_NUMBER()` | Numéro d'identification de l'erreur | 2627 |
| `ERROR_MESSAGE()` | Texte descriptif | 'Violation of PRIMARY KEY...' |
| `ERROR_SEVERITY()` | Niveau de gravité (1-25) | 14 |
| `ERROR_LINE()` | Numéro de ligne de l'erreur | 5 |

---

## 6. Procédures Stockées

### 6.1 Définition et syntaxe de base

```sql
CREATE PROCEDURE sp_NomProcedure
AS
BEGIN
    -- Instructions T-SQL ici
END
```

### 6.2 Paramètres d'entrée (avec valeur par défaut)

```sql
CREATE PROCEDURE sp_RechercherEtudiant
    @lettreDebut NVARCHAR(1),      -- Paramètre requis
    @ageMinimum  INT = 18          -- Valeur par défaut
AS
BEGIN
    SELECT * FROM Etudiants
    WHERE Nom LIKE @lettreDebut + '%'
      AND Age >= @ageMinimum;
END
```

### 6.3 Exécution

```sql
-- Par position
EXEC sp_RechercherEtudiant 'A', 20;

-- Par nom (recommandé — plus lisible et sécurisé)
EXEC sp_RechercherEtudiant @lettreDebut = 'B', @ageMinimum = 22;
```

### 6.4 Paramètres de sortie (OUTPUT)

```sql
-- Définition
CREATE PROCEDURE sp_CompterParFiliere
    @filiere VARCHAR(10),
    @nb      INT OUTPUT   -- Marqueur de sortie
AS
BEGIN
    SELECT @nb = COUNT(*) FROM Etudiants WHERE Filiere = @filiere;
END

-- Appel — le mot-clé OUTPUT doit figurer aux deux endroits
DECLARE @resultatFinal INT;
EXEC sp_CompterParFiliere @filiere = 'LUS', @nb = @resultatFinal OUTPUT;
PRINT 'Total LUS : ' + CAST(@resultatFinal AS VARCHAR);
```

### 6.5 Maintenance

```sql
ALTER PROCEDURE sp_CalculerRemise @prix MONEY
AS BEGIN
    SELECT @prix * 0.90 AS PrixRemisé;   -- Modification interne
END

DROP PROCEDURE IF EXISTS sp_CalculerRemise;  -- Suppression sécurisée
```

> ✅ **ALTER** conserve les droits d'accès existants. **DROP + CREATE** les efface.

---

## 7. Fonctions (UDF)

### Comparaison Procédure vs Fonction

| Critère | Procédure Stockée | Fonction (UDF) |
|---|---|---|
| Objectif | Exécuter une logique métier | Calculer / Transformer |
| Effets de bord | Peut modifier les données | Lecture seule uniquement |
| Retour | OUTPUT ou SELECT | Une valeur ou une table |
| Appel | `EXECUTE` (instruction) | Dans `SELECT`, `WHERE`, `JOIN` |
| Transactions | Autorisées | Interdites |

### 7.1 Fonction Scalaire (retourne une valeur unique)

```sql
CREATE FUNCTION fn_FormatNomComplet
    (@nom NVARCHAR(50), @prenom NVARCHAR(50))
RETURNS NVARCHAR(101)
AS
BEGIN
    RETURN UPPER(@nom) + ' ' + @prenom;
END

-- Utilisation
SELECT dbo.fn_FormatNomComplet(Nom, Prenom) FROM Etudiants;
-- Résultat : ZEROUAL Badr
```

### 7.2 Fonction Table Inline (retourne un jeu de données)

```sql
CREATE FUNCTION fn_CoursParEtudiant (@etudiantId INT)
RETURNS TABLE
AS
RETURN (
    SELECT C.NomCours, C.Coefficient, I.DateInscription
    FROM Cours C
    JOIN Inscriptions I ON C.IdCours = I.IdCours
    WHERE I.IdEtudiant = @etudiantId
);

-- Utilisation comme une table
SELECT * FROM dbo.fn_CoursParEtudiant(5);
```

---

## 8. Curseurs

> ⚠️ **Règle d'or** : Si vous pouvez résoudre le problème avec un `UPDATE` ou `JOIN`, n'utilisez PAS de curseur. Les curseurs sont lents et consomment beaucoup de mémoire.

### 8.1 Le cycle de vie en 5 étapes

| Étape | Commande | Description |
|---|---|---|
| 1 | `DECLARE` | Définir la requête SELECT qui alimente le curseur |
| 2 | `OPEN` | Exécuter la requête, charger en mémoire |
| 3 | `FETCH NEXT` | Lire la ligne courante dans des variables |
| 4 | `CLOSE` | Fermer le curseur |
| 5 | `DEALLOCATE` | Libérer la mémoire serveur |

### 8.2 Exemple complet

```sql
DECLARE @Nom VARCHAR(50);

-- 1. Déclaration
DECLARE cur_etudiant CURSOR FOR
    SELECT Nom FROM Etudiants WHERE Note >= 10;

-- 2. Ouverture
OPEN cur_etudiant;

-- 3. Première lecture
FETCH NEXT FROM cur_etudiant INTO @Nom;

-- Boucle tant que la lecture réussit (@@FETCH_STATUS = 0)
WHILE @@FETCH_STATUS = 0
BEGIN
    PRINT 'Félicitations M./Mme ' + @Nom;
    FETCH NEXT FROM cur_etudiant INTO @Nom;   -- Ligne suivante
END

-- 4 & 5. Fermeture et libération
CLOSE cur_etudiant;
DEALLOCATE cur_etudiant;
```

### 8.3 La variable système @@FETCH_STATUS

| Valeur | Signification |
|---|---|
| `0` | Succès — la ligne a été lue |
| `-1` | Fin du curseur dépassée |
| `-2` | La ligne lue a été supprimée entre-temps |

---

## 9. Triggers (Déclencheurs)

### 9.1 Principe

Un trigger est une **procédure stockée spéciale** qui se déclenche **automatiquement** suite à un `INSERT`, `UPDATE` ou `DELETE` — jamais appelé manuellement.

> 🔔 Analogie : c'est une **alarme de sécurité** qui se déclenche dès qu'une porte s'ouvre.

### 9.2 Les tables magiques INSERTED et DELETED

| Opération | Table INSERTED | Table DELETED |
|---|---|---|
| `INSERT` | Nouvelles données | Vide |
| `DELETE` | Vide | Données supprimées |
| `UPDATE` | Nouvelles valeurs | Anciennes valeurs |

### 9.3 Syntaxe de base

```sql
CREATE TRIGGER tr_NomDuTrigger
ON NomDeLaTable
AFTER INSERT, UPDATE   -- ou INSTEAD OF
AS
BEGIN
    -- Code exécuté automatiquement
END
```

### 9.4 Exemple 1 — Audit (historique des modifications)

```sql
CREATE TRIGGER TR_AuditPrix
ON Produits
AFTER UPDATE
AS
BEGIN
    -- On sauvegarde l'ancien prix depuis la table DELETED
    INSERT INTO HistoriquePrix (IdProduit, AncienPrix, DateModif)
    SELECT Id, Prix, GETDATE() FROM DELETED;
END
```

### 9.5 Exemple 2 — Calcul automatique (mise à jour de stock)

```sql
CREATE TRIGGER TR_MajStock
ON Ventes
AFTER INSERT
AS
BEGIN
    UPDATE Produits
    SET Stock = Stock - I.Quantite
    FROM Produits P
    JOIN INSERTED I ON P.Id = I.ProduitId;
END
```

### 9.6 Maintenance

```sql
ALTER TRIGGER TR_Audit ON Etudiants AFTER INSERT
AS BEGIN PRINT 'Nouvel étudiant !'; END

DISABLE TRIGGER TR_Audit ON Etudiants;   -- Mise en pause (import massif)
ENABLE  TRIGGER TR_Audit ON Etudiants;   -- Réactivation
DROP TRIGGER IF EXISTS TR_Audit;          -- Suppression
```

### 9.7 Points d'attention

- **Invisibilité** : Des données peuvent changer sans que le développeur comprenne pourquoi.
- **Performance** : Un trigger lourd ralentit chaque opération DML.
- **Boucle infinie** : Un trigger sur Table A qui modifie Table A → ⚠️ danger !

---

## 10. Transactions et Concurrence

### 10.1 Principe ACID — Le "Tout ou Rien"

```
Analogie du virement bancaire :
  ① Retirer 100€ du Compte A
  ② Ajouter 100€ au Compte B
  → Si ② échoue, ① doit être annulé — l'argent ne peut pas disparaître.
```

### 10.2 Les 3 commandes de contrôle

| Commande | Rôle |
|---|---|
| `BEGIN TRANSACTION` | Marque le début de l'unité de travail |
| `COMMIT` | Valide définitivement toutes les modifications |
| `ROLLBACK` | Annule tout et revient à l'état initial |

### 10.3 Patron de sécurité — Transaction + TRY...CATCH

```sql
BEGIN TRANSACTION;

BEGIN TRY
    -- Étape 1 : Débiter
    UPDATE Comptes SET Solde = Solde - 100 WHERE Id = 1;

    -- Étape 2 : Créditer
    UPDATE Comptes SET Solde = Solde + 100 WHERE Id = 2;

    COMMIT;   -- ✅ Tout s'est bien passé
    PRINT 'Transfert réussi.';
END TRY
BEGIN CATCH
    ROLLBACK;  -- ❌ Annulation de TOUT (y compris l'étape 1)
    PRINT 'Erreur : ' + ERROR_MESSAGE();
END CATCH
```

### 10.4 Concurrence — Les Verrous (Locks)

Pendant qu'une transaction est ouverte, SQL Server pose des **verrous** sur les lignes modifiées → empêche d'autres utilisateurs de corrompre les données en cours de calcul.

---

## 11. 📚 Ressources en Ligne pour Approfondir

### 🎓 Cours Gratuits (Débutant → Avancé)

| Plateforme | Cours | Niveau | Lien |
|---|---|---|---|
| **Microsoft Learn** | Introduction to T-SQL | Débutant | [learn.microsoft.com](https://learn.microsoft.com/fr-fr/training/paths/get-started-querying-with-transact-sql/) |
| **Microsoft Learn** | Build AI solutions with SQL Server 2025 | Avancé | [learn.microsoft.com](https://learn.microsoft.com/en-us/training/modules/build-ai-solutions-sql-server/) |
| **SQLZoo** | SQL interactif dans le navigateur | Débutant | [sqlzoo.net](https://sqlzoo.net/) |
| **Khan Academy** | Intro to SQL : Querying and managing data | Débutant | [khanacademy.org](https://www.khanacademy.org/computing/computer-programming/sql) |
| **Codecademy** | Learn SQL (Browser-based) | Débutant | [codecademy.com](https://www.codecademy.com/learn/learn-sql) |
| **freeCodeCamp** | Relational Database Full Course | Débutant | [freecodecamp.org](https://www.freecodecamp.org/learn/relational-database/) |
| **SQLBolt** | SQL interactif — leçons progressives | Débutant | [sqlbolt.com](https://sqlbolt.com/) |
| **W3Schools SQL** | Référence complète + sandbox | Débutant | [w3schools.com/sql](https://www.w3schools.com/sql/) |
| **Kaggle** | Intro to SQL (sur BigQuery) | Intermédiaire | [kaggle.com/learn/intro-to-sql](https://www.kaggle.com/learn/intro-to-sql) |
| **HackerRank SQL** | Challenges pratiques avec badge | Intermédiaire | [hackerrank.com/domains/sql](https://www.hackerrank.com/domains/sql) |

### 📹 Chaînes YouTube Recommandées

| Chaîne | Description | Lien |
|---|---|---|
| **Bro Code** | T-SQL & SQL Server en anglais clair | [YouTube](https://www.youtube.com/@BroCodez) |
| **Kudvenkat** | Série complète SQL Server / T-SQL | [YouTube](https://www.youtube.com/@Csharp-video-tutorialsBlogspot) |
| **Microsoft Developer** | Nouveautés SQL Server & Azure | [YouTube](https://www.youtube.com/@MicrosoftDeveloper) |
| **Data with Mo** | SQL & BI en français | [YouTube](https://www.youtube.com/@DatawithMo) |

### 🏅 Certifications Microsoft Officielles

| Certification | Niveau | Contenu | Lien |
|---|---|---|---|
| **DP-900** — Azure Data Fundamentals | Débutant | Bases SQL, NoSQL, Azure Data | [learn.microsoft.com/dp-900](https://learn.microsoft.com/fr-fr/credentials/certifications/azure-data-fundamentals/) |
| **DP-300** — Azure Database Administrator Associate | Intermédiaire | Administration SQL Server/Azure SQL | [learn.microsoft.com/dp-300](https://learn.microsoft.com/fr-fr/credentials/certifications/azure-database-administrator-associate/) |
| **DP-203** — Azure Data Engineer Associate | Avancé | ETL, Data Lake, pipelines | [learn.microsoft.com/dp-203](https://learn.microsoft.com/fr-fr/credentials/certifications/azure-data-engineer/) |
| **70-761 / DP-080** — Querying with T-SQL | Intermédiaire | T-SQL avancé, requêtes complexes | [learn.microsoft.com](https://learn.microsoft.com/en-us/credentials/certifications/query-data-with-t-sql/) |

> 💡 **Conseil** : Commencez par **DP-900** (gratuit à préparer via Microsoft Learn), puis enchaînez avec **DP-300** pour la spécialisation SQL Server.

### 🛠️ Outils de Pratique SQL

| Outil | Description | Lien |
|---|---|---|
| **SQL Server Management Studio (SSMS)** | IDE officiel Microsoft pour SQL Server | [Télécharger SSMS](https://learn.microsoft.com/fr-fr/ssms/download-sql-server-management-studio-ssms) |
| **Azure Data Studio** | IDE léger, cross-platform, notebooks | [Télécharger ADS](https://learn.microsoft.com/fr-fr/azure-data-studio/download-azure-data-studio) |
| **DB Fiddle** | Sandbox SQL en ligne (SQL Server, MySQL, PostgreSQL) | [db-fiddle.com](https://www.db-fiddle.com/) |
| **SQL Server Express** | Version gratuite de SQL Server | [microsoft.com](https://www.microsoft.com/fr-fr/sql-server/sql-server-downloads) |
| **LeetCode SQL** | 200+ exercices SQL pratiques | [leetcode.com/problemset/database/](https://leetcode.com/problemset/database/) |

### 📖 Documentation de Référence

| Ressource | Description | Lien |
|---|---|---|
| **Microsoft Docs T-SQL** | Référence officielle complète | [learn.microsoft.com/tsql](https://learn.microsoft.com/fr-fr/sql/t-sql/language-reference) |
| **SQL Server 2025 — Nouveautés** | Annonce officielle Microsoft | [microsoft.com/sql-server/blog](https://www.microsoft.com/en-us/sql-server/blog/2025/05/19/announcing-sql-server-2025-preview/) |
| **SQLServerCentral** | Articles, forums, scripts | [sqlservercentral.com](https://www.sqlservercentral.com/) |
| **Brent Ozar Unlimited** | Blog expert SQL Server (performance) | [brentozar.com](https://www.brentozar.com/) |

---

## 12. 🤖 T-SQL × Intelligence Artificielle

> **Bonne nouvelle** : SQL Server 2025 intègre nativement l'IA directement dans le moteur de base de données. Si vous maîtrisez T-SQL, vous êtes déjà prêt(e) à faire de l'IA sur vos données.

### 12.1 Les Grandes Nouveautés SQL Server 2025 + IA

| Fonctionnalité | Description |
|---|---|
| **`CREATE EXTERNAL MODEL`** | Enregistre un modèle IA (OpenAI, Azure, Ollama) comme objet natif de la BD |
| **`sp_invoke_external_rest_endpoint`** | Appelle n'importe quelle API REST (Azure OpenAI, etc.) directement depuis T-SQL |
| **Type `VECTOR`** | Stocke des embeddings (vecteurs) en natif dans SQL Server |
| **`AI_GENERATE_EMBEDDINGS`** | Génère des embeddings vectoriels en T-SQL |
| **`VECTOR_SEARCH`** | Recherche sémantique (par sens, pas par mot-clé) dans la base |
| **Copilot dans SSMS** | Génère du T-SQL à partir de langage naturel (NLP → SQL) |

### 12.2 Exemple : Appeler Azure OpenAI depuis T-SQL

```sql
-- 1. Enregistrer le modèle IA
CREATE EXTERNAL MODEL MonModeleOpenAI
    WITH (
        LOCATION = 'https://mon-endpoint.openai.azure.com/',
        API_FORMAT = 'AzureOpenAI',
        MODEL_TYPE = GENERATIVE,
        MODEL = 'gpt-4o'
    );
GO

-- 2. Générer du texte directement en T-SQL
EXEC sp_invoke_external_rest_endpoint
    @url = 'https://mon-endpoint.openai.azure.com/openai/deployments/gpt-4o/chat/completions',
    @method = 'POST',
    @payload = '{"messages":[{"role":"user","content":"Résume ce produit"}]}',
    @response = @result OUTPUT;
```

### 12.3 Exemple : Recherche Sémantique (RAG avec SQL)

```sql
-- Stocker des embeddings dans une colonne VECTOR
ALTER TABLE Produits ADD DescriptionVector VECTOR(1536);

-- Chercher les produits les plus proches sémantiquement
SELECT TOP 5 NomProduit, VECTOR_DISTANCE('cosine', DescriptionVector, @queryVector) AS Score
FROM Produits
ORDER BY Score ASC;
```

### 12.4 Cas d'Usage concrets T-SQL + IA

| Cas d'usage | Ce que T-SQL + IA permet |
|---|---|
| **Analyse de sentiment** | Passer une colonne "commentaires clients" à GPT et stocker le résultat |
| **Catégorisation automatique** | Classer des tickets, des produits ou des emails via un LLM |
| **Recherche sémantique** | Trouver des produits/articles par sens ("chaussures légères pour courir") |
| **Génération de rapports** | Envoyer des données agrégées à un LLM pour rédiger un résumé en langage naturel |
| **Détection d'anomalies** | Coupler ML Services (Python/R) avec T-SQL pour détecter des fraudes |
| **Chatbot sur vos données** | Architecture RAG : SQL Server stocke les embeddings, LLM répond aux questions |

### 12.5 Ressources T-SQL × IA

| Ressource | Description | Lien |
|---|---|---|
| **Microsoft Learn — Build AI with SQL Server 2025** | Module officiel pas-à-pas | [learn.microsoft.com](https://learn.microsoft.com/en-us/training/modules/build-ai-solutions-sql-server/) |
| **SQL AI Samples (GitHub)** | Dépôt officiel Microsoft avec exemples RAG, embeddings | [github.com/microsoft/sql-ai-samples](https://github.com/microsoft/sql-ai-samples) |
| **Intelligent Apps — Microsoft Docs** | Vue d'ensemble IA + SQL Server | [learn.microsoft.com/ai](https://learn.microsoft.com/en-us/sql/sql-server/ai/artificial-intelligence-intelligent-applications) |
| **SQLYARD — AI + SQL Server 2025** | Guide pratique étape par étape | [sqlyard.com](https://sqlyard.com/2026/01/19/build-ai-powered-solutions-using-sql-server-2025-step-by-step/) |
| **LangChain + SQL Server** | Construire des agents IA qui interrogent votre BD | [python.langchain.com](https://python.langchain.com/docs/integrations/toolkits/sql_database) |
| **Semantic Kernel (Microsoft)** | Framework IA pour orchestrer des agents avec SQL | [learn.microsoft.com/semantic-kernel](https://learn.microsoft.com/fr-fr/semantic-kernel/overview/) |
| **Azure OpenAI Service** | LLMs (GPT-4o, embeddings) accessibles via API REST depuis T-SQL | [azure.microsoft.com/openai](https://azure.microsoft.com/fr-fr/products/ai-services/openai-service) |
| **Ollama (local LLM)** | Faire tourner un LLM localement, appelable depuis SQL Server 2025 | [ollama.ai](https://ollama.ai) |
| **4sysops — AI in SQL Server 2025** | Article technique détaillé | [4sysops.com](https://4sysops.com/archives/ai-features-in-microsoft-sql-server-2025-and-azure-sql/) |

### 12.6 Copilot dans SSMS — L'IA qui écrit du T-SQL pour vous

> **SSMS 22+** intègre GitHub Copilot : tapez votre besoin en français ou en anglais, Copilot génère le T-SQL correspondant.

```
Exemple de prompt naturel dans SSMS :
  "Donne-moi la liste des 10 étudiants ayant la meilleure moyenne
   cette année, avec leur filière et leur note de rattrapage si elle existe"

→ Copilot génère automatiquement la requête T-SQL avec les bons JOINs.
```

---

## 📌 Résumé Global — Les 6 Piliers du T-SQL

```
┌─────────────────────────────────────────────────────────────┐
│  1. Variables & Types    →  La mémoire du script            │
│  2. Structures de contrôle →  La logique décisionnelle      │
│  3. Procédures & Fonctions → La modularité et réutilisation │
│  4. Curseurs             →  Le traitement ligne par ligne   │
│  5. Triggers             →  L'automatisation par événement  │
│  6. Transactions         →  La sécurité et l'intégrité     │
└─────────────────────────────────────────────────────────────┘
```

---
