# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 13:46:52 2019

@author: Administrator
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        index = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]

        return index + 1
    
    


if __name__ == '__main__':
    x=input()
    xlist=x.split(" ")
    nums=[int(xlist[i]) for i in range(len(xlist))] #输入字符串转化为list
    s=Solution()
    b=s.removeDuplicates(nums)
    print(b)