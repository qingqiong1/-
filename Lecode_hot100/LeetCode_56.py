# https://leetcode.cn/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-100-liked
"""
排序：将所有区间按起始位置 start 从小到大排序。排序后，重叠的区间必然是连续的，我们只需一次遍历即可完成合并。
贪心合并：维护一个结果列表，遍历排序后的区间：
若结果列表为空，或当前区间的 start > 结果列表最后一个区间的 end，说明不重叠，直接加入结果。
否则，说明重叠，将结果列表最后一个区间的 end 更新为两者的最大值（合并）。
"""
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        # 进行排序
        intervals.sort(key=lambda x:x[0])
        # 结果存储列表
        result = [intervals[0]]

        for _,interval in enumerate(intervals[1:]):
            # 去除结果里面的最后一个区间的第二个值和当前区间的第一个值进行比较
            # 如果大于，就直接合并区间
            if result[-1][1]>=interval[0]:
                result[-1][1] = max(result[-1][1],interval[1])
            else:
                result.append(interval) #不重叠就直接放入结果
        return result