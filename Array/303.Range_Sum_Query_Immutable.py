# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 23:21:21 2019

@author: Administrator
"""

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        
    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
        
    
# DP思路
class NumArray2(object):
 
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = [0] *len(nums)
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            self.dp[i] = sums
 
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.dp[j]
        else:
            return self.dp[j] - self.dp[i-1]
