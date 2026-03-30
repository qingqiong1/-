# https://leetcode.cn/problems/subarray-sum-equals-k/description/?envType=study-plan-v2&envId=top-100-liked
"""
前缀和定义：设 pre[i] 为数组前 i 个元素的和（即 nums[0] + nums[1] + ... + nums[i-1]）。
        那么任意的子数组 nums[j...i] 的和可以表示为 pre[i+1] - pre[j]。j < i+1
目标转化：我们需要子数组和为 k，即 pre[i+1] - pre[j] = k → 变形为 pre[j] = pre[i+1] - k。
        也就是如果满足pre[i+1] - pre[j] = k，就看一下之前的pre[j]出现过多少次
哈希表统计：遍历数组时，用哈希表（字典）记录每个前缀和出现的次数。对于当前的前缀和 pre[i+1]， pre[i+1] - k 出现的次数，即可得到以当前位置结尾的、和为 k 的子数组个数。
初始化细节：哈希表初始需存入 {0: 1}，用于处理 “当前前缀和本身就等于 k” 的情况（即子数组从数组开头起始）。

"""
from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # key: 前缀和, value: 该前缀和出现的次数
        # 初始化 {0: 1}，处理子数组从索引 0 开始的情况
        prefix_count = defaultdict(int) #存储pre[j]数值的个数
        prefix_count[0] = 1 
        
        pre_sum = 0  # 当前的前缀和
        count = 0    # 统计符合条件的子数组个数
        
        for num in nums:
            pre_sum += num  # 更新当前前缀和p[i+1]
            
            # 核心逻辑：如果哈希表里面有数值满足pre[i+1] - pre[j] = k
            # 则说明存在子数组num[j:i]和为 k，个数为之前出现的次数
            if (pre_sum - k) in prefix_count:
                count += prefix_count[pre_sum - k]
            
            # 记录当前前缀和出现的次数
            prefix_count[pre_sum] += 1
        
        return count