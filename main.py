from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Any
from schemas import OrderResponse
from api_contract import build_order_response
from order_query import load_orders


app = FastAPI(
    title="ServiceFlow",
    description="电商售后 AI 客服 Agent",
)

ORDERS = load_orders("orders.json")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get(
        "/orders/{order_id}",
        response_model=OrderResponse,
    )
def get_order(order_id: str) -> dict[str, Any] | JSONResponse:
    status_code, body = build_order_response(ORDERS, order_id)

    if status_code == 404:
        return JSONResponse(
            status_code=status_code,
            content=body,
        )
    return body
