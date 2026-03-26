# https://leetcode.cn/problems/maximum-subarray/description/?envType=problem-list-v2&envId=2cktkvj
"""
1. 最大子数组一定是以某一个数结尾
2. 对于每一个数，我们可以算出以它结尾的最大子数组
3. 在这个过程中我们取最大就是答案
总结：前面是累赘就从新开始，前面还有用就继续保留
"""

from typing import List
# 最大子数组和 O(n)
class Solution1:
    def maxSubArray1(self, nums: List[int]) -> int:
        # 当前的子数组
        cur = nums[0]
        # 全局的最大数组
        max_sum = nums[0]
        # 循环，如果加入一个数当前子数组变小，子数组就重新开始，同时记录一个历史最大数组
        for num in nums:
            cur = max(num,cur+num)
            max_sum = max(max_sum,cur)
        return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution1().maxSubArray1(nums))
# 分治法
"""
递归的思想
最大子数组不是在两边就是跨中间
先算两边的最大子数组
在算跨中间的最大子数组
最后比较三个最大子数组
通过递归可以得到子数组的最大子数组
如果左右一样的话最大子数组就是它本身

"""
class Solution2:
    def maxSubArray2(self, nums: List[int]) -> int:
        # 数组分成两半
        def devide(left,right):
            if left == right :
                return nums[left]
            mid = (left +right) // 2
            left_max = devide(left,mid)
            right_max = devide(mid+1,right)

            cross_left = - int("inf")
            s = 0
            for i in range(mid,left-1,-1):
                s+=nums[i]
                cross_left = max(cross_left,s)
            cross_right = -int('inf')
            s = 0
            for j in range(mid+1,right+1):
                s+= nums[j]
                cross_right = max(cross_right,s)
            cross_max = cross_left +cross_right
            
            return max(cross_max,left_max,right_max)

        return devide(0,len(nums)-1)
          

if __name__ == "main":
    pass
