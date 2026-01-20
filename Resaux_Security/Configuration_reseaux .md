# Module 5 : Configuration d’un routeur

## Objectifs
À la fin de ce module, vous devez être capable de :
- Nommer un routeur.
- Définir des mots de passe (console, Telnet, enable).
- Examiner les commandes **show** pour le diagnostic.
- Configurer une interface série et Ethernet.
- Apporter des modifications et les sauvegarder.
- Créer des descriptions d’interface.
- Configurer une bannière (Message of the Day).
- Configurer des tables d’hôtes.
- Comprendre l’importance des sauvegardes et de la documentation.

---

## 5.1 Configuration d’un routeur

### 5.1.1 Modes de commande CLI
Un routeur Cisco fonctionne avec différents **modes CLI** (Command Line Interface) :

- **Mode utilisateur** : accès limité, consultation basique.
- **Mode privilégié** : accès complet aux commandes de diagnostic.
- **Mode configuration globale** : permet de modifier la configuration du système entier.
- **Modes spécifiques** (sous-ensembles du mode global) :
  - Mode interface
  - Mode ligne (console, VTY)
  - Mode routeur
  - Mode sous-interface
  - Mode contrôleur

**Commandes clés :**
```bash
Router#configure terminal
Router(config)#
## Configuration du nom d’un routeur
Router(config)#hostname Tokyo
Tokyo(config)#

## Configuration des mots de passe
Router(config)#line console 0
Router(config-line)#password monpass
Router(config-line)#login
 ##Commandes show
Router#show interfaces
Router#show controllers serial 0/1
Router#show clock
Router#show hosts
Router#show users
Router#show history
Router#show flash
Router#show version
Router#show arp
Router#show protocols
Router#show startup-config
Router#show running-config

###
