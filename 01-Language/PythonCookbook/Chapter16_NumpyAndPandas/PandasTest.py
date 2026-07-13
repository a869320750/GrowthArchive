import numpy as np

# 隔离符号
print("-"*50,"问题1","-"*50)

# 题目：创建一个 5x5 的随机整数矩阵（0-100），然后把所有 > 50 的元素替换成 0
arr = np.random.randint(0, 100, size=(5, 5))
print("原始矩阵：\n", arr)

# 解法1：用 where
arr2 = np.where(arr > 50, 0, arr)
print("替换后：\n", arr2)

# 解法2：布尔索引直接赋值（原地修改）
arr[arr > 50] = 0
print("原地替换：\n", arr)

# 隔离符号
print("-"*50,"问题2","-"*50)


# 题目：把一个数组归一化到 [0, 1] 区间： (x - min) / (max - min)
arr = np.random.randn(100) * 10 + 50  # 均值50，标准差10
print("原始数组 - min: {:.4f}, max: {:.4f}".format(arr.min(), arr.max()))
print("原始数组：\n", arr)
# 向量化归一化（一行搞定）
normalized = (arr - arr.min()) / (arr.max() - arr.min())
print(f"归一化后 - min: {normalized.min():.4f}, max: {normalized.max():.4f}")
print("归一化数组：\n", normalized)



# 隔离符号
print("-"*50,"问题3","-"*50)
# 题目：计算一个时间序列的 5 日移动平均线（不要直接用 pandas，用 numpy 实现）

def moving_average_numpy(data, window):
    """
    用 numpy 实现滑动窗口平均
    """
    # 方法1：用 cumsum 实现
    cumsum = np.cumsum(np.insert(data, 0, 0))
    return (cumsum[window:] - cumsum[:-window]) / window

    # 方法2：用卷积（更快的实现，但需要理解）
    # return np.convolve(data, np.ones(window)/window, mode='valid')

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(moving_average_numpy(data, 3))
print(moving_average_numpy(data, 5))
# 输出: [2. 3. 4. 5. 6. 7. 8. 9.]