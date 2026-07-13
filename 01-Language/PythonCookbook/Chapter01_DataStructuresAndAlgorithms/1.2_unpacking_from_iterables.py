"""
Recipe 1.2: 从任意长度的可迭代对象中解压元素
使用 * 表达式
如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。那么怎样才能从这个可迭代对象中解压出 N 个元素出来？
"""

def drop_first_last(grades):
    """去掉第一个和最后一个成绩，取中间的平均值"""
    first, *middle, last = grades
    return sum(middle) / len(middle)

grades = [85, 90, 78, 92, 88, 76]
avg = drop_first_last(grades)
print(f"去掉首尾后的平均分: {avg}")

# 其他用法
record = ("Dave", "dave@example.com", "773-555-1212", "847-555-1212")
name, email, *phone_numbers = record
print(f"name={name}, email={email}, phones={phone_numbers}")

# 星号解压在字符串分割中也很实用
line = "nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false"
uname, *fields, homedir, sh = line.split(":")
print(f"uname={uname}, homedir={homedir}, shell={sh}")
