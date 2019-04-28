# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 10:13:17 2019

@author: Administrator
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n>0:
            if n%3==0:
                n/=3
            else:
                break
        return n==1
#without loop
class Solution2:
    def isPowerOfThree(self, n: int) -> bool:
        return n>0 and 1162261467%n==0  #3^19=1162261467是小于2^31最大的3的倍数