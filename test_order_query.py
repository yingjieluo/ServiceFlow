from models import Order
from order_query import find_order

TEST_ORDERS: list[Order] = [
    Order(
        order_id="1001",
        user_id="U001",
        product="蓝牙耳机",
        amount=299.0,
        status="已发货",
    ),
    Order(
        order_id="1002",
        user_id="U002",
        product="机械键盘",
        amount=459.0,
        status="待付款",
    ),
]

def test_find_order_existing() -> None:
    result = find_order(TEST_ORDERS, "1002")

    assert result is not None
    assert result.product == "机械键盘"
    assert result.amount == 459.0
    assert result.status == "待付款"

def test_find_missing_order() -> None:
    result = find_order(TEST_ORDERS, "9999")

    assert result is None