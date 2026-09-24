from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

out = Path(__file__).parent / "sorties"
out.mkdir(exist_ok=True)
df = pd.DataFrame(
    {
        "jour": [0, 7, 14, 0, 7, 14],
        "poids_kg": [180, 185.6, 191.2, 160, 161.75, 163.5],
        "animal": ["A"] * 3 + ["B"] * 3,
    }
)
fig, ax = plt.subplots(figsize=(7, 4))
for animal, part in df.groupby("animal"):
    ax.plot(part.jour, part.poids_kg, marker="o", label=animal)
ax.set(
    xlabel="Temps (jours)",
    ylabel="Poids (kg)",
    title="Croissance synthétique — 2 animaux, 6 pesées",
)
ax.legend()
fig.tight_layout()
fig.savefig(out / "croissance.png", dpi=160)
plt.close(fig)
fig, ax = plt.subplots(figsize=(7, 4))
sns.scatterplot(
    data=df, x="jour", y="poids_kg", hue="animal", style="animal", ax=ax, s=90
)
ax.set(
    xlabel="Temps (jours)",
    ylabel="Poids (kg)",
    title="Observations individuelles — données synthétiques",
)
fig.tight_layout()
fig.savefig(out / "observations.png", dpi=160)
plt.close(fig)
print("Figures :", out)
