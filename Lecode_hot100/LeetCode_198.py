# https://leetcode.cn/problems/house-robber/?envType=problem-list-v2&envId=2cktkvj
"""
核心思路
我们不能偷相邻的房子。对于第 i 间房子，有两种选择：
偷：那么第 i-1 间就不能偷，最大金额为 第i间金额 + 前i-2间的最大金额。
不偷：最大金额为 前i-1间的最大金额。
状态转移方程：dp[i] = max(dp[i-1], dp[i-2] + nums[i])

"""

from typing import List
def rob(self, nums: List[int]) -> int:
    if  len(nums)==0: return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
    pre1 = nums[0]
    pre2 = max(nums[:2])
    for i in range(2,len(nums)):
        current  = max(pre2,pre1+nums[i])
        pre1 = pre2
        pre2 = current
    return pre2



