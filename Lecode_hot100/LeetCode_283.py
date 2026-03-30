# https://leetcode.cn/problems/move-zeroes/description/?envType=study-plan-v2&envId=top-100-liked
"""
移动0
思路：快慢指针，把非零元素放到一起，最后补充0元素
"""
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        必须在不复制数组的情况下原地对数组进行操作.
        """
        # 计算数组长度为填充做准备
        len_nums = len(nums)
        # 定义慢指针指向第一个位置
        slow = 0
        for num in nums:
            # 如果num不是0，就把slow位置的数换为num，slow向前进
            if num != 0:
                nums[slow] = num
                slow += 1
        # 最后按照数组原长度填充0
        if slow < len_nums:
            nums[slow:len_nums] = [0]*(len_nums - slow)
        




        