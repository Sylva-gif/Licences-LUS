# Chapitre 2 : Pile de protocoles TCP/IP et Adressage IP

## 1. Présentation du protocole TCP/IP

### Origine
- Développé par le **ministère américain de la Défense (DoD)** pour garantir la communication même en cas de guerre.
- Normalisé en **1981**.
- Base de l’Internet moderne.

### Les 4 couches du modèle TCP/IP
1. **Application** : gère les protocoles de haut niveau (FTP, HTTP, SMTP, DNS…).
2. **Transport** : assure la fiabilité et le contrôle de flux (TCP, UDP).
3. **Internet** : sélectionne le meilleur chemin pour les paquets (IP, ICMP, ARP, RARP).
4. **Accès réseau** : définit la liaison physique avec le média (Ethernet, PPP, SLIP).

---

## 2. Comparaison OSI vs TCP/IP

| Modèle OSI (7 couches) | Modèle TCP/IP (4 couches) |
|-------------------------|---------------------------|
| Application             | Application               |
| Présentation            | Application               |
| Session                 | Application               |
| Transport               | Transport                 |
| Réseau                  | Internet                  |
| Liaison de données      | Accès réseau              |
| Physique                | Accès réseau              |

**Différences clés :**
- TCP/IP regroupe **Application + Présentation + Session** en une seule couche.
- TCP/IP regroupe **Physique + Liaison de données** en une seule couche.
- TCP/IP est plus simple et directement utilisé dans les réseaux réels.

---

## 3. L’architecture d’Internet
- Internet = interconnexion de multiples réseaux (LAN, WAN).
- Les routeurs choisissent le meilleur chemin pour acheminer les paquets.
- Objectifs : **évolutivité, robustesse, flexibilité, économie**.

---

## 4. Les adresses Internet

### Adressage IP
- Chaque équipement doit avoir une **adresse IP unique** (adresse logique).
- Adresse IP = 32 bits (IPv4), exprimée en **notation décimale pointée** (ex. `192.168.1.2`).
- Chaque machine possède aussi une **adresse MAC** (adresse physique).

---

### Conversion binaire ↔ décimal
- IP = 32 bits (4 octets).
- Exemple :  
  - `192.168.1.8` → `11000000.10101000.00000001.00001000` (binaire).
  - `00000100 00011101` → `1053` (décimal).

---

### Adressage IPv4
- Adresse = **partie réseau** + **partie hôte**.
- Système hiérarchique (comme un code postal).
- Utilisé pour identifier chaque machine sur un réseau.

---

### Classes d’adresses IPv4

| Classe | Plage du 1er octet | Taille réseau | Nb hôtes |
|--------|--------------------|---------------|----------|
| A      | 1 – 126            | Très grand    | ~16 M    |
| B      | 128 – 191          | Moyen         | ~65 K    |
| C      | 192 – 223          | Petit         | 254      |
| D      | 224 – 239          | Multicast     | -        |
| E      | 240 – 255          | Réservé       | -        |

**Remarques :**
- `127.0.0.0` → réservé pour les tests en boucle locale (loopback).
- Certaines adresses sont réservées pour usages spécifiques.

---

### IP publiques vs privées
- **Publiques** : utilisées sur Internet, attribuées par un fournisseur.
- **Privées** : utilisées en interne (LAN), non routables sur Internet.  
  - Classe A : `10.0.0.0/8`  
  - Classe B : `172.16.0.0/12`  
  - Classe C : `192.168.0.0/16`

---

### IPv4 vs IPv6
- **IPv4** : 32 bits, ~4,3 milliards d’adresses.
- **IPv6** : 128 bits, espace d’adressage quasi illimité.
- IPv6 apporte : sécurité intégrée, meilleure gestion du routage, simplification du NAT.

---

## 5. Obtention d’une adresse IP

### Méthodes
- **Statique** : configurée manuellement.
- **RARP** : obtient une IP à partir d’une adresse MAC.
- **BOOTP** : attribue une IP au démarrage.
- **DHCP** : attribue dynamiquement une IP (le plus utilisé).

### Protocole ARP
- Traduit une **adresse IP** en **adresse MAC**.
- Essentiel pour la communication sur un LAN.

---

## Résumé visuel

| Concept         | IPv4                  | IPv6                  |
|-----------------|-----------------------|-----------------------|
| Taille adresse  | 32 bits               | 128 bits              |
| Nb d’adresses   | ~4,3 milliards        | Quasi illimité        |
| Format          | Décimal pointé        | Hexadécimal           |
| Exemple         | 192.168.1.1           | 2001:0db8::1          |

---

## Ressources professionnelles
- [RFC 791 – IPv4 Specification](https://www.rfc-editor.org/rfc/rfc791)
- [RFC 2460 – IPv6 Specification](https://www.rfc-editor.org/rfc/rfc2460)
- [IANA – IPv4/IPv6 Address Space](https://www.iana.org/assignments/ip-addresses/ip-addresses.xhtml)
- [Cisco Networking Academy – TCP/IP Protocol Suite](https://www.netacad.com/)
