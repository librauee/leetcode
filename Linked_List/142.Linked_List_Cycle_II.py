# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 20:11:48 2019

@author: Lee
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#  2(a+b)=a+2b+c => a=c 即快慢指针相遇后再走一个头结点到环入口的距离
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1=p2=head
        while p1 and p2 and p2.next:
            p1=p1.next
            p2=p2.next.next
            if p1==p2:
                p3=head
                while p1!=p3:
                    p3=p3.next
                    p1=p1.next
                return p3
        return None