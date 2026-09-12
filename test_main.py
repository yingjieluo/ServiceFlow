from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_existing_order() -> None:
    response = client.get("/orders/1001")

    assert response.status_code == 200

    body = response.json()

    assert body["data"]["order_id"] == "1001"
    assert body["data"]["product"] == "蓝牙耳机"


def test_get_missing_order() -> None:
    response = client.get("/orders/9999")

    assert response.status_code == 404
    assert response.json()["error"]["code"] == "ORDER_NOT_FOUND"