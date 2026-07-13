"""
怎样实现一个键对应多个值的字典 (也叫 multidict )？
"""
d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}
print(d['a'], d['b'],type(d),type(d['a']),type(d['b']))
e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}
print(e['a'], e['b'],type(e),type(e['a']),type(e['b']))
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d['a'], d['b'],type(d),type(d['a']),type(d['b']))

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d['a'], d['b'],type(d),type(d['a']),type(d['b']))
