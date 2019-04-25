# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 16:37:40 2019

@author: Administrator
"""
#py2 / 得整数，py3得小数，需加int
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(re.findall("[a-zA-Z0-9]+", s))
        l=int(len(s)/2)
        if not s or len(s) == 1:
            return True
        if len(s) % 2 == 0:
            first = s[:l]
            second = s[l:]
        else:
            first = s[:l]
            second = s[l + 1:]

        return first.lower()[::-1] == second.lower()