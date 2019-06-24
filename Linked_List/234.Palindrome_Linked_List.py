# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 20:21:53 2019

@author: Lee
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        if len(a)%2==0:
            for i in range(len(a)/2):
                if a[i]!=a[-i-1]:
                    return False
            return True
        else:
            for i in range((len(a)+1)/2):
                if a[i]!=a[-i-1]:
                    return False
            return True