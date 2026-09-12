from collections.abc import Generator

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from database import Base, get_db
from db_models import OrderRecord
from main import app


test_engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(bind=test_engine)

Base.metadata.create_all(bind=test_engine)


with TestingSessionLocal() as session:
    session.add_all(
        [
            OrderRecord(
                order_id="1001",
                user_id="U001",
                product="蓝牙耳机",
                amount=299.0,
                status="已发货",
            ),
            OrderRecord(
                order_id="1002",
                user_id="U002",
                product="机械键盘",
                amount=459.0,
                status="待付款",
            ),
        ]
    )
    session.commit()


def override_get_db() -> Generator[Session, None, None]:
    with TestingSessionLocal() as session:
        yield session


app.dependency_overrides[get_db] = override_get_db

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