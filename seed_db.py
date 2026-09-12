from sqlalchemy import select

from database import SessionLocal
from db_models import OrderRecord


def seed_and_show_orders() -> None:
    sample_orders = [
        OrderRecord(
            order_id="1001",
            user_id="U001",
            product="蓝牙耳机",
            amount=299.0,
            status="已发货",
        ),
        OrderRecord(
            order_id="1002",
            user_id="U002",
            product="机械键盘",
            amount=459.0,
            status="待付款",
        ),
    ]

    with SessionLocal() as session:
        added_count = 0

        for order in sample_orders:
            existing_order = session.get(
                OrderRecord,
                order.order_id,
            )

            if existing_order is None:
                session.add(order) #告诉Session准备新增
                added_count += 1

        session.commit() #正式写入数据库

        statement = select(OrderRecord).order_by(
            OrderRecord.order_id
        )
        orders = session.scalars(statement).all()

        print(f"本次新增 {added_count} 条订单")
        print(f"数据库共有 {len(orders)} 条订单")

        for order in orders:
            print(
                order.order_id,
                order.product,
                order.amount,
                order.status,
            )


if __name__ == "__main__":
    seed_and_show_orders()