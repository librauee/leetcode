# -*- coding: utf-8 -*-
"""
Created on Wed May 29 20:23:55 2019

@author: Administrator
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            a = 1
            b = 2
            for i in range(2,n):
                a,b = b,(a+b)
            return b