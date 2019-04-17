# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 15:31:44 2019

@author: Administrator
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum=maxSum=nums[0]
        for i in range(1,len(nums)):  
            curSum = max(nums[i],curSum+nums[i])
            maxSum = max(curSum,maxSum)
  
        return maxSum
                
        
        
        
if __name__ == '__main__':
    
    x=input()
    xlist=x.split(" ")
    nums=[int(xlist[i]) for i in range(len(xlist))] #输入字符串转化为list
    s=Solution()
    b=s.maxSubArray(nums)
    print(b)