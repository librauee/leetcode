# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 20:46:12 2019

@author: Lee
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        arr, i = [], 0
        if not head:
            return None
        while head:
            arr.append(head)
            head = head.next

        while i <= len(arr) - k:
            arr[i:i+k] = arr[i:i+k][::-1]
            i += k
        for j in range(len(arr) - 1):
            arr[j].next = arr[j+1]
        if arr:
            arr[-1].next = None
            return arr[0]