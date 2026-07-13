"""
你正在试着使用正则表达式去匹配一大块的文本，而你需要跨越多行去匹配。
"""
import re
comment = re.compile(r'/\*(.*?)\*/')

text1 = '/* this is a comment */'
text2 = '''/* this is a
multiline comment */
'''
print(comment.findall(text1))  # [' this is a comment ']
print(comment.findall(text2))  #

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))  # [' this is a\nmultiline comment ']

comment = re.compile(r'/\*((?:.|\n)*?)\*/', re.DOTALL)
print(comment.findall(text2))  # [' this is a\nmultiline comment ']