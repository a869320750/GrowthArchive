"""
你正在处理 Unicode 字符串，需要确保所有字符串在底层有相同的表示。
"""
import re
num = re.compile('\d+')

print(num.match('123'))  # 匹配

print(num.match('\u0661\u0662\u0663'))  # 匹配

arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straβe'

print(pat.match(s))  # 匹配失败

print(pat.match(s.upper())) # 匹配失败

print(s.upper())  # STRAßE