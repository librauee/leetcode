# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 13:17:39 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#l2 go first for n+1 steps
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        res = l1 = l2 = ListNode(0)
        res.next = head
        for i in range(n+1): 
            l2 = l2.next
        while l2:
            l1,l2 = l1.next,l2.next
        l1.next = l1.next.next
        return res.next
    
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        Node=[]
        while head:
            Node.append(head)
            head=head.next
        n=len(Node)-n
        if n==0:
            if len(Node)>1:
                Node[0].val=Node[1].val
                Node[0].next=Node[1].next
            else:
                return None
        else:
            Node[n-1].next=Node[n].next
        return Node[0]