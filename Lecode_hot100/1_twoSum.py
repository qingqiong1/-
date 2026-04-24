# https://leetcode.cn/problems/two-sum/description/?envType=study-plan-v2&envId=top-100-liked

"""
两数之和
通过哈希值存储已经搜索过的数【数值，索引】，看当前数的补数在哈希表里面是否存在
"""
from typing import List
from collections import defaultdict
class Solution:
    def twoSum(self,nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[num] = i
        return []