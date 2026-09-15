from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from database import get_db
from order_repository import create_order, find_order_record
from schemas import OrderCreate, OrderData, OrderResponse


app = FastAPI(
    title="ServiceFlow",
    description="电商售后 AI 客服 Agent",
)


SessionDep = Annotated[Session, Depends(get_db)]


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get(
    "/orders/{order_id}",
    response_model=OrderResponse,
)
def get_order(
    order_id: str,
    session: SessionDep,
) -> OrderResponse | JSONResponse:
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
    return OrderResponse(data=order_data)


@app.post(
    "/orders",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_new_order(
    order_create: OrderCreate,
    session: SessionDep,
) -> OrderResponse:
    existing_order = find_order_record(
        session,
        order_create.order_id,
    )

    if existing_order is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={
                "code": "ORDER_ALREADY_EXISTS",
                "message": "订单已存在",
            },
        )

    new_order = create_order(session, order_create)
    order_data = OrderData.model_validate(new_order)

    return OrderResponse(data=order_data)