"""
你需要在数据序列上执行聚集函数 (比如 sum() , min() , max() )，但是首先你需要先转换或者过滤数据
"""

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(f"平方和: {s}")

import os
files = os.listdir('.')
if any(name.endswith('.py') for name in files):
    print("当前目录下存在 Python 源文件")
else:
    print("当前目录下不存在 Python 源文件")

s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(f"最少的股票份额: {min_shares}")