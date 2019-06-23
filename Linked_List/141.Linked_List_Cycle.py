# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 08:13:28 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 快指针走两步慢指针走一步，若相遇则存在环

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        p1=p2=head
        while p2.next and p2.next.next:
            p1=p1.next
            p2=p2.next.next
            if p1==p2:
                return True
        return False