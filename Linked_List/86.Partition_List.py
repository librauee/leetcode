# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 21:28:12 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head == None or head.next == None:
            return head

        cur = head
        pre_min = cur_min = ListNode(None)
        pre_max = cur_max = ListNode(None)

        while cur != None:
            if cur.val < x:
                cur_min.next = cur
                cur_min = cur_min.next
            else:
                cur_max.next = cur
                cur_max = cur_max.next

            cur = cur.next

        cur_min.next = pre_max.next
        cur_max.next = None
        return pre_min.next