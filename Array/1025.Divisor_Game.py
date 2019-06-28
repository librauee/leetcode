# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 07:54:21 2019

@author: Administrator
"""

class Solution:
    def divisorGame(self, N: int) -> bool:
        result=[False for i in range(N+1)]
        for i in range(2,N+1):
            for j in range(1,i):
                if i%j==0 and result[i-j]==False:
                    result[i]=True
                    break
        return result[N]


# 另解   
class Solution2:
    def divisorGame(self, N: int) -> bool:
        return N%2==0