# 创建数据表
from database import Base, engine
from db_models import OrderRecord


def create_tables() -> None:
    Base.metadata.create_all(bind=engine)
    print("数据库表创建完成")


if __name__ == "__main__":
    create_tables()