# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:32:37 2019

@author: Administrator
"""
class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ""
        while n != 0:
            result += chr(n%26+64)
            n = int((n-1)/26)
        return result[::-1]
