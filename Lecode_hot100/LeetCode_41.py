# https://leetcode.cn/problems/first-missing-positive/description/?envType=study-plan-v2&envId=top-100-liked
"""
41. 缺失的第一个正数
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
思路：
没有出现的正整数只会出现在1 ~ n+1中间的某一个数
需要把每个在1 ~ n+1的数i放到数组的i-1的位置上，再看一下第一个不满足num[i] = i+1,i+1就是要找的目标值
极端情况就是1~n都存在，此时就是n+1
"""

from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            # 如果数i是在1~n之间
            # 并且其对应的位置上面的数也不对，就和其对应位置上面的数进行交换
            # 这里不能只判断位置是否正确（nums[i]-1 ！= i），如果有重复的会出现死循环
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                # 交换
                traget = nums[i] - 1 
                nums[i] ,nums[traget] = nums[traget] ,nums[i] 
        #上面的所有的数都放到对应位置上面了，第一个不满足条件的就是我们要找的目标
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        # 极端情况是返回n+1
        return n+1

nums = [3,4,-1,1]
s = Solution()
print(s.firstMissingPositive(nums))