from collections.abc import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


DATABASE_URL = "sqlite:///./serviceflow.db"
# 表示使用SQLite，并将数据保存在当前项目目录的serviceflow.db中。

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(bind=engine)
# 创建数据库引擎。它负责管理程序与数据库之间的连接。

# 创建Session工厂。后面每次查询、添加或修改数据库，都通过Session完成。
class Base(DeclarativeBase):
    pass

def get_db() -> Generator[Session, None, None]: 
    #get_db是一次数据库操作使用的Session
    with SessionLocal() as session:
        yield session
# 收到HTTP请求
# 创建Session
# yield把Session暂时交给接口
# 接口完成数据库查询
# 退出with，自动关闭Session

# Session可以理解成“一次数据库工作会话”。
# 通过它可以： Session完成一次或一组查询、增加、修改操作
# session.get(...)      # 查询
# session.add(...)      # 准备新增
# session.delete(...)   # 准备删除
# session.commit()      # 提交修改
# session.rollback()    # 撤销本次未完成的数据库修改