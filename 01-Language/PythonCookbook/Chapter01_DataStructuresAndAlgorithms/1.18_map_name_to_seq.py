"""
你有一段通过下标访问列表或者元组中元素的代码，但是这样有时候会使得你的代码难以阅读，于是你想通过名称来访问元素。
"""

from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)

print(sub.addr)

print(sub.joined)

print(len(sub))

addr, joined = sub
print(addr)
print(joined)

def compute_cost(records):
    total = 0.0
    for rec in records:
        s = slice(20, 23)
        p = slice(31, 37)
        total += int(rec[s]) * float(rec[p])
    return total

from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost_named(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total
