#https://leetcode.cn/problems/intersection-of-two-linked-lists/solutions/12624/intersection-of-two-linked-lists-shuang-zhi-zhen-l/?envType=study-plan-v2&envId=top-100-liked
"""
相交链表
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

思路：
两个节点分别遍历A和B，相等的时候就是他们相交的地点
a：A到相交点的路程
b：B到相交点的路程
c：相交点到null的路程
A：a+c+b
B：b+c+a
当都走完的时候就是A和B的相交点
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        la = headA
        lb = headB
        while la!=lb:
            la = la.next if la else headB
            lb = lb.next if lb else headA
        return la