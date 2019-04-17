# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:32:56 2019

@author: Administrator
"""

  
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        B=[]
        for a in A:
            for i in range(len(a)):
                if a[i]==0:
                    a[i]=1
                else:
                    a[i]=0
            B.append(a[::-1])
        return B
    

#other Solution
#异或 xor
class Solution2:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B=[]
        for a in A:
            for i in range(len(a)):
                a[i]^=1
            B.append(a[::-1])
        return B

        
#A=[[1,1,0],[1,0,1],[0,0,0]]       
