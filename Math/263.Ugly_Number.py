# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 09:57:06 2019

@author: Administrator
"""

class Solution:
    def isUgly(self, num: int) -> bool:
        if num<=0:
            return False
        elif num>=1:
            for i in [2,3,5]:
                while num%i==0:
                    num/=i
        return num==1
    
