# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 10:04:40 2019

@author: Administrator
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=sum(nums)
        b=len(nums)*(len(nums)+1)/2
        return int(b-a)