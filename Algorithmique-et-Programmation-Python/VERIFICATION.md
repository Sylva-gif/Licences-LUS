# Vérification du livrable

Date : **24 septembre 2026**. Environnement d'exécution : Linux, Python **3.12.14**, rendu Qt hors écran. Les résultats suivants distinguent les essais réellement exécutés des validations qui demandent une autre plateforme.

## Application PyQt5

**16 tests automatisés réussis** avec `python -m unittest discover -s tests -v` : GMQ et tri, dates dupliquées, données insuffisantes, poids non finis, IC sur une fenêtre complète, perte de poids, droite connue, persistance, contraintes SQL, import atomique, fuseaux, temps, échappement CSV, ancienneté des capteurs, démonstration intégrée et fermeture du chronomètre dans Qt.

`main.py --db :memory: --demo --smoke` a démarré puis fermé l'interface. Une capture du tableau de bord a été examinée : onglets, GMQ **800 g/j**, IC **5 kg/kg**, courbe et alerte visibles. Ce test n'est pas un essai manuel sur Windows ou macOS ; ces plateformes doivent être validées lors de leur première installation.

## Exemples

| Exemple | Résultat |
|---|---|
| 01 à 05 : bases, collections, fonctions, objets, stockage | Exécutés, assertions réussies |
| 06 : DataFrame | Moyenne des lignes 175,2 kg ; moyenne par animal 171,4 kg |
| 07 : visualisation | Deux figures PNG produites sans écran |
| 08 : scikit-learn | MAE modèle ≈ 0,684 kg ; baseline ≈ 5,052 kg |
| 09 : PyTorch et TensorFlow | Syntaxe contrôlée ; backends optionnels non installés, entraînements non exécutés |
| 10 : Cryptography | Chiffrement/déchiffrement et rejet d'altération vérifiés séparément |
| 10 : Scapy | Exécution bloquée à l'import par l'interdiction d'accès aux interfaces réseau de l'environnement ; aucun paquet émis |
| 11 : FastAPI, Flask, Django | Clients de test exécutés ; validation HTTP, route JSON et ORM vérifiés |
| 12 : simulateur IoT | CSV de six mesures produit |
| 12 : ESP32 et Raspberry Pi | Syntaxe contrôlée ; absence de matériel, acquisition non testée |
| 13 : SciPy | Solveurs réussis ; RC à τ ≈ 3,160603 V ; écart à la solution exacte < 10⁻⁶ V |

L'import de Scapy peut initialiser les interfaces réseau même si le script se limite aux paquets en mémoire. Le blocage est lié aux permissions de ce conteneur ; le TP doit être exécuté sur un poste de laboratoire approprié. Il n'a pas été contourné. Le client de test FastAPI a émis un avertissement de dépréciation de son adaptateur HTTPX avec les versions présentes ; les assertions ont réussi.

## Versions utilisées pour la vérification

| Paquet | Version |
|---|---|
| PyQt5 | 5.15.11 |
| NumPy | 2.3.5 |
| Pandas | 2.2.3 |
| SciPy | 1.17.0 |
| scikit-learn | 1.8.0 |
| Matplotlib | 3.10.8 |
| Seaborn | 0.13.2 |
| Cryptography | 46.0.0 |
| Scapy | 2.7.0, import bloqué |
| FastAPI | 0.141.1 |
| Flask | 3.1.3 |
| Django | 5.2.17 |

## Documents et figures

Le script `python outils/verifier_contenu.py` vérifie les cibles des liens internes, la syntaxe des scripts et des blocs Python, la validité XML des SVG et la présence d'un TP/illustration dans chaque chapitre. Les **14 figures SVG** ont été rendues et examinées en planche contact. Le diagramme UML et le modèle de données sont également fournis en Mermaid dans les documents.

Les références externes sont des liens documentaires, dont les guides principaux ont été consultés ; elles n'ont pas toutes été soumises à un vérificateur de liens automatisé. Aucun certificat industriel, aucune validation zootechnique et aucune certification de modèle ne sont revendiqués.

## Reproduire

```bash
# Depuis le dossier du module
python outils/verifier_contenu.py
cd projet-elevage
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python main.py --db :memory: --demo --smoke
```

Sur serveur sans écran, définir `QT_QPA_PLATFORM=offscreen` pour les commandes Qt. Pour la procédure utilisateur Windows, se reporter au README du projet.
