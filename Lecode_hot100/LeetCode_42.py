# https://leetcode.cn/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-100-liked
"""
接雨水
核心思路：
算出每一列可以存多少雨水 = max(0,min(left_max_heitht ,right_max_height)  - height)
如果已经知道右边又比左边高的，那么i位置的就是由left_max_heitht决定。
也就是：max(0,left_max_heitht - height)
右边同理 
"""
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        total = 0
        left, right = 0, n-1
        left_max = right_max = 0
        
        while left < right:
            if height[left] < height[right]:
                # 更新左侧最大值
                left_max = max(left_max, height[left])
                # 计算当前left位置的储水量
                total += left_max - height[left]
                left += 1
            else:
                # 更新右侧最大值
                right_max = max(right_max, height[right])
                # 计算当前right位置的储水量
                total += right_max - height[right]
                right -= 1
        return total