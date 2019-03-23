# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:21:46 2019

@author: Administrator
"""

class Solution:
    def removeElement(self, nums, val):
        '''
        type nums: List[int]
        type val:  int
        rtype:    int
        
        '''
        index=0
        print(val)
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[index] = nums[i]
                index += 1
        return index

        
        
        
if __name__ == '__main__':
    val=int(input())
    x=input()
    xlist=x.split(" ")
    nums=[int(xlist[i]) for i in range(len(xlist))] #输入字符串转化为list
    s=Solution()
    b=s.removeElement(nums,val)
    print(b)