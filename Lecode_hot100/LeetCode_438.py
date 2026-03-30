# https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/?envType=study-plan-v2&envId=top-100-liked
"""
统计目标频率：先统计字符串 p 中每个字符的出现频率（用长度为 26 的数组表示，对应小写字母 a-z）。
滑动窗口遍历：在字符串 s 中维护一个长度为 len(p) 的滑动窗口，统计窗口内的字符频率。
频率比较：每次滑动窗口时，比较窗口内的频率与 p 的频率。若相等，则记录当前窗口的起始索引。
窗口更新：滑动窗口时，只需将左侧移出的字符频率减 1，右侧移入的字符频率加 1，避免重复统计。
"""

from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)
        if len_s < len_p:
            return []
        
        # 初始化字符频率数组（对应 a-z）
        count_p = [0] * 26
        count_s = [0] * 26
        
        # 统计 p 的字符频率
        for c in p:
            count_p[ord(c) - ord('a')] += 1
        
        # 统计 s 中第一个窗口（前 len_p 个字符）的频率
        for i in range(len_p):
            count_s[ord(s[i]) - ord('a')] += 1
        
        res = []
        # 检查第一个窗口是否是异位词
        if count_s == count_p:
            res.append(0)
        
        # 滑动窗口，从索引 1 开始
        for i in range(1, len_s - len_p + 1):
            # 移出窗口左侧的字符（s[i-1]）
            count_s[ord(s[i-1]) - ord('a')] -= 1
            # 移入窗口右侧的新字符（s[i+len_p-1]）
            count_s[ord(s[i + len_p - 1]) - ord('a')] += 1
            
            # 比较频率，若相等则记录起始索引
            if count_s == count_p:
                res.append(i)
        
        return res
                


