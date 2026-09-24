import numpy as np
import pandas as pd

df = pd.DataFrame(
    {"animal": ["A", "A", "B", "B"], "poids_kg": [180, 185.6, 160, np.nan]}
)
valides = df.dropna(subset=["poids_kg"])
par_animal = valides.groupby("animal")["poids_kg"].agg(["mean", "count"])
print("Lignes exclues :", len(df) - len(valides))
print(par_animal)
print("Moyenne des observations :", valides["poids_kg"].mean())
print("Moyenne des moyennes par animal :", par_animal["mean"].mean())
assert np.isclose(par_animal["mean"].mean(), 171.4)
meta = pd.DataFrame({"animal": ["A", "B"], "batiment": ["Nord", "Sud"]})
jointure = valides.merge(meta, on="animal", validate="many_to_one")
assert len(jointure) == len(valides)
