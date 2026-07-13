"""
Recipe 1.1: 将序列分解为单独变量
问题：现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值
给 N 个变量？
"""
# 任何可迭代对象都可以通过赋值操作解压
p = (4, 5)
x, y = p
print(f"x={x}, y={y}")

data = ["ACME", 50, 91.1, (2024, 7, 1)]
name, shares, price, date = data
print(f"name={name}, shares={shares}, price={price}, date={date}")

# 解压时变量数量必须匹配
# 如果只需要部分元素，可用 _ 占位
_, shares, price, _ = data
print(f"shares={shares}, price={price}")

print(type(list((range(5,7)))))