# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 12:31:34 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0   
        result = l3 = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            l3.next = ListNode(carry%10)
            l3 = l3.next
            carry=int(carry/10)
        return result.next