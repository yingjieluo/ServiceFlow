# 定义订单表
from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class OrderRecord(Base):
    __tablename__ = "orders"

    order_id: Mapped[str] = mapped_column(
        String(50),
        primary_key=True,
    )
    user_id: Mapped[str] = mapped_column(String(50))
    product: Mapped[str] = mapped_column(String(200))
    amount: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String(50))

    def __repr__(self) -> str:
        return (
            f"OrderRecord("
            #OrderRecord是什么？OrderRecord  → SQLAlchemy数据库模型
            #它是“数据库中的订单模型”。一个OrderRecord对象对应orders表中的一行。
            f"order_id={self.order_id!r}, "
            f"product={self.product!r}"
            f")"
        )