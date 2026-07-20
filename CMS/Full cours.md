# Cours complet sur les CMS

## De la création de contenu à WordPress, l’automatisation, l’IA et MCP

**Niveau :** débutant à intermédiaire  
**Durée conseillée :** 18 à 24 heures  
**Méthode :** 40 % théorie, 60 % pratique  
**Projet fil rouge :** concevoir et sécuriser le site d’une entreprise de rénovation de l’habitat, puis connecter ses formulaires à un CRM.

---

## Objectifs généraux

À la fin de ce cours, l’apprenant saura :

- expliquer le rôle d’un CMS et distinguer CMS traditionnel, headless, hybride et SaaS ;
- comparer WordPress, Drupal, Shopify, Wix et plusieurs CMS headless ;
- installer, configurer et administrer un site WordPress ;
- structurer les contenus, les rôles, les extensions et les intégrations ;
- appliquer les bases du SEO, de la performance, de l’accessibilité et de la sécurité ;
- construire une automatisation fiable entre formulaire, CRM et outil de notification ;
- expliquer le rôle réel d’un LLM et de MCP, ainsi que leurs risques ;
- décider rationnellement entre CMS, headless et développement fullstack.

## Prérequis et environnement

- Savoir utiliser un navigateur et gérer des fichiers.
- Connaître les bases de HTML et CSS est utile, mais pas obligatoire.
- Pour les travaux pratiques : Local, Studio, Docker ou un hébergement de test, un navigateur avec outils de développement et un dépôt Git pour le code personnalisé.
- Ne jamais réaliser les exercices directement sur un site en production.

## Évaluation proposée

| Évaluation | Pondération | Livrable |
|---|---:|---|
| Quiz de fin de partie | 20 % | 5 quiz courts |
| Travaux pratiques | 35 % | Captures, configuration et justification |
| Audit d’un site | 20 % | Rapport SEO, performance et sécurité |
| Projet final | 25 % | Prototype fonctionnel et soutenance |

---

# Partie 1 — Comprendre l’écosystème des CMS

**Durée :** 3 heures

## Objectifs de la partie

- Définir précisément un CMS.
- Identifier les grandes familles d’architecture.
- Comparer les plateformes selon un besoin métier.
- Comprendre que le choix dépend du coût total, pas seulement du prix de départ.

## 1. Qu’est-ce qu’un CMS ?

Un CMS, ou système de gestion de contenu, permet de créer, organiser, valider et publier des contenus sans développer manuellement chaque page. Il sépare généralement :

- le **contenu** : textes, images, produits et métadonnées ;
- la **présentation** : thème, modèles et composants ;
- les **fonctionnalités** : extensions, modules ou applications ;
- la **gouvernance** : comptes, rôles, permissions et workflow éditorial.

Un CMS ne supprime pas le besoin de compétences techniques. Il déplace une partie du travail vers la configuration, l’intégration, la maintenance et la gouvernance.

## 2. Les quatre architectures principales

| Architecture | Fonctionnement | Avantages | Limites | Exemple |
|---|---|---|---|---|
| Traditionnelle | Administration et affichage dans le même système | Simple, rapide, nombreux modèles | Couplage front/back | WordPress classique, Drupal |
| SaaS | Logiciel et hébergement gérés par l’éditeur | Faible maintenance technique | Dépendance, limites contractuelles | Wix, Shopify |
| Headless | Le CMS fournit le contenu par API à un front séparé | Expériences multicanales, liberté du front | Coût et complexité accrus | Strapi, Contentful, Sanity |
| Hybride | Rendu traditionnel et API selon les besoins | Compromis progressif | Architecture plus difficile à gouverner | WordPress ou Drupal avec front découplé |

> **Point clé :** « headless » ne signifie pas automatiquement plus rapide, plus sécurisé ou meilleur pour le SEO. Le résultat dépend de l’architecture, du rendu, du cache et de la qualité de l’implémentation.

## 3. Panorama des principales solutions

### WordPress

- **Idéal pour :** sites vitrines, médias, blogs, génération de prospects et boutiques WooCommerce.
- **Technologies :** PHP, MySQL/MariaDB, HTML, CSS et JavaScript.
- **Forces :** autonomie marketing, vaste écosystème, extensibilité et documentation abondante.
- **Vigilance :** qualité variable des extensions, maintenance et conflits possibles.

### Drupal

- **Idéal pour :** portails complexes, contenu fortement structuré, multisite et permissions avancées.
- **Forces :** modélisation du contenu, taxonomies, rôles et workflows.
- **Vigilance :** courbe d’apprentissage et coût d’intégration supérieurs.

