"""Variables, calcul et contrat élémentaire. Bibliothèque standard uniquement."""

poids_kg = [100, 110, 120, 130]
total = 0
for valeur in poids_kg:
    total += valeur
    print(f"Valeur : {valeur} kg ; cumul : {total} kg")
moyenne = total / len(poids_kg) if poids_kg else None
assert moyenne == 115
print(f"Moyenne : {moyenne} kg ; masse totale : {total*1000} g")
