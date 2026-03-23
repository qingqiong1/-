# https://leetcode.cn/problems/remove-duplicates-from-sorted-array/description/
# 删除有序数组的重复项

"""
通过快慢指针实现
也可以通过set实现
"""
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        slow = 0
        # 如果相等，fast前进不计数，如果不相等，slow+1，计数的同时修改当前fast的最新值
        for fast in range(1,len(nums)):
            if nums[slow] != nums[fast]:
                slow +=1
                nums[slow] = nums[fast]
        return slow+1
    


        