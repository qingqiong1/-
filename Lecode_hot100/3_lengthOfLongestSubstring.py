# https://leetcode.cn/problems/longest-substring-without-repeating-characters/?envType=study-plan-v2&envId=top-100-liked
'''
无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

右指针 right 不断向右移动，遍历每个字符。
如果当前字符在窗口内出现过（即其最后一次出现的索引 ≥ left），则将 left 移动到该字符上次出现位置的下一个位置，保证窗口内无重复。
更新当前字符的最后出现索引为 right。
计算当前窗口长度，更新最大长度。

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # 键：字符，值：字符最后一次出现的索引
        left = 0       # 窗口左边界
        max_len = 0    # 最长子串长度
        
        # 右指针遍历字符串（enumerate 同时获取索引和字符）
        for right, c in enumerate(s):
            # 如果当前字符在窗口内出现过，移动左边界
            if c in char_map and char_map[c] >= left:
                left = char_map[c] + 1
            # 更新当前字符的最后出现索引
            char_map[c] = right
            # 更新最长子串长度
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
        
        return max_len
