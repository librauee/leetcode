# -*- coding: utf-8 -*-
"""
Created on Tue May 28 20:28:26 2019

@author: Administrator
"""
import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        collect=collections.Counter(s)
        index=0
        for i in s:
            if collect[i]==1:
                return index
            else:
                index+=1
        return -1
                