### Shopify

- **Idéal pour :** commerce en ligne centré sur le catalogue, le paiement et les commandes.
- **Forces :** environnement hébergé, exploitation simplifiée, écosystème marchand.
- **Vigilance :** abonnement, applications payantes, frais éventuels et dépendance à la plateforme.

### Wix

- **Idéal pour :** petit site vitrine ou portfolio à mettre en ligne rapidement.
- **Forces :** interface visuelle et hébergement intégrés.
- **Vigilance :** contrôle technique, portabilité et personnalisation avancée plus limités.

### Autres solutions utiles

- **PrestaShop / Adobe Commerce :** commerce électronique spécialisé.
- **Ghost :** publication et abonnements.
- **Strapi :** CMS headless open source et API-first.
- **Contentful, Sanity, Prismic :** plateformes headless gérées.
- **Joomla :** CMS généraliste avec gestion native de contenus et d’utilisateurs.

## 4. Le coût total de possession

Le coût réel sur trois ans comprend : licences, hébergement, thème, extensions, intégration, maintenance, sécurité, sauvegardes, formation, migrations et temps de l’équipe. Une solution gratuite peut donc coûter plus cher qu’un SaaS si elle demande beaucoup de maintenance.

## 5. Méthode de sélection pondérée

1. Lister les exigences obligatoires et souhaitables.
2. Attribuer un poids à chaque critère : contenu, commerce, SEO, sécurité, autonomie, intégrations, budget et délai.
3. Noter chaque solution de 1 à 5.
4. Tester les deux meilleures avec une preuve de concept.
5. Évaluer la réversibilité : export des contenus, données, médias et URLs.

### Cas pratique

Une entreprise de rénovation veut publier des pages locales, collecter des demandes de diagnostic, connecter un CRM et permettre au marketing de modifier les pages. Comparez WordPress, Wix et une application fullstack sur 8 critères. Justifiez votre recommandation en 300 mots.

### Quiz rapide

1. Quelle différence existe entre CMS traditionnel et headless ?
2. Pourquoi le coût de licence ne suffit-il pas pour comparer deux CMS ?
3. Citez deux situations dans lesquelles Drupal peut être préférable à WordPress.

### Ressources

