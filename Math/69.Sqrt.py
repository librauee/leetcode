# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:08:06 2019

@author: Administrator
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        a=0
        b=x
        c=int(x/2)
        while a<=b:
            c_squre=c*c
            if c_squre>x:
                b=c-1
            elif c_squre<x:
                a=c+1
            else:
                return c
                break
            c=int((a+b)/2)
        return c