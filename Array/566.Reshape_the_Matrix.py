# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 15:33:21 2019

@author: Administrator
"""

#nums = [[1,2], [3,4]]
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(nums)
        n=len(nums[0])        
        if m*n!=r*c:
            return nums
        else:
            ans=[]
            row_nums=[]
            for i in range(m):
                for j in range(n):
                    row_nums.append(nums[i][j])
            for i in range(r):
                ans.append(row_nums[i*c : (i+1)*c])
            return ans
