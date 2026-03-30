# https://leetcode.cn/problems/3sum/description/?envType=study-plan-v2&envId=top-100-liked
"""
排序：先对数组排序，便于后续去重和双指针查找。
固定第一个数：遍历数组，将每个元素作为三元组的第一个数 nums[i]。
若 nums[i] > 0：由于数组已排序，后面两数之和必然大于 0，直接终止循环。
去重：若 nums[i] 与前一个数相同，跳过以避免重复三元组。
双指针查找：在 i 之后的子数组中，用左指针 left（头）和右指针 right（尾）查找和为 -nums[i] 的两个数。
若和为目标值：记录结果，并同时移动左右指针，跳过所有重复值。
若和小于目标值：左指针右移（增大和）。
若和大于目标值：右指针左移（减小和）。
"""
from typing import List
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        if len(nums) < 3:
            return []
        nums.sort()
        result = []
        for i , num in enumerate(nums):
            if num > 0:
                break
            if i>0 and num == nums[i-1]:
                continue
            left,right = i+1 ,len(nums)-1
            while left < right :
                s = nums[left]  + nums[right]
                if s == -num :
                    result.append([num,nums[left],nums[right]])
                    while left<right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < -num: left += 1
                elif s > -num: right -= 1
        return result


                
nums = [-1,0,1,2,-1,-4]
s = Solution()
print(s.threeSum(nums))                    

