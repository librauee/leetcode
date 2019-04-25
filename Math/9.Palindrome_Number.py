# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:07:40 2019

@author: Administrator
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        if x[:]==x[::-1]:
            return True 
        else:
            return False