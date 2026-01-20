# Chapitre 3 : Notions de base sur le routage et les sous-réseaux

## 1. Protocole routé

### Définition
- Un **protocole** = ensemble de règles pour échanger des messages entre ordinateurs.
- **Protocole routé** : permet au routeur de transmettre des données entre différents réseaux.
- **Protocole routable** : doit inclure une partie réseau et une partie hôte dans l’adresse IP.

### Exemple
- **IP** : protocole routé le plus utilisé.
- Non orienté connexion, best-effort delivery (pas de garantie de livraison).
- Encapsulation des données en **paquets IP** (datagrammes).

---

## 2. Propagation d’un paquet et rôle du routeur
- À chaque saut, les **trames de couche 2** sont retirées et remplacées.
- Le routeur vérifie l’adresse MAC et l’adresse IP de destination.
- Si l’adresse correspond → données transmises à la couche supérieure.
- Sinon → recherche dans la **table de routage** et envoi vers l’interface appropriée.

---

## 3. Transmission orientée vs non orientée connexion
- **Non orientée connexion** : pas de circuit établi, les paquets peuvent suivre des chemins différents (ex. IP).
- **Orientée connexion** : une connexion est établie avant le transfert, tous les paquets suivent le même chemin (ex. TCP).

---

## 4. Anatomie d’un paquet IP
Champs principaux :
- **Version** : IPv4 ou IPv6.
- **HLEN** : longueur de l’en-tête.
- **Type de service (ToS)** : priorité.
- **Longueur totale** : taille du paquet.
- **Identification + fragmentation** : gestion des fragments.
- **TTL (Time To Live)** : nombre de sauts maximum.
- **Protocole** : indique la couche supérieure (TCP, UDP).
- **Adresse source / destination** : IP de l’émetteur et du destinataire.
- **Checksum** : vérification d’intégrité.

---

## 5. Protocoles de routage IP

### Vue d’ensemble
- Le **routage** = fonction de la couche 3 (réseau).
- Le **routeur** choisit le chemin optimal grâce aux **tables de routage**.

### Routage vs commutation
- **Commutateur (switch)** : couche 2, utilise les adresses MAC.
- **Routeur** : couche 3, utilise les adresses IP.
- Routeur bloque les broadcasts → meilleure sécurité et gestion de bande passante.

---

### Protocole routé vs protocole de routage
- **Protocole routé** : transporte les données (IP, IPX, AppleTalk…).
- **Protocole de routage** : aide les routeurs à choisir le meilleur chemin (RIP, OSPF, BGP, EIGRP…).

---

### Détermination du chemin
- Routes **statiques** : configurées manuellement.
- Routes **dynamiques** : apprises via protocoles de routage.
- Processus : comparaison IP destination ↔ table de routage → choix du port de sortie.

---

### Tables de routage
Contiennent :
- Type de protocole.
- Saut suivant.
- Métriques (nombre de sauts, délai, bande passante…).
- Interface de sortie.

---

### Algorithmes et métriques
Objectifs :
- **Optimisation** : choisir le meilleur chemin.
- **Simplicité** : traitement rapide.
- **Stabilité** : résister aux défaillances.
- **Flexibilité** : s’adapter aux changements.
- **Convergence rapide** : accord entre routeurs sur les routes disponibles.

---

## 6. Sous-réseaux

### Classes d’adresses IP
- Classe A : grands réseaux.
- Classe B : réseaux moyens.
- Classe C : petits réseaux.
- Classe D : multicast.
- Classe E : réservé.

### Découpage en sous-réseaux
- Utilisation d’un **masque de sous-réseau** pour séparer partie réseau et partie hôte.
- Permet de diviser un réseau en plusieurs sous-réseaux plus petits.

### Calcul du sous-réseau
- Opération **AND logique** entre adresse IP et masque.
- Exemple :  
  - IP : `192.168.1.10`  
  - Masque : `255.255.255.0`  
  - Résultat (réseau) : `192.168.1.0`

---


## Principe du découpage en sous-réseaux
- On **emprunte des bits** de la partie hôte pour les réattribuer à la partie réseau.
- Cela permet de créer plusieurs sous-réseaux à partir d’un réseau principal.
- Chaque sous-réseau a :
  - Une **adresse réseau** (première adresse).
  - Une **adresse de broadcast** (dernière adresse).
  - Des **adresses utilisables** pour les hôtes (entre les deux).

