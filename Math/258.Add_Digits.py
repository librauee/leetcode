# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 09:24:35 2019

@author: Administrator
"""

class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num))!=1:
            num=sum([int(i) for i in str(num)])
        return num
    
#O(1) Brilliant Solution
class Solution2:
    def addDigits(self, num: int) -> int:
        return num % 9 if num % 9 or not num else 9 
    
#Every number whose digits sum to a multiple of 9 is divisible by 9.
#Otherwise, the iterative sum of digits leads to the remainder when divided by 9.
#We account for the case when the number is divisible by 9 or is 0.