from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_health():
    response = client.get("/api/v1/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}
