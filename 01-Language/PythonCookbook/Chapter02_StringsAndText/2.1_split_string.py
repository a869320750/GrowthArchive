"""
你需要将一个字符串分割为多个字段，但是分隔符 (还有周围的空格) 并不是固定的。
"""
line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
print(re.split(r'[;,\s]\s*', line))
print(line.split(r'[;,\s]\s*'))
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)

result = ''.join(v + d for v, d in zip(values, delimiters))
print(result)

print((values, delimiters))
print(zip(values, delimiters))