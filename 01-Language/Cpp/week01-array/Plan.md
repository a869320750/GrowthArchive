# 序号	题目	关键词	难度

- [x]  1	两数之和	哈希表	简单
```
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]

提示：
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
只会存在一个有效答案
``` 
- [x]  15	三数之和	排序 + 双指针 + 哈希	中等
```txt
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：
输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。

提示：
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
```
- [x]  18	四数之和	排序 + 双指针 + 哈希	中等
```txt
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

示例 1：
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
示例 2：
输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]
 
提示：
1 <= nums.length <= 200
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
```
- [x]  217	存在重复元素	哈希表	简单
```
给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。

示例 1：
输入：nums = [1,2,3,1]
输出：true
解释：
元素 1 在下标 0 和 3 出现。
示例 2：
输入：nums = [1,2,3,4]
输出：false
解释：
所有元素都不同。
示例 3：
输入：nums = [1,1,1,3,3,4,3,2,4,2]
输出：true

提示：
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
```
- [x]  219	存在重复元素 II（允许距离 <= k）	哈希表	简单
```
给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。

示例 1：
输入：nums = [1,2,3,1], k = 3
输出：true
示例 2：
输入：nums = [1,0,1,1], k = 1
输出：true
示例 3：
输入：nums = [1,2,3,1,2,3], k = 2
输出：false

提示：
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
0 <= k <= 10^5
```
- [x]  136	数组中第一个出现一次的数字	哈希表	简单
```
给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

示例 1 ：
输入：nums = [2,2,1]
输出：1
示例 2 ：
输入：nums = [4,1,2,1,2]
输出：4
示例 3 ：
输入：nums = [1]
输出：1

提示：
1 <= nums.length <= 3 * 10^4
-3 * 10^4 <= nums[i] <= 3 * 10^4
除了某个元素只出现一次以外，其余每个元素均出现两次。
```
- [x]  560	和为K的子数组	前缀和 + 哈希表	中等
    第一次听说前缀和
```
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
子数组是数组中元素的连续非空序列。

示例 1：
输入：nums = [1,1,1], k = 2
输出：2
示例 2：
输入：nums = [1,2,3], k = 3
输出：2

提示：
1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7
```
- [x]  8	连续数组（0和1数量相等的最长子数组）	哈希表	中等

想到了用前缀和，但是缺少优化，知道了一般是用前缀和做key，用下表做value
- [x]  9	最长连续序列	哈希表	中等

使用set存数据可以去重，然后依次判断是不是开头的，是开头的就往后走一遍算，

不是开头的就跳过
- [x]  10	两个数组的交集	哈希表	简单

确实比较简单，这个老哥的答案有点东西：
```cpp
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int>result;
        unordered_map<int ,int>hash;
        for(const auto &c:nums1)
        {
            hash[c]=1;
        }
        for(const auto &c:nums2)
        {
            --hash[c];
            if(hash[c]==0)
            result.push_back(c);
        }
        return result;
    }
```
- [x]  11	两个数组的交集 II	哈希表	简单

这个题目描述纯属瞎写啊，这道题本身比较简单，就不单独搞文件了，直接在平台上写了
```cpp
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> result;
        unordered_map<int,int> mp1;
        unordered_map<int,int> mp2;
        for(auto &&i:nums1) {
            if (mp1.count(i)) {
                ++mp1[i];
            } else {
                mp1[i] = 1;
            }
        }
        for(auto &&i:nums2) {
            if (mp2.count(i)) {
                ++mp2[i];
            } else {
                mp2[i] = 1;
            }
        }
        for(auto &&i:mp1){
            if (mp2.count(i.first)) {
                for(int j = 0; j < min(i.second,mp2[i.first]); j++) {
                    result.push_back(i.first);
                }
            }
        }
        return result;
    }
```
- [x]  12	数组中的第K个最大元素	堆 / 快排	中等

竟然是考过的一道题，两种方法
快速排序的特殊版本（快速选择）。分离函数通过双指针分离，然后外界一个循环类似折半查找。
第二种方法是堆排序，在C++里面就是priority_queue
```cpp
vector<int> heapSort(vector<int>& nums) {
    priority_queue<int> maxHeap; // 默认最大堆
    for (int num : nums) {
        maxHeap.push(num); // 所有元素入堆
    }
    
    vector<int> sorted;
    while (!maxHeap.empty()) {
        sorted.push_back(maxHeap.top()); // 取堆顶（最大值）
        maxHeap.pop(); // 删除堆顶
    }
    reverse(sorted.begin(), sorted.end()); // 最大堆需反转
    return sorted;
}
```
- [x]  13	缺失的第一个正数	哈希 + 原地置换	困难
- [x]  14	除自身以外数组的乘积	前后缀积	中等

有点意思,一个数组存左边的乘积，一个数组存右边的乘积：
```cpp
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> Left(nums.size());
        vector<int> Right(nums.size());
        int temp = 1;
        for(int i = 0; i < nums.size(); i++) {
            Left[i] = temp;
            temp = temp * nums[i];
        }
        temp = 1;
        for(int i = nums.size() - 1; i >= 0; --i) {
            Right[i] = temp;
            temp = temp * nums[i];
        }

        for(int i = 0; i < nums.size(); i++) {
            Left[i] = Left[i] * Right[i];
        }

        return Left;
    }
```
- [x]  15	移动零	双指针	简单

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
```cpp
void moveZeroes(vector<int>& nums) {
        int left = 0;
        int right = 0;
        while(right < nums.size()) {
            if(nums[right] != 0) {
                swap(nums[right], nums[left]);
                ++left;
                ++right;
            } else if (nums[right] == 0) {
                ++right;
            }
        }
    }
```
