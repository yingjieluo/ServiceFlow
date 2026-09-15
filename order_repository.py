# 数据库查询层
from sqlalchemy.orm import Session

from db_models import OrderRecord
from schemas import OrderCreate

from db_models import OrderRecord

def find_order_record(
    session: Session,
    order_id: str,
) -> OrderRecord | None:
    return session.get(OrderRecord, order_id)

def create_order(
    db: Session,
    order_data: OrderCreate,
) -> OrderRecord:
    db_order = OrderRecord(**order_data.model_dump())

    db.add(db_order)#把新对象放进当前Session，准备写入；
    db.commit()     #提交事务，真正保存；
    db.refresh(db_order)#重新从数据库读取这一行，获得数据库生成或更新的字段；

    return db_order  #把创建后的数据库对象交给路由