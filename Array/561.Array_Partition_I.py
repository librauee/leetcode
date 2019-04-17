# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:11:26 2019

@author: Administrator
"""

#A=[1,4,3,2]
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums=sorted(nums)
        result=sum(nums)-sum(nums[::-2])
        return result
    