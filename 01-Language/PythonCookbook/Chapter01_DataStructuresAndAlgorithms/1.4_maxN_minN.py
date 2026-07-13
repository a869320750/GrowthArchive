"""
怎样从一个集合中获得最大或者最小的 N 个元素列表？
"""

import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# 找出最大的 3 个元素
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(f"最便宜的三只股票: {cheap}") 
print(f"最贵的三只股票: {expensive}")

heapq.heapify(nums)
print(heapq.heappop(nums))
print(heapq.heappop(nums))
print(heapq.heappop(nums))
heapq.heappush(nums, 5)
heapq.heappush(nums, 7)
print(heapq.heappop(nums))
print(heapq.heappop(nums))