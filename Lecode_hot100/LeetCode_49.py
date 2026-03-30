# https://leetcode.cn/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-100-liked
"""
解题思路：使用hash表
默认排序的作为指针，其余的作为数值
"""
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for s in strs:
            # 对字符串排序，生成唯一键
            key = ''.join(sorted(s))
            anagram_dict[key].append(s)
        # 将字典的值转换为列表返回
        return list(anagram_dict.values())
if __name__ == "__main__":
     strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
     print(Solution().groupAnagrams(strs))
