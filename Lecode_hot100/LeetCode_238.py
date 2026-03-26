# https://leetcode.cn/problems/product-of-array-except-self/description/?envType=problem-list-v2&envId=2cktkvj
"""
左遍历（前缀积）：创建一个结果数组 answer，先从左向右遍历，让 answer[i] 存储 nums[i] 左侧所有元素的乘积。
右遍历（后缀积）：再从右向左遍历，使用一个变量 right 记录 nums[i] 右侧所有元素的乘积，并将其与 answer[i]（左侧积）相乘，得到最终结果。
假设有【A,B,C,D】
向左走answer分别变成[1,A,AB,ABC]
向右走answer分别变成[BCD,ACD,ABD,ABC]
从而得到结果
"""
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    n  = len(nums)
    answer = [1]* n
    # answer[i] 表示 nums[i] 左边所有元素的乘积
    for i in range(1,n):
        answer[i] = answer[i-1] * nums[i-1]
    right = 1
    # right 变量表示 nums[i] 右边所有元素的乘积
    for i in range(n-1 ,-1,-1):
        answer[i] = answer[i]*right
        right *= nums[i]
    return answer


nums = [2, 3, 4]
print(productExceptSelf(nums))