- [Documentation WordPress](https://wordpress.org/documentation/)
- [Guide utilisateur Drupal](https://www.drupal.org/docs/user_guide/en/index.html)
- [Documentation Shopify](https://help.shopify.com/)
- [Documentation Strapi](https://docs.strapi.io/)
- [Web Content Accessibility Guidelines — WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)

---

# Partie 2 — WordPress en profondeur

**Durée :** 8 à 10 heures

## Objectifs de la partie

- Comprendre le cycle d’une requête WordPress.
- Structurer correctement le contenu et les comptes.
- Choisir entre Gutenberg, constructeur visuel et développement personnalisé.
- Installer des extensions selon une méthode de sélection rigoureuse.
- mettre en place SEO, performance, sécurité et maintenance.

## 1. WordPress.org et WordPress.com

**WordPress.org** fournit le logiciel open source à installer chez l’hébergeur de son choix. **WordPress.com** est un service hébergé proposant plusieurs offres. Il faut distinguer le logiciel, le service d’hébergement et le nom de domaine avant d’évaluer les coûts ou les limitations.

## 2. Architecture technique

Une requête simplifiée suit ce parcours : navigateur → serveur web → PHP/WordPress → base de données → thème/modèle → HTML retourné au navigateur. Le cache peut éviter plusieurs étapes.

Répertoires importants :

- `wp-admin` : interface d’administration ;
- `wp-includes` : cœur technique ;
- `wp-content/themes` : thèmes ;
- `wp-content/plugins` : extensions ;
- `wp-content/uploads` : médias.

Ne jamais modifier directement le cœur de WordPress ni un thème parent. Utiliser un thème enfant, un plugin personnalisé ou un plugin de snippets correctement gouverné.

## 3. Modèle de contenu

- **Article :** contenu daté, souvent classé et destiné à un flux éditorial.
- **Page :** contenu plutôt permanent et hiérarchique.
- **Custom Post Type :** type métier, par exemple « Réalisations » ou « Agences ».
- **Taxonomie :** système de classement, par exemple service, région ou type de chantier.
- **Métadonnée :** information attachée à un objet, par exemple durée ou surface.

### Exemple pour Culture Habitat

Créer un type `realisation`, une taxonomie `service` et les champs ville, département, surface, date et photos. Cette structure évite de dupliquer la mise en page et facilite les filtres et le SEO local.

## 4. Base de données

Tables courantes : `wp_posts`, `wp_postmeta`, `wp_users`, `wp_usermeta`, `wp_options`, `wp_terms`, `wp_term_taxonomy` et `wp_term_relationships`. Le préfixe peut différer de `wp_`.

Règles essentielles :

- passer par les API WordPress quand elles existent ;
- utiliser `$wpdb->prepare()` pour les requêtes personnalisées ;
- sauvegarder fichiers **et** base de données ;
- ne pas nettoyer automatiquement les tables sans sauvegarde et test préalable ;
- surveiller les options autoloadées, les transients et les révisions excessives.

## 5. Thèmes, Gutenberg et Elementor

| Solution | À privilégier lorsque… | Risque principal |
|---|---|---|
| Éditeur de site/Gutenberg | on veut rester proche du cœur et réutiliser des blocs | apprentissage du système de blocs |
| Elementor | l’équipe doit produire rapidement des pages visuelles | poids, dépendance et incohérences de design |
| Thème personnalisé | design et performance exigent un contrôle fin | coût de développement et maintenance |

Avec un constructeur visuel, définir un système de design global : couleurs, typographies, espacements, boutons et composants. Éviter de régler chaque widget séparément.

## 6. Hooks et extension

Une **action** exécute une fonction à un moment donné. Un **filtre** reçoit une valeur, la transforme puis la retourne.

```php
<?php
add_filter('the_title', function ($title) {
    return is_admin() ? $title : esc_html($title);
});
```

Pour du code réel : vérifier les capacités de l’utilisateur, utiliser des nonces contre les requêtes forgées, valider à l’entrée, nettoyer avant stockage et échapper selon le contexte de sortie.

## 7. Utilisateurs et gouvernance

Appliquer le principe du moindre privilège. Un rédacteur n’a généralement pas besoin du rôle administrateur. Documenter : propriétaire du domaine, comptes d’hébergement, responsables des sauvegardes, licences, accès prestataires et procédure de départ d’un collaborateur.

## 8. Choisir une extension

Avant l’installation, vérifier :

- utilité métier et absence de doublon ;
- compatibilité avec la version actuelle de WordPress et PHP ;
- fréquence des mises à jour et qualité du support ;
- réputation de l’éditeur et politique de sécurité ;
- impact sur les performances et les données personnelles ;
- méthode d’export et comportement après désactivation.

Une extension installée mais inactive reste du code à maintenir ou à supprimer si elle n’est pas nécessaire.

## 9. SEO technique et éditorial

Le plugin SEO aide à configurer, mais ne garantit pas le positionnement. Le travail comprend :

- intention de recherche et contenu utile ;
- un titre principal clair et une hiérarchie logique ;
- URLs stables, liens internes et fil d’Ariane ;
- titres SEO et descriptions uniques ;
- canonicals, sitemap XML et règles d’indexation cohérentes ;
- données structurées adaptées au contenu réel ;
- images dimensionnées, compressées et décrites ;
- pages rapides, mobiles et accessibles ;
- suivi dans Google Search Console.

Pour un site multirégional, chaque page locale doit fournir une valeur réellement locale. Éviter les centaines de pages presque identiques où seul le nom de ville change.

## 10. Performance

Mesurer avant d’optimiser avec PageSpeed Insights, Lighthouse et les outils réseau du navigateur. Les Core Web Vitals portent notamment sur le chargement, la réactivité et la stabilité visuelle.

Ordre de priorité conseillé :

1. hébergement, version PHP et temps de réponse serveur ;
2. images aux bonnes dimensions, WebP/AVIF et chargement différé ;
3. cache de page et CDN si nécessaire ;
4. polices, scripts tiers, pixels et formulaires embarqués ;
5. CSS/JS inutilisés et chargement conditionnel ;
6. base de données et tâches planifiées.

Ne pas activer simultanément plusieurs plugins de cache remplissant la même fonction : ils peuvent se contredire.

## 11. Sécurité

La sécurité est un processus, pas un plugin. Mesures minimales :

- mises à jour rapides du cœur, des thèmes et extensions ;
- comptes nominatifs, mots de passe uniques et MFA ;
- moindre privilège et suppression des comptes obsolètes ;
- sauvegardes chiffrées, hors serveur et restaurations testées ;
- HTTPS, en-têtes adaptés et configuration serveur maintenue ;
- pare-feu applicatif et limitation des tentatives si le risque le justifie ;
- journalisation, surveillance de disponibilité et plan de réponse à incident ;
- installation uniquement depuis des sources fiables.

En cas de compromission : isoler, préserver les journaux, changer les secrets depuis un appareil sain, identifier la cause, restaurer une version propre, corriger puis surveiller. Une simple réinstallation d’un plugin de sécurité ne suffit pas.

## 12. Sauvegardes et maintenance

Appliquer une variante de la règle 3-2-1 : plusieurs copies, sur des supports différents, dont une hors du serveur. La fréquence dépend de la perte de données acceptable. Une sauvegarde non restaurée en test n’est pas une garantie.

Cycle recommandé : sauvegarde → staging → mises à jour → tests fonctionnels → déploiement → surveillance → possibilité de retour arrière.

### TP guidé

1. Installer WordPress dans un environnement de test.
2. Créer les pages Accueil, Services, Réalisations, Diagnostic et Contact.
3. Créer un rôle « Éditeur marketing » sans droit d’installation d’extension.
4. Construire un formulaire de diagnostic avec consentement explicite.
5. Configurer les permaliens, sitemap et métadonnées.
6. Mesurer les performances avant/après optimisation.
7. Effectuer une sauvegarde et prouver sa restauration sur l’environnement de test.

### Critères de réussite

- Aucun compte partagé ni droit administrateur injustifié.
- Formulaire testé sur mobile, confirmation affichée et donnée reçue.
- Pas de conflit de cache ou d’erreur JavaScript visible.
- Sauvegarde restaurable et procédure documentée.
- Pages accessibles au clavier et images avec alternative pertinente.

### Ressources

- [Learn WordPress — cours et ateliers](https://learn.wordpress.org/)
- [WordPress Developer Resources](https://developer.wordpress.org/)
- [Plugin Handbook](https://developer.wordpress.org/plugins/)
- [Theme Handbook](https://developer.wordpress.org/themes/)
- [REST API Handbook](https://developer.wordpress.org/rest-api/)
- [Guide de durcissement WordPress](https://developer.wordpress.org/advanced-administration/security/hardening/)
- [Google Search Central — SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- [PageSpeed Insights](https://pagespeed.web.dev/)
- [Web.dev — Core Web Vitals](https://web.dev/articles/vitals)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)

---

# Partie 3 — CRM, automatisation, LLM et MCP

**Durée :** 4 à 5 heures

## Objectifs de la partie

- Concevoir une automatisation observable et résistante aux erreurs.
- Distinguer API, webhook, LLM, agent et MCP.
- Évaluer les risques liés aux données, aux permissions et à la publication automatique.

## 1. Intégrer un CRM

Un formulaire n’est pas un CRM. Le formulaire collecte ; le CRM centralise les contacts, leur historique, leur statut et les actions commerciales.

Flux type :

1. Le visiteur soumet le formulaire.
2. Le serveur valide et enregistre la demande.
3. Un webhook transmet les données nécessaires.
4. Le CRM recherche un éventuel doublon et crée ou met à jour le contact.
5. Une notification est envoyée au bon responsable.
6. L’événement de conversion est déclenché après succès réel.

Prévoir un identifiant de demande, un journal, des tentatives contrôlées, une file d’erreur et une alerte. Une automatisation silencieuse qui perd des prospects est pire qu’un traitement manuel visible.

## 2. API, webhook et outils no-code

- **API :** contrat permettant à un logiciel de demander ou modifier des données.
- **Webhook :** notification HTTP envoyée lorsqu’un événement se produit.
- **Make, Zapier, n8n :** orchestrateurs permettant d’enchaîner des déclencheurs et actions.
- **WP-Cron :** planificateur WordPress dépendant historiquement des visites ; pour une tâche critique, préférer un cron serveur correctement configuré.

Sécuriser les webhooks avec HTTPS, secret/signature, validation du schéma, limitation des droits et protection contre les répétitions.

## 3. LLM et IA générative

Un LLM prédit et génère du langage ; il ne constitue pas une source de vérité. Il peut aider à :

- produire des variantes de titres ou de descriptions ;
- classer des demandes ;
- résumer un dossier ;
- préparer un brouillon de réponse ;
- suggérer des liens internes ou des champs manquants.

Il faut une validation humaine pour les contenus juridiques, techniques, médicaux, financiers ou engageant la marque. Documenter le modèle, le prompt, les sources, la date, le validateur et la version publiée.

## 4. MCP correctement défini

Le **Model Context Protocol** est un standard ouvert permettant à une application d’IA de se connecter de manière structurée à des systèmes externes. Un serveur MCP peut exposer notamment des **outils**, des **ressources** et des **prompts** à un client compatible.

MCP ne remplace ni l’API WordPress ni l’authentification. Il fournit une couche standardisée entre l’application d’IA et les capacités exposées. Un connecteur WordPress pourrait, par exemple, autoriser la lecture des brouillons ou la création d’un article, mais chaque opération doit respecter les permissions et être journalisée.

## 5. Modèle de menace pour une IA connectée

Risques : fuite de données personnelles, prompt injection dans un contenu lu, action excessive, secret exposé, publication erronée et dépendance à un fournisseur.

Garde-fous :

- lecture seule par défaut ;
- outils étroits plutôt qu’accès administrateur général ;
- confirmation humaine avant publication, suppression ou envoi ;
- séparation test/production ;
- liste des champs autorisés et minimisation des données ;
- journaux, quotas, délais d’expiration et révocation des accès ;
- contenu externe traité comme donnée non fiable, jamais comme instruction prioritaire.

## 6. Atelier d’automatisation

Concevoir le flux « formulaire de diagnostic → CRM → attribution commerciale → email → tableau de suivi ».

Le dossier doit contenir : schéma des champs, base légale/consentement, règles de dédoublonnage, secrets utilisés, stratégie d’erreur, responsable et test de bout en bout.

### Exercice MCP

Définir sans le déployer un serveur MCP WordPress avec trois outils : `list_drafts`, `create_draft` et `publish_post`. Pour chacun, préciser entrées, sorties, rôle autorisé, journalisation et validation humaine. La publication doit exiger une approbation explicite.

### Ressources

- [Introduction officielle à MCP](https://modelcontextprotocol.io/docs/getting-started/intro)
- [Architecture MCP](https://modelcontextprotocol.io/docs/learn/architecture)
- [WordPress REST API](https://developer.wordpress.org/rest-api/)
- [Documentation des webhooks WordPress](https://developer.wordpress.org/plugins/http-api/)
- [Documentation Make](https://www.make.com/en/help/home)
- [Documentation n8n](https://docs.n8n.io/)
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [CNIL — développer un système d’IA](https://www.cnil.fr/fr/intelligence-artificielle/guide)

---

# Partie 4 — CMS, headless ou fullstack : décider

**Durée :** 2 à 3 heures

## Objectifs de la partie

- Éviter les oppositions simplistes entre no-code et code.
- Relier le choix d’architecture aux risques métier.
- Produire une recommandation défendable.

## 1. Forces d’un CMS

- Publication rapide et autonomie éditoriale.
- Fonctions standards déjà disponibles.
- Gestion centralisée des médias, utilisateurs et versions.
- Écosystème et coût initial souvent maîtrisé.

## 2. Forces d’une application fullstack

- Modèle métier et parcours entièrement personnalisés.
- Contrôle précis de l’architecture et des performances.
- Meilleure adéquation aux interactions complexes et temps réel.
- Cycle de développement, tests et déploiement sur mesure.

Le fullstack n’est pas automatiquement plus sécurisé ou plus rapide : il transfère davantage de responsabilité à l’équipe qui conçoit et maintient le système.

## 3. Quand choisir quoi ?

| Besoin dominant | Choix probable |
|---|---|
| Site marketing piloté par les équipes contenu | CMS traditionnel |
| Boutique standard avec mise en marché rapide | SaaS e-commerce |
| Même contenu distribué sur site, app et bornes | CMS headless/hybride |
| Application métier avec règles très spécifiques | Fullstack |
| Contenu complexe, permissions et workflow avancés | Drupal ou CMS comparable |
| Marketing autonome avec intégrations courantes | WordPress |

## 4. Questions de décision

- Qui publie, combien de fois et avec quel workflow ?
- Quelles données personnelles ou sensibles sont traitées ?
- Quelles intégrations sont indispensables ?
- Quels objectifs de disponibilité et de reprise ?
- Quel budget sur trois ans ?
- Qui assurera la maintenance après le lancement ?
- Comment exporter contenus, comptes, médias et URLs ?
- Un prototype valide-t-il les hypothèses critiques ?

## 5. Étude de cas

Pour Culture Habitat, un WordPress bien gouverné est cohérent si le besoin principal reste la génération de prospects, le SEO local et l’autonomie marketing. Une application séparée devient pertinente si apparaissent un espace client, des calculs métier complexes, une planification temps réel ou des règles d’accès dépassant raisonnablement le CMS.

### Exercice

Produire une matrice pondérée pour trois architectures. Inclure coût sur trois ans, délai, SEO, autonomie marketing, sécurité, intégrations, performance, maintenance et réversibilité. Terminer par une recommandation et trois risques résiduels.

### Ressources

- [MDN — notions de développement web](https://developer.mozilla.org/fr/docs/Learn_web_development)
- [The Twelve-Factor App](https://12factor.net/fr/)
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
- [Strapi — architecture headless](https://docs.strapi.io/)

---

# Partie 5 — Projet final et plan de progression

**Durée :** 4 heures minimum

## Projet final

Créer sur un environnement de test le prototype d’un site de services comprenant :

- une page d’accueil, trois services et une page locale utile ;
- un modèle de réalisation réutilisable ;
- un formulaire de diagnostic avec consentement ;
- une connexion simulée ou réelle à un CRM ;
- un plan de mesure des conversions ;
- une sauvegarde restaurée en test ;
- un mini-audit SEO, performance, accessibilité et sécurité ;
- une proposition d’usage de l’IA respectant les permissions et la validation humaine.

## Livrables

1. Cahier des besoins et choix du CMS.
2. Carte du contenu et rôles utilisateurs.
3. Prototype accessible uniquement en test ou protégé.
4. Schéma d’automatisation et dictionnaire de données.
5. Rapport d’audit de 3 à 5 pages.
6. Plan de maintenance mensuel et procédure d’incident.

## Grille d’évaluation

| Critère | Points |
|---|---:|
| Pertinence du choix technique | 20 |
| Structure et qualité du contenu | 15 |
| SEO, performance et accessibilité | 20 |
| Sécurité, sauvegarde et gouvernance | 20 |
| Fiabilité de l’automatisation | 15 |
| Documentation et présentation | 10 |

## Parcours conseillé sur quatre semaines

- **Semaine 1 :** vocabulaire, architectures et comparaison des CMS.
- **Semaine 2 :** WordPress, contenu, blocs, thèmes et extensions.
- **Semaine 3 :** SEO, performance, accessibilité, sécurité et sauvegardes.
- **Semaine 4 :** CRM, automatisation, IA, MCP et projet final.

## Checklist professionnelle finale

- [ ] Les objectifs et propriétaires du site sont définis.
- [ ] Le contenu est structuré avant le choix des extensions.
- [ ] Les comptes suivent le moindre privilège et utilisent le MFA.
- [ ] Les sauvegardes ont été restaurées en test.
- [ ] Le site est testé sur mobile, clavier et connexion lente.
- [ ] Les scripts marketing et formulaires respectent la minimisation des données.
- [ ] Les conversions sont testées de bout en bout.
- [ ] Les mises à jour passent par un environnement de staging.
- [ ] Les automatisations possèdent journaux, alertes et traitement d’erreur.
- [ ] Toute action d’IA sensible nécessite une validation explicite.

---

# Glossaire

- **API :** interface permettant à des logiciels de communiquer.
- **CDN :** réseau distribuant des fichiers depuis des serveurs proches des visiteurs.
- **CMS headless :** CMS qui expose le contenu sans imposer l’interface publique.
- **CPT :** type de contenu personnalisé dans WordPress.
- **Hook :** point d’extension sous forme d’action ou de filtre.
- **LLM :** modèle de langage génératif.
- **MCP :** standard ouvert reliant des applications d’IA à des outils et sources externes.
- **MFA :** authentification utilisant plusieurs facteurs.
- **Nonce WordPress :** jeton contribuant à vérifier l’intention d’une requête ; ce n’est pas un mécanisme d’autorisation.
- **RPO/RTO :** perte de données acceptable et délai cible de reprise.
- **Staging :** copie de test séparée de la production.
- **Webhook :** message envoyé automatiquement lors d’un événement.

## Pour aller plus loin

- [Documentation générale WordPress](https://wordpress.org/documentation/)
- [Documentation officielle Drupal](https://www.drupal.org/docs/official_docs)
- [Documentation développeur Shopify](https://shopify.dev/docs)
- [W3C Web Accessibility Initiative](https://www.w3.org/WAI/)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [CNIL — sécurité des données personnelles](https://www.cnil.fr/fr/securite-des-donnees)

> **Conseil pédagogique :** les versions, interfaces et outils évoluent. Vérifier la documentation officielle au moment de chaque mise en œuvre et consigner la date des tests.
