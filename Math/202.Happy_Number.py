# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 17:00:20 2019

@author: Administrator
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        a=set() 
        while n!=1:     
            n=sum([int(i)**2 for i in str(n)]) 
            if n not in a:
                a.add(n)
            else:                
                return False
        return True