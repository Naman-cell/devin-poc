import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.services.users import user_service

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_users() -> None:
    user_service.clear()


def test_create_user_returns_created_user() -> None:
    response = client.post("/users", json={"name": "Naman", "email": "naman@example.com"})

    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "Naman", "email": "naman@example.com"}


def test_ids_increment_per_user() -> None:
    first = client.post("/users", json={"name": "Naman", "email": "naman@example.com"})
    second = client.post("/users", json={"name": "Ada", "email": "ada@example.com"})

    assert first.json()["id"] == 1
    assert second.json()["id"] == 2


def test_duplicate_email_returns_409() -> None:
    client.post("/users", json={"name": "Naman", "email": "naman@example.com"})
    response = client.post("/users", json={"name": "Other", "email": "NAMAN@example.com"})

    assert response.status_code == 409


def test_invalid_email_returns_422() -> None:
    response = client.post("/users", json={"name": "Naman", "email": "not-an-email"})

    assert response.status_code == 422


def test_health_still_ok() -> None:
    assert client.get("/health").json() == {"status": "ok"}
