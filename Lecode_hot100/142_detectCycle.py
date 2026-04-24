"""
https://leetcode.cn/problems/linked-list-cycle-ii/description/?envType=study-plan-v2&envId=top-100-liked
环形链表二
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
不允许修改 链表。

思路：先找到相遇点，再有一个指针指向头和slow同步走，相遇的地方就是入环点
具体解释可以看力扣官方题解的公式推导
"""

import re
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        pre = head

        while fast and fast.next:
            slow = slow.next # type: ignore
            fast = fast.next.next
            if fast == slow:
                while pre != fast:
                    pre = pre.next # type: ignore
                    fast = fast.next
                return fast
        return None
        
