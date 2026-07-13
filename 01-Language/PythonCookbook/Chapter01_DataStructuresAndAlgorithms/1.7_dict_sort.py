"""
你想创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序。
"""

from collections import OrderedDict
def ordered_dict_demo():
    d = OrderedDict()
    d['a'] = 1
    d['c'] = 3
    d['b'] = 2

    print(d)
    for key, value in d.items():
        print(key, value)

ordered_dict_demo()


"""
四、一句话总结本节要传达的知识
核心功能：强制保留键的插入顺序，遍历、序列化输出顺序可控；
历史必要性：3.6 前普通字典无序，是唯一可靠方案；
现代价值：就算新版 dict 有序，OrderedDict 依然不可替代 —— 支持顺序敏感相等判断、动态调整键位置，适合配置、缓存、严格有序 JSON 场景。
"""