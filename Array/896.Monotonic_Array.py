# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 16:40:01 2019

@author: Administrator
"""

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        count1=0
        count2=0
        n=len(A)
        for i in range(n-1):
            temp=A[i+1]-A[i]
            if temp>=0:
                count1+=1
            if temp<=0:
                count2+=1
        if count1==n-1 or count2==n-1:
            return True
        else:
            return False
        
#other solution        
class Solution2(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return self.isIncrease(A) or self.isDecrease(A)
        
    def isIncrease(self, A):
        return all(A[i] - A[i+1] >= 0 for i in range(len(A) - 1))
        
    def isDecrease(self, A):
        return all(A[i] - A[i+1] <= 0 for i in range(len(A) - 1))
