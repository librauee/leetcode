# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 16:05:50 2019

@author: Administrator
"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n<5:
            return 0
        result=0
        while n!=0:
            result+= int(n/5)
            n=int(n/5)           
        return result