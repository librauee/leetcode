# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:21:45 2019

@author: Administrator
"""


class Solution:
    def isValid(self, s: str) -> bool:
        a = {')':'(', ']':'[', '}':'{'}
        l = [None]
        for i in s:
            if i in a and a[i] == l[-1]:
                l.pop()
            else:
                l.append(i)
        return len(l)==1



class Solution2:
    def isValid(self, s: str) -> bool:
        i = 0
        l = len(s)/2
        while s and i <= l:
            s = s.replace('()','')
            s = s.replace('[]','')
            s = s.replace('{}','')
            i += 1        
        return not s