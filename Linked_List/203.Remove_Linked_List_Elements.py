# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 22:09:22 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        head_node = ListNode(None)
        head_node.next = head
        q = head_node
        while q.next:
            if q.next.val == val:
                q.next = q.next.next
            else:
                q = q.next
        return head_node.next
