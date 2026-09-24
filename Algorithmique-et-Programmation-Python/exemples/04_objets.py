from dataclasses import dataclass, field
from datetime import date
from math import isfinite


@dataclass(frozen=True)
class Pesee:
    jour: date
    poids_kg: float


@dataclass
class Animal:
    identifiant: str
    pesees: list[Pesee] = field(default_factory=list)

    def ajouter(self, pesee):
        if not isfinite(pesee.poids_kg) or pesee.poids_kg <= 0:
            raise ValueError("Poids invalide")
        if any(p.jour == pesee.jour for p in self.pesees):
            raise ValueError("Date déjà présente")
        self.pesees.append(pesee)


a, b = Animal("A"), Animal("B")
a.ajouter(Pesee(date(2026, 1, 1), 180))
assert len(a.pesees) == 1 and not b.pesees
print(a, b)
