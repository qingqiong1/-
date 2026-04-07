"""
17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。


通过递归逐层处理每个数字，从当前数字对应的字母中选择一个加入组合，直到处理完所有数字，将完整组合加入结果。
映射表：先建立数字到字母的对应关系（如'2'对应['a','b','c']）。
边界处理：如果输入为空字符串，直接返回空列表。
回溯函数：
index：当前处理到的数字的索引（从 0 开始）。
path：当前正在构建的字母组合。
终止条件：当index等于输入字符串长度时，说明已处理完所有数字，将path加入结果。
递归过程：遍历当前数字对应的每个字母，将字母加入path，递归处理下一个数字（index+1）。
"""
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 边界情况：输入为空字符串，直接返回空列表
        if not digits:
            return []
        
        # 建立数字到字母的映射（与电话按键一致）
        digit_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        res = []
        n = len(digits)
        
        def backtrack(index: int, path: str):
            # 递归终止条件：已处理完所有数字，将当前组合加入结果
            if index == n:
                res.append(path)
                return
            # 获取当前数字对应的字母列表
            current_digit = digits[index]
            for letter in digit_map[current_digit]:
                # 选择当前字母，递归处理下一个数字
                backtrack(index + 1, path + letter)
        
        # 从第0个数字开始，初始组合为空字符串
        backtrack(0, "")
        return res