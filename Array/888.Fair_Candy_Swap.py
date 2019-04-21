# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 16:21:42 2019

@author: Administrator
"""

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_A, sum_B, set_B = sum(A), sum(B), set(B)
        target = (sum_A + sum_B) / 2
        for a in A:
            b = target - (sum_A - a)
            if  b in set_B:
                return [a, b]