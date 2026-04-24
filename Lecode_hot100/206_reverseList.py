"""
https://leetcode.cn/problems/reverse-linked-list/?envType=study-plan-v2&envId=top-100-liked
反转链表
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

1.存储下一个节点
2.当前节点指向前一个
3.处理下一个节点
"""


from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, pre = head, None
        while cur:
            tmp = cur.next # 暂存后继节点 cur.next
            cur.next = pre # 修改 next 引用指向
            pre = cur      # pre 暂存 cur
            cur = tmp      # cur 访问下一节点
        return pre

