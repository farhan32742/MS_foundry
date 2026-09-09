from fastapi.testclient import TestClient
from src.personal_ai.main import app


client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "healthy"
    assert body["environment"] == "development"
    assert body["version"] == "0.1.0"
