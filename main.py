from typing import Annotated

from fastapi import Depends,FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from database import get_db
from order_repository import find_order_record
from schemas import OrderData,OrderResponse

app = FastAPI(
    title="ServiceFlow",
    description="电商售后 AI 客服 Agent",
)

SessionDep = Annotated[Session, Depends(get_db)]

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
# 路由是什么？
# 路由就是：
# 某种HTTP方法和某个网址，应该由哪个Python函数处理。
# 上面这个@app.get("/health")建立的路由就是GET /health → health_check()

@app.get(
        "/orders/{order_id}",
        response_model=OrderResponse,
    )
def get_order(order_id: str, session: SessionDep,) -> OrderResponse | JSONResponse:
   
    order = find_order_record(session, order_id)

    if order is None:
        return JSONResponse(
            status_code=404,
            content={
                "error": {
                    "code": "ORDER_NOT_FOUND",
                    "message": "订单不存在",
                }
            },
        )

    order_data = OrderData.model_validate(order)
    return OrderResponse(data=order)


