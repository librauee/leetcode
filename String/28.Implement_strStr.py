# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:00:56 2019

@author: Administrator
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len1=len(haystack)
        len2=len(needle)
        for i in range(len1-len2+1):
            if haystack[i:i+len2]==needle:
                return i
        return -1
    
class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle  not in haystack:
            return -1
        return haystack.find(needle)