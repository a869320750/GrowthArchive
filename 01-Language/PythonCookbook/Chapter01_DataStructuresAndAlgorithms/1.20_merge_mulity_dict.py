"""
现在有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某些操作，比如查找值或者检查某些键是否存在。
"""


a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2, 'z': 4}

#现在假设你必须在两个字典中执行查找操作 (比如先从 a 中找，如果找不到再在 b中找)。一个非常简单扼解决方案就是使用 collections 模块中的 ChainMap 

from collections import ChainMap
c = ChainMap(a, b)
print(c['x'], c['w'], c['y'], c['z'])