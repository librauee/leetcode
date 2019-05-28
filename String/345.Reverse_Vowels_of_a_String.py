# -*- coding: utf-8 -*-
"""
Created on Tue May 28 20:29:06 2019

@author: Administrator
"""

#vowels: a,e,i,o,u
class Solution:
    def reverseVowels(self, s: str) -> str:
        s1 = []
        s2 = []
        s = list(s)
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                s1.append(s[i])
                s2.append(i)
        s1=s1[::-1]
        for j in range(len(s2)):
            s[s2[j]] = s1[j]
        return ''.join(s)