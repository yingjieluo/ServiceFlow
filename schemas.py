from pydantic import BaseModel, ConfigDict


class OrderData(BaseModel):
    # """服务器返回给客户端的订单数据"""
    model_config = ConfigDict(from_attributes=True)
    # from_attributes=True就是告诉Pydantic：
    # 可以从SQLAlchemy对象的属性中读取数据。
    order_id: str
    user_id: str
    product: str
    amount: float
    status: str


class OrderCreate(BaseModel):
    #  """客户端创建订单时提交的数据"""
    order_id: str
    user_id: str
    product: str
    amount: float
    status: str

class OrderResponse(BaseModel):
    data: OrderData