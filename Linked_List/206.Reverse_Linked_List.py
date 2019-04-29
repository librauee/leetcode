# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 10:59:01 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        while head:
            nex = head.next
            head.next,pre,head = pre,head,nex
        return pre