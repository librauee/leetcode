# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 13:39:01 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        res = pre = ListNode(0)
        pre.next = head
        while head and head.next:
            l1,l2 = head,head.next
            pre.next,l1.next,l2.next = l2,l2.next,l1
            pre,head = l1,l1.next
        return res.next