from api_contract import build_order_response
from models import Order
import json

def test_existing_order_returns_200() -> None:
    orders = [
        Order(
            order_id="1001",
            user_id="U001",
            product="机械键盘",
            amount=299.0,
            status="已支付",
        )
    ]

    status_code, body = build_order_response(orders, "1001")

    assert status_code == 200
    assert body["data"]["order_id"] == "1001"
    assert body["data"]["product"] == "机械键盘"

def test_missing_order_returns_404() -> None:
    orders = [
        Order(
            order_id="1001",
            user_id="U001",
            product="机械键盘",
            amount=299.0,
            status="已支付",
        )
    ]

    status_code, body = build_order_response(orders, "9999")

    assert status_code == 404
    assert body["error"]["code"] == "ORDER_NOT_FOUND"
    assert body["error"]["message"] == "订单不存在"

def test_response_can_round_trip_json() -> None:
    orders = [
        Order(
            order_id="1001",
            user_id="U001",
            product="机械键盘",
            amount=299.0,
            status="已支付",
        )
    ]

    status_code, body = build_order_response(orders, "1001")

    json_text = json.dumps(body, ensure_ascii=False)
    restored_body = json.loads(json_text)

    assert status_code == 200
    assert isinstance(json_text, str)
    assert isinstance(restored_body, dict)
    assert restored_body["data"]["order_id"] == "1001"
    assert restored_body["data"]["product"] == "机械键盘"