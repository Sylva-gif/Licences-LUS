from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/etat")
def state():
    return jsonify(service="elevage-tp", status="ok")


if __name__ == "__main__":
    with app.test_client() as client:
        response = client.get("/etat")
        assert response.status_code == 200 and response.json["status"] == "ok"
    print("Flask : route de lecture vérifiée, aucun serveur lancé")
