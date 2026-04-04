# https://leetcode.cn/problems/sliding-window-maximum/description/?envType=study-plan-v2&envId=top-100-liked

"""
思路：
1. 窗口的长度是固定的，每次移动都会新增一个值，删除一个值
2. 我需要存储一个历史最大值，并且这个最大值是在窗口内的
3. 为了方便找这个最大值，我需要把最大值统一放到第一个位置，这样的话查找是O(1)

这些比新元素小的旧元素，永远不可能成为后续任何一个窗口的最大值

"""
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()  # 双端队列，存储索引，保持对应值单调递减

        for i in range(len(nums)):
            # 1. 移除队首超出窗口范围的元素 (索引 <= i - k)
            if dq and dq[0] == i - k:
                dq.popleft()

            # 2. 从队尾移除所有小于等于当前元素的索引
            # 因为它们在当前元素存在时，不可能成为后续窗口的最大值
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()

            # 3. 将当前索引加入队尾
            dq.append(i)

            # 4. 当窗口形成时 (i >= k - 1)，记录队首对应的最大值
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
