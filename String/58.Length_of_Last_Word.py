# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 15:35:12 2019

@author: Administrator
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s.split()) == 0:
            return 0        
        else:
            s=s.split()
            return len(s[-1])