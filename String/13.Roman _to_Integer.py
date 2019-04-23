# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:59:39 2019

@author: Administrator
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        for i in range(len(s)-1):
            if dic[s[i]] < dic[s[i+1]]:
                result-= dic[s[i]]
            else:
                result+=dic[s[i]]
        result+=dic[s[len(s)-1]]
        return result
