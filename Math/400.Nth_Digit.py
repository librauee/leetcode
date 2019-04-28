# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 13:45:35 2019

@author: Administrator
"""

class Solution:
    def findNthDigit(self, n: int) -> int:
        digit=1
        base=9
        ith=1
        while n>base*digit:
            n-=base*digit
            digit+=1
            ith+=base
            base*=10
        return ord(str(ith+int((n-1)/digit))[(n-1)%digit])-ord('0')