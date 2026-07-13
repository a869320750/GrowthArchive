"""
怎样在两个字典中寻寻找相同点 (比如相同的键、相同的值等等)？
"""

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

print(f"字典 a: {a}")
print(f"字典 b: {b}")
print(f"字典 a 和 b 的键的交集: {a.keys() & b.keys()}")
print(f"字典 a 和 b 的键的并集: {a.keys() | b.keys()}")
print(f"字典 a 和 b 的键的差集: {a.keys() - b.keys()}")
print(f"字典 a 和 b 的键的对称差集: {a.keys() ^ b.keys()}")
print(f"字典 a 和 b 的键值对的交集: {a.items() & b.items()}")



"""
同类三大推导式一起区分：
列表推导式：[x*2 for x in arr]
集合推导式：{x%3 for x in arr}
字典推导式：{k:v for k,v in dict.items()}
"""
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(f"字典 a 中去掉键 'z' 和 'w' 后的新字典: {c}")


a = {'a','b','c'}
b = {'b','c','d'}

print(f"set a: {a}")
print(f"set b: {b}")
print(f"set a 和 b 的键的交集: {a & b}")
print(f"set a 和 b 的键的并集: {a | b}")
print(f"set a 和 b 的键的差集: {a - b}")
print(f"set a 和 b 的键的对称差集: {a ^ b}")