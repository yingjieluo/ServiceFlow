# 数据库查询层
from sqlalchemy.orm import Session

from db_models import OrderRecord


def find_order_record(
    session: Session,
    order_id: str,
) -> OrderRecord | None:
    return session.get(OrderRecord, order_id)