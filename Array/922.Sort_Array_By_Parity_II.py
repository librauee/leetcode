# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 17:31:03 2019

@author: Administrator
"""

#A=[4,2,5,7]
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        B=A.copy()
        even=0
        odd=1
        length=len(A)
        for a in A:
            if a%2==0:
                B[even]=a
                if(even<length-2):
                    even+=2
            else:
                B[odd]=a
                if(odd<length):
                    odd+=2
        return B
        