---

##  Formules essentielles

- **Nombre total de sous-réseaux** = \(2^{n}\)  
  (où \(n\) = nombre de bits empruntés)

- **Sous-réseaux utilisables** = \(2^{n} - 2\)  
  (on retire l’adresse réseau et l’adresse broadcast)

- **Nombre total d’hôtes par sous-réseau** = \(2^{m}\)  
  (où \(m\) = nombre de bits restants pour la partie hôte)

- **Hôtes utilisables par sous-réseau** = \(2^{m} - 2\)  
  (on retire l’adresse réseau et l’adresse broadcast)

---

## Exemple pratique (Classe C)

### Données
- Adresse réseau : `192.168.10.0`
- Masque par défaut : `255.255.255.0` (/24)
- On **emprunte 3 bits** pour créer des sous-réseaux.

### Calculs
- Sous-réseaux utilisables = \(2^3 - 2 = 6\)
- Hôtes utilisables par sous-réseau = \(2^5 - 2 = 30\)

### Nouveau masque
- Masque = `255.255.255.224` (/27)

### Résultats
- **Sous-réseau 0** :  
  - Adresse réseau : `192.168.10.0`  
  - Broadcast : `192.168.10.31`  
  - Plage hôtes : `192.168.10.1` → `192.168.10.30`

- **Sous-réseau 1** :  
  - Adresse réseau : `192.168.10.32`  
  - Broadcast : `192.168.10.63`  
  - Plage hôtes : `192.168.10.33` → `192.168.10.62`

- **Sous-réseau 2** :  
  - Adresse réseau : `192.168.10.64`  
  - Broadcast : `192.168.10.95`  
  - Plage hôtes : `192.168.10.65` → `192.168.10.94`

👉 Et ainsi de suite jusqu’au sous-réseau 7 (mais seuls 6 sont utilisables).

---

##  Exemple pratique (Classe B)

### Données
- Adresse réseau : `172.16.0.0`
- Masque par défaut : `255.255.0.0` (/16)
- On **emprunte 12 bits**.

### Calculs
- Sous-réseaux utilisables = \(2^{12} - 2 = 4094\)
- Hôtes utilisables par sous-réseau = \(2^{4} - 2 = 14\)

### Nouveau masque
- Masque = `255.255.255.240` (/28)

---

## 5. Étapes pour calculer un sous-réseau

1. Identifier la **classe d’adresse** (A, B, C).
2. Déterminer le **masque par défaut**.
3. Décider du nombre de **sous-réseaux** ou d’**hôtes** nécessaires.
4. Calculer le nombre de bits à emprunter.
5. Appliquer les formules :
   - Sous-réseaux utilisables = \(2^n - 2\)
   - Hôtes utilisables = \(2^m - 2\)
6. Écrire le **nouveau masque**.
7. Lister les adresses réseau, broadcast et plages d’hôtes.

---

## Résumé visuel

| Classe | Masque par défaut | Bits empruntés | Nouveau masque | Sous-réseaux utilisables | Hôtes utilisables |
|--------|-------------------|----------------|----------------|--------------------------|-------------------|
| A      | /8                | 20             | /28            | 1 048 574                | 14                |
| B      | /16               | 12             | /28            | 4094                     | 14                |
| C      | /24               | 3              | /27            | 6                        | 30                |

---

## Résumé visuel

| Concept                  | Explication simple |
|---------------------------|--------------------|
| Protocole routé           | Transporte les données (IP) |
| Protocole de routage      | Aide les routeurs à choisir le chemin (RIP, OSPF…) |
| Routage                  | Couche 3, basé sur IP |
| Commutation              | Couche 2, basé sur MAC |
| Sous-réseau              | Division d’un réseau en segments plus petits |
| Masque de sous-réseau     | Sépare partie réseau et partie hôte |

---

## Ressources professionnelles
- [RFC 791 – IPv4 Specification](https://www.rfc-editor.org/rfc/rfc791)
- [RFC 2328 – OSPF Routing Protocol](https://www.rfc-editor.org/rfc/rfc2328)
- [RFC 4271 – BGP-4](https://www.rfc-editor.org/rfc/rfc4271)
- [Cisco Networking Academy – Routing Basics](https://www.netacad.com/)
