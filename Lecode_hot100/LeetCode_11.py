# https://leetcode.cn/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-100-liked
"""
核心思路
初始化：左指针 left 指向数组起点（索引 0），右指针 right 指向数组终点（索引 n-1）。
计算当前面积：用公式计算当前容器的面积。
移动指针：移动高度较小的那个指针（因为移动较高指针时，宽度减小且高度不会增加，面积只会更小；移动较矮指针，虽然宽度减小，但高度可能变大，从而可能得到更大面积）。
更新最大面积：每次计算后更新最大面积，直到 left >= right 时停止。
"""
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while(left < right):
            max_area = max( min(height[left], height[right]) * (right-left), max_area)
            if height[left] <  height[right]:
                left += 1
            else:
                right -=1
        return max_area
    
if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    s = Solution()
    print(s.maxArea(height))
