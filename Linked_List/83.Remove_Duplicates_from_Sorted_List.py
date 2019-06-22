# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 22:54:29 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head is None:
            return head
        p=head
        while p.next:
            if p.val==p.next.val:
                p.next=p.next.next
            else:
                p=p.next
        return head