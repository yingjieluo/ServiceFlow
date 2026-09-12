from pydantic import BaseModel


class OrderData(BaseModel):
    order_id: str
    user_id: str
    product: str
    amount: int
    status: str


class OrderResponse(BaseModel):
    data: OrderData