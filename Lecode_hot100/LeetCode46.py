"""
https://leetcode.cn/problems/permutations/description/?envType=study-plan-v2&envId=top-100-liked
46. 全排列
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
思路
回溯法
回溯法解决，核心思路是通过 “尝试 - 回溯” 的方式枚举所有可能的排列
1. 选择：在当前步骤选择一个可用元素加入排列。
2. 递归：基于当前选择，继续构建下一个位置的元素。
3. 回溯：撤销上一步的选择，尝试其他可能的元素。
"""
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def backtrack(start: int):
            # 递归终止条件：已确定所有位置的元素
            if start == n:
                res.append(nums.copy())  # 注意要copy，否则后续修改会影响结果
                return
            # 遍历从start开始的所有元素，选择一个作为当前位置的元素
            for i in range(start, n):
                # 交换：将nums[i]放到当前确定的位置start
                nums[start], nums[i] = nums[i], nums[start]
                # 递归：确定下一个位置（start+1）
                backtrack(start + 1)
                # 回溯：交换回来，恢复数组原状
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0)
        return res