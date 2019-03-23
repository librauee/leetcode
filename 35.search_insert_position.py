# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:41:26 2019

@author: Administrator
"""
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = int((right - left) / 2 + left)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left
        
        
        
if __name__ == '__main__':
    target=int(input())
    x=input()
    xlist=x.split(" ")
    nums=[int(xlist[i]) for i in range(len(xlist))] #输入字符串转化为list
    s=Solution()
    b=s.searchInsert(nums,target)
    print(b)

