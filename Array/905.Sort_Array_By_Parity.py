# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:09:34 2019

@author: Administrator
"""

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:        
        B=[]
        C=[]
        for i in range(len(A)):
            if A[i]%2==0:
                B.append(A[i])
            else:
                C.append(A[i])
        B.extend(C)
        return B


#other solution
#divede in to two class :key=1,key=0,then sorted
class Solution2(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted(A, key = lambda x : x % 2)

#list Generator   
class Solution3:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return [x for x in A if x % 2 == 0] + [x for x in A if x % 2 > 0]
