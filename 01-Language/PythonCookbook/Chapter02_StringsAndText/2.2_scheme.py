"""
你需要通过指定的文本模式去检查字符串的开头或者结尾，比如文件名后缀，URL
Scheme 等等。
"""

filenames = 'spam.txt'
print(filenames.endswith('.txt'))
print(filenames.startswith('file:'))

url = 'http://www.python.org'
print(url.startswith('http:'))

import os
filenames = os.listdir('.')
print(filenames)

print([name for name in filenames if name.endswith(('.c', '.h', '.py', '.md'))])

from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        with urlopen(name) as f:
            return f.read()
    else:
        with open(name) as f:
            return f.read()
        
choices = ['http:', 'ftp:']
url = 'http://www.python.org'
print(url.startswith(tuple(choices)))

print(any(name.endswith('.py') for name in filenames))