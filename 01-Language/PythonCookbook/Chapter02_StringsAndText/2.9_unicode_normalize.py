"""
你正在处理 Unicode 字符串，需要确保所有字符串在底层有相同的表示。
"""
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print(s1, s2)
print(s1 == s2)  # False
print(len(s1), len(s2))  # 13 14

import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)  # True

print(len(t1), len(t2))  # 13 13

print(ascii(t1), ascii(t2))  # 'Spicy Jalape\xf1o' 'Spicy Jalape\xf1o'

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)

print(t3 == t4)  # True
print(len(t3), len(t4))  # 14 14