"""
怎样在数据字典中执行一些计算操作 (比如求最小值、最大值、排序等等)？
"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(f"最便宜的股票: {min_price[1]}，价格: {min_price[0]}")

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(f"按价格排序的股票列表: {prices_sorted}")

"""
# 下面这段代码会报错，因为 zip 对象只能迭代一次

prices_and_names = zip(prices.values(), prices.keys())
print(f"zip: {list(prices_and_names)}")
# 取出价格最低的三只股票
print(min(prices_and_names))
print(max(prices_and_names))
"""
