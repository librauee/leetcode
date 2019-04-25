# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 16:47:21 2019

@author: Administrator
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:]=s[::-1]