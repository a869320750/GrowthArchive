"""
你的程序已经出现一大堆已无法直视的硬编码切片下标，然后你想清理下代码。
"""

record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
print(f"cost={cost}")

SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
print(f"cost={cost}")