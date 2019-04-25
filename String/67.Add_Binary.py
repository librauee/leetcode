# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 15:58:03 2019

@author: Administrator
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = 0
        for i in range(len(a)):
            result += pow(2, i)*int(a[len(a)-i-1])
        for i in range(len(b)):
            result += pow(2, i)*int(b[len(b)-i-1])
        s = '{:b}'.format(result)
        return s
    
    
class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        num=int(a,2)+int(b,2)
        ans=bin(num)
        return ans[2:]  #0b开口，第三位起是二进制数
