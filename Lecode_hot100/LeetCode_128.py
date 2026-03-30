# https://leetcode.cn/problems/longest-consecutive-sequence/?envType=study-plan-v2&envId=top-100-liked
"""
思路：
遍历每一个数，如果


"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. 存入集合，去重并支持 O(1) 查找
        num_set = set(nums)
        max_len = 0

        # 2. 遍历集合中的每个数
        for num in num_set:
            # 3. 关键：只有当 num-1 不在集合中时，num 才是序列的起点
            if num - 1 not in num_set:
                current_num = num
                current_len = 1

                # 4. 从起点开始，向后扩展查找
                while current_num + 1 in num_set:
                    current_num += 1
                    current_len += 1

                # 5. 更新最长长度
                max_len = max(max_len, current_len)

        return max_len

if __name__ == "__main__":

    nums = [100,4,200,1,3,2]
    print(Solution().longestConsecutive(nums))
