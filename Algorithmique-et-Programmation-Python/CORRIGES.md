# Corrections commentées des travaux pratiques

Ces corrections donnent le raisonnement et les résultats attendus. Les scripts complets sont dans `exemples/`, les tests d'intégration dans `projet-elevage/tests/`. Commencer par sa propre solution avant comparaison.

## TP 01

Sommes successives : 100, 210, 330, 460 kg. Quatre valeurs donnent 460/4 = **115 kg**, soit 115 000 g de masse moyenne. La masse totale est 460 000 g. Pour une liste vide, la division est impossible : retourner une absence ou lever une erreur selon le contrat. Le parcours traite chaque valeur une fois : O(n).

## TP 02

Initialiser un dictionnaire vide. Pour chaque couple bâtiment/mesure, compter `None` séparément ; si la valeur dépasse strictement 30, incrémenter `alertes[batiment]` avec `.get(batiment,0)+1`. Résultat : **A : 2 alertes**, une absence. B n'a pas d'alerte ; son absence ne signifie pas 0 °C. Une boucle sur m bâtiments contenant une boucle sur n mesures coûte O(mn), contre O(n) ici.

## TP 03

`(185.6-180)×1000/7` donne environ **800 g/j**. `(179.3-180)×1000/7` donne **−100 g/j** : une perte ne doit pas être tronquée à zéro. Durée nulle : `ValueError`. Les valeurs NaN perturbent les comparaisons ; `math.isfinite` rejette explicitement NaN et infini. Les annotations de type ne constituent pas une validation runtime.

## TP 04

Chaque instance doit disposer de sa propre liste, obtenue par `field(default_factory=list)`. Rechercher une date déjà présente avant l'ajout. Pour les temps : une tâche possède zéro ou plusieurs sessions ; chaque session appartient à une seule tâche. Les sessions contiennent une date de début et une durée, tandis que le cumul est une valeur dérivée.

## TP 05

La ligne d'humidité à 101 % invalide le lot avant écriture. Un doublon détecté par SQLite lève `IntegrityError` pendant la transaction ; sa propagation hors de `with connection` provoque le rollback. Dans les deux cas, le nombre de nouvelles mesures doit être **0**. La transaction protège la cohérence d'un lot, tandis que la sauvegarde permet de restaurer une version après perte ou erreur ultérieure.

## TP 06

Après suppression de l'unique valeur manquante : moyenne des lignes = `(180+185.6+160)/3` = **175,2 kg**. Moyenne A = 182,8 ; moyenne B = 160 ; moyenne des deux animaux = **171,4 kg**. Les réponses diffèrent car A est mesuré deux fois. Une table de métadonnées avec une ligne unique par animal permet une jointure `many_to_one` sans augmentation des lignes.

## TP 07

La courbe montre l'évolution temporelle ; le nuage rend visibles les observations individuelles. Le point extrême augmente la moyenne plus fortement que la médiane, mais ne doit pas être supprimé sans justification. Pour une interprétation honnête : mêmes unités, dates réelles, source synthétique et effectif annoncé. Les sorties attendues sont `croissance.png` et `observations.png`.

## TP 08

La droite régularisée doit faire mieux que la baseline dernière valeur sur la série synthétique livrée ; le script vérifie cette propriété. La valeur exacte de MAE peut légèrement dépendre des versions. Une feature de futur poids, un total alimentaire calculé après la prédiction ou une normalisation sur tout le dataset créent une fuite. Grouper les lignes d'un animal dans un même ensemble est nécessaire pour évaluer de nouveaux individus ; ce split répond à une question différente d'un split temporel.

## TP 09

Entrée et sortie ont les formes `(n,1)` ; le réseau possède une couche cachée de 8 unités. Les 24 premières observations entraînent, les 6 suivantes valident et les 10 dernières testent. Le réseau peut mieux interpoler que prévoir au-delà du domaine observé. Une erreur train faible peut venir d'une capacité excessive ; elle ne suffit pas. Ne pas exiger une MAE exacte identique entre backends. Le modèle linéaire est une baseline particulièrement adaptée à `y=2x+1`.

## TP 10

Source IP : **192.0.2.10** ; destination : **192.0.2.20** ; port UDP de destination : **12001** ; charge utile : `temperature=24.5`. L'objet est construit et décodé en mémoire. Le token altéré doit lever `InvalidToken`. Une clé correcte prouve une propriété cryptographique du message, pas l'étalonnage ni la localisation réelle du capteur.

## TP 11

La requête valide reçoit **200** ; l'humidité à 150 et la date sans fuseau reçoivent **422** avec FastAPI. La route Flask renvoie `status='ok'`. Une clé métier possible pour l'ingestion est `(sensor_id, measured_at)` ; le modèle minimal livré utilise seulement bâtiment/horodatage. Une retransmission doit retourner le résultat existant ou un conflit explicite, sans doubler une observation. Cette politique doit être testée au stockage, pas seulement au client HTTP.

## TP 12

Le simulateur crée six mesures, espacées de cinq minutes, pour Atelier A. Les dates sont en UTC et la dernière est récente. Le CSV importé est étiqueté « CSV », le bouton de simulation « simulation ». Une donnée datant de plus de 30 minutes déclenche une alerte de fraîcheur. L'ESP32 lit le capteur ; la passerelle gère le transport, l'identité et l'horloge ; Qt affiche les données validées.

## TP 13

τ = 1 000 × 100×10⁻⁶ = **0,1 s**. À τ : `5(1−e⁻¹)` = **3,1606028 V**. Doubler R double τ à 0,2 s et ralentit la charge. Le filtre `sosfiltfilt` utilise des observations futures dans sa passe arrière ; il ne peut pas servir tel quel à une alerte en direct. Une version causale doit maintenir l'état du filtre et accepter son retard.

## TP 14

Exemple de fonction pure :

```python
def productivite(taches_terminees: int, secondes: float):
    if taches_terminees < 0 or secondes < 0:
        raise ValueError("Valeurs négatives interdites")
    return None if secondes == 0 else taches_terminees / (secondes / 3600)

assert productivite(3, 5400) == 2.0
assert productivite(0, 0) is None
```

Trois tâches en 1,5 h donnent **2 tâches/h**. Cette métrique ne compare pas équitablement des tâches de difficultés différentes : le rapport doit signaler cette limite. L'interface appelle la fonction avec les agrégats du stockage ; la fonction n'importe ni Qt ni SQLite.
