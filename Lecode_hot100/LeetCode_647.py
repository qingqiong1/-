# https://leetcode.cn/problems/palindromic-substrings/description/?envType=problem-list-v2&envId=2cktkvj
"""
核心思路
回文子串分为两种情况：
奇数长度：中心是一个字符（例如 "aba" 的中心是 b）。
偶数长度：中心是两个相邻字符之间的间隙（例如 "abba" 的中心是两个 b 之间）。
我们遍历字符串中的每一个可能的 “中心”，然后向左右两边扩展，只要左右字符相等，就计数加一。

"""


def countSubstrings(s: str) -> int:
    n = len(s)
    count = 0
    
    # 辅助函数：给定中心 left 和 right，向外扩展统计回文数
    def expand_around_center(left: int, right: int) -> int:
        cnt = 0
        # 只要左右边界不越界，且字符相等，就是回文
        while left >= 0 and right < n and s[left] == s[right]:
            cnt += 1
            left -= 1   # 左指针左移
            right += 1  # 右指针右移
        return cnt
    
    # 遍历每一个可能的中心
    for i in range(n):
        # 情况1：奇数长度回文，中心为 s[i]
        count += expand_around_center(i, i)
        # 情况2：偶数长度回文，中心为 s[i] 和 s[i+1] 之间
        count += expand_around_center(i, i + 1)
    
    return count

