# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 10:53:22 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val <= l2.val:
            res = l1
            l1 = l1.next
        else:
            res = l2
            l2 = l2.next
        temp = res
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1 != None:
            temp.next = l1
        else:
            temp.next = l2
        return res 