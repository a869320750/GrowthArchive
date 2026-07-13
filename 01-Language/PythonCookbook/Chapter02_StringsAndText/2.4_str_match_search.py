"""
你想匹配或者搜索特定模式的文本
"""

text = 'yeah, but no, but yeah, but no, but yeah'

print(text.startswith('yeah'))  # True
print(text.endswith('no'))  # False

print(text.find('no'))  # 12

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'[A-Za-z]+ \d+, \d+', text2):
    print('yes')
else:
    print('no')


datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match(text1)
print(m)
print(type(m))
print(m.groups()) # type: ignore