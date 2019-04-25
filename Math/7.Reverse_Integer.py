# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 16:56:14 2019

@author: Administrator
"""

class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            x_reverse=0
            l=len(str(x))
            for i in range(l):
                t=x%10
                x=int(x/10)
                x_reverse+=t*pow(10,l-1)
                l-=1
            return x_reverse if x_reverse<=pow(2,31)-1 else 0
        else:
            x_reverse=0
            x=-x
            l=len(str(x))
            for i in range(l):
                t=x%10
                x=int(x/10)
                x_reverse+=t*pow(10,l-1)
                l-=1
            return -x_reverse if x_reverse<=pow(2,31)-1 else 0
    