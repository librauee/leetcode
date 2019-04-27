# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:42:34 2019

@author: Administrator
"""

class Solution:
    def titleToNumber(self, s: str) -> int:
        dic={}
        result=0
        d=1
        for i in range(26):
            dic[chr(65+i)]=i+1
        for i in range(len(s)):
            result+=dic[s[-1-i]]*d
            d*=26
        return result
    
class Solution2:
    def titleToNumber(self, s: str) -> int:
        
        result=0
        d=1
        for i in range(len(s)):
            result+=(ord(s[-1-i])-64)*d
            d*=26
        return result