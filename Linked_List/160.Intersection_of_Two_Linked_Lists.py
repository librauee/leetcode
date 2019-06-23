# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 08:35:35 2019

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 字典法
# 将链表A的节点地址存入字典中,然后在字典检索链表B的节点地址，占用辅助空间O(n)

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        dic={}
        while headA:
            dic[headA]=1
            headA=headA.next
        while headB:
            if headB in dic:
                return headB
            headB=headB.next
        return None


# 指针追逐法
# p,q分别为headA,headB的指针，指针在两链表的长度上追逐
# 若p,q同时达到地址相同的节点，返回p，q任一
# 若没有相同的节点，各自走了两链表的长度，返回None



class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        while(p1 != p2):
            p1 = headB if p1 == None else p1.next
            p2 = headA if p2 == None else p2.next
        return p1