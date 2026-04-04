# https://leetcode.cn/problems/rotate-array/description/?envType=study-plan-v2&envId=top-100-liked

"""
核心思想
对数组先进行反转，然后对前k个进行反转，对后k个进行反转，就可以得到目标值
"""
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n

        def reverse(start ,end):
            while start <end:
                nums[start], nums[end] = nums[end], nums[start]
                start +=1
                end -=1
        reverse(0,len(nums)-1)
        reverse(0,k-1)
        reverse(k,len(nums)-1)
    
    def rotate2(self, nums, k):
        n = len(nums)
        k = k % n
        # 把最后k个 + 前n-k个拼接
        nums[:] = nums[-k:] + nums[:-k]


        