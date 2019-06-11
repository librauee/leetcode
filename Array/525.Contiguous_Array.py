# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 09:56:57 2019

@author: Administrator
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        track,has=0,{0:-1}
        ress_max=0        
        for i in range(len(nums)):
            track += (1 if nums[i]==1 else -1)
            if  track not in has:
                has[track]=i
            elif ress_max <i-has[track]:
                ress_max = i-has[track]
        return ress_max