from dataclasses import asdict
from typing import Any

from models import Order
from  order_query import find_order

def build_order_response(orders: list[Order],order_id: str,) -> tuple[int, dict[str, Any]]:
    """模拟查询订单API的响应。"""

    #第一步，先查询，得到Order对象或者None
    order = find_order(orders,order_id)

    #第二步，判断是否没找到
    if order is None:
        return 404, {
            "error": {
                "code": "ORDER_NOT_FOUND",
                "message": "订单不存在",
                        }
            }
    
    #第三步，执行到这里，说明找到了订单
    return 200, {
        "data":asdict(order)
        }
