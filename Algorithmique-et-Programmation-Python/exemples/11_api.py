"""API de TP non persistante ; exécution directe = tests sans serveur exposé."""

from datetime import datetime
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field, field_validator

app = FastAPI(title="Contrat de mesure — TP local")


class Measurement(BaseModel):
    barn: str = Field(min_length=1, max_length=120)
    measured_at: datetime
    temperature: float = Field(ge=-50, le=70, allow_inf_nan=False)
    humidity: float = Field(ge=0, le=100, allow_inf_nan=False)

    @field_validator("measured_at")
    @classmethod
    def timezone_required(cls, value):
        if value.tzinfo is None:
            raise ValueError("Fuseau horaire requis")
        return value


@app.post("/mesures")
def accept(data: Measurement):
    return {"acceptee": True, "mesure": data.model_dump()}


if __name__ == "__main__":
    payload = {
        "barn": "A",
        "measured_at": "2026-01-01T12:00:00Z",
        "temperature": 24.5,
        "humidity": 60,
    }
    with TestClient(app) as client:
        assert client.post("/mesures", json=payload).status_code == 200
        assert (
            client.post("/mesures", json={**payload, "humidity": 150}).status_code
            == 422
        )
        assert (
            client.post(
                "/mesures", json={**payload, "measured_at": "2026-01-01T12:00:00"}
            ).status_code
            == 422
        )
    print("API : contrat et refus de valeurs invalides vérifiés")
