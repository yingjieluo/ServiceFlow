from dataclasses import dataclass
# Order = dict[str, str | float]
# # 一条订单 = 键为str、值为str或float的字典

# 定义数据类：
@dataclass
class Order:
    order_id: str
    user_id: str
    product: str
    amount: float
    status: str
