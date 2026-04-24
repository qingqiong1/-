"""
https://leetcode.cn/problems/palindrome-linked-list/description/?envType=study-plan-v2&envId=top-100-liked
回文链表
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

通过快慢指针找到中间点，再反转后面的链表，再比较
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        # 找中间节点
        while fast and fast.next:
            slow = slow.next # pyright: ignore[reportOptionalMemberAccess]
            fast = fast.next.next
        # 从slow开始反转
        pre = None
        while slow:
            nex = slow.next
            slow.next = pre
            pre = slow
            slow = nex
        
        # 对比
        while pre:
            if pre.val != head.val: # pyright: ignore[reportOptionalMemberAccess]
                return False
            pre = pre.next
            head = head.next # pyright: ignore[reportOptionalMemberAccess]
        return True



