import json
import logging

from models import Order
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

def load_orders(file_path: str) -> list[Order]:
    # 这里的file_path应该是字符串，而且函数已经通过参数接收了它，
    # 不需要重新赋值：
    with open(file_path, "r", encoding="utf-8") as file:
        raw_orders = json.load(file)

    orders: list[Order] = []
    for item in raw_orders:
        order = Order(
            order_id=item["order_id"],
            user_id=item["user_id"],
            product=item["product"],
            amount=item["amount"],
            status=item["status"],
        )
        orders.append(order)

        # orders = json.load(file)
        # # 把JSON转换成Python对象。

    logger.info("成功加载 %d 条订单", len(orders))
    # print("raw_orders的类型：", type(raw_orders))
    # print("第一条原始数据的类型：", type(raw_orders[0]))
    # print("orders的类型：", type(orders))
    # print("第一条转换后数据的类型：", type(orders[0]))
    return orders

def find_order(orders:list[Order], order_id:str) -> Order | None:
    for order in orders:
        if order.order_id == order_id:
            # logger.info("开始查询订单：%s", order_id)
            return order
        
    return None 

def display_order(order: Order | None) -> None: #类型提示
    if order is None:
        logger.warning("没有找到对应订单")
        print("订单不存在") 
    else: 
        print("商品：",order.product)
        print("金额：",order.amount)
        print("状态：",order.status)



def main() -> None:
    try:
        orders = load_orders("orders.json")
    except FileNotFoundError:
        logger.error("订单数据文件不存在")
        print("错误：找不到orders.json文件")
        return
    except json.JSONDecodeError as error:
        logger.error(
            "JSON格式不正确：第%d行，第%d列",
            error.lineno,
            error.colno,
        )
        print(
            f"错误：JSON格式不正确，"
            f"第{error.lineno}行，第{error.colno}列"
        )
        return
    
    order_id = input("请输入订单号：").strip()
    logger.info("开始查询订单：%s", order_id)
    order = find_order(orders, order_id)
    display_order(order)


if __name__ == "__main__":
    main()
#     list：保存多条订单。
# dict：保存一条订单的字段。
# for：逐条查找订单。
# function：把加载、查询和显示分开。
# exception：处理文件不存在、JSON损坏等异常


# JSON    	Python
# []	    list
# {}	    dict
# "1001"	str
# 299.0	    float
# null	    None