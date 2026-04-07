"""
https://leetcode.cn/problems/subsets/description/?envType=study-plan-v2&envId=top-100-liked
78. 子集
思路：
核心思路是对每个元素进行 “选” 或 “不选” 的决策，递归枚举所有可能的组合。
递归树结构：每个节点代表一个子集，根节点是空集。
选择与回溯：
对于每个元素，先 “选” 它（加入path），递归处理后续元素；
然后 “回溯”（从path中移除），尝试 “不选” 它的情况。
start变量的作用：确保每次只从start之后的元素中选择，避免生成重复子集（如[2,1]）。
"""
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []  # 当前正在构建的子集
        n = len(nums)
        
        def backtrack(start: int):
            # 每进入一个节点，就将当前path加入结果（因为每个节点都是一个子集）
            res.append(path.copy())
            # 从start开始遍历，避免重复选择之前的元素
            for i in range(start, n):
                # 选择：将nums[i]加入当前子集
                path.append(nums[i])
                # 递归：处理下一个元素（start=i+1，保证不重复）
                backtrack(i + 1)
                # 回溯：撤销选择
                path.pop()
        
        backtrack(0)
        return res