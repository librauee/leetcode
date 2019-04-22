# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:49:12 2019

@author: Administrator
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result=0
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                result=max(count,result)
            else:
                count=0
        return result
    
#通过"0" split之后最长的子字符串的长度
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return len(max("".join(map(str,nums)).split('0')))
        