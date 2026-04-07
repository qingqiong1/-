"""
https://leetcode.cn/problems/combination-sum/description/?envType=study-plan-v2&envId=top-100-liked
39. 组合总和
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 
对于给定的输入，保证和为 target 的不同组合数少于 150 个。

回溯核心：遍历数组，逐个选择数字，累加和，直到和等于目标值则记录组合；若超过目标值则回溯（撤销当前选择）。
去重优化：因为数字可重复使用，且组合不考虑顺序（如 [2,3] 和 [3,2] 是同一个组合），所以每次递归从当前索引开始遍历，避免重复组合。
剪枝优化：先对数组排序，若当前数字累加后超过目标值，直接跳出循环（后续数字更大，无需遍历）。

"""
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 1. 排序：为了剪枝优化，提前排序
        candidates.sort()
        result = []  # 存储最终所有符合条件的组合
        
        # 回溯函数：path=当前选择的组合，start=起始索引（避免重复），sum=当前和
        def backtrack(path, start, current_sum):
            # 递归终止条件：当前和等于目标值，记录组合
            if current_sum == target:
                result.append(path.copy())
                return
            # 遍历数组，从start开始（可重复选当前数字，防止组合重复）
            for i in range(start, len(candidates)):
                num = candidates[i]
                # 剪枝：当前和+数字超过目标，直接跳出（数组已排序，后续数字更大）
                if current_sum + num > target:
                    break
                # 选择当前数字
                path.append(num)
                # 递归：i不变（可重复选当前数字），更新当前和
                backtrack(path, i, current_sum + num)
                # 回溯：撤销选择，尝试下一个数字
                path.pop()
        
        # 初始调用：空组合，起始索引0，当前和0
        backtrack([], 0, 0)
        return result