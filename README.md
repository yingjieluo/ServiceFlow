# ServiceFlow

面向电商售后的可信AI客服Agent平台。
ServiceFlow主要是借助本地的rag，langchain的内容等，解决客户的订单等问题，尤其是当人工客服不在的时候能实时会话并给出对应解决方案

## 当前进度

当前已完成本地订单读取、订单查询、数据模型和单元测试。

## 运行

`python order_query.py`主程序运行后输入订单号可以查询

## 测试

`python -m pytest -v test_order_query.py`

当前版本仅支持通过订单号查询本地模拟订单。