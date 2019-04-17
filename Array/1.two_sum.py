# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 09:28:17 2019

@author: Administrator
"""
import time

class Solution_n_square(object):
    def twoSum(self, nums, target):
        result = []
        t1 = time.time()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j])== target:
                    result.append(i)
                    result.append(j)
                    print(time.time() - t1)
                    return result
                
                
class Solution_n(object):
    def twoSum(self, nums, target):       
        dic = {}
        t1 = time.time()
        for i in range(len(nums)):
            if nums[i] in dic:
                print(time.time() - t1)
                return [dic[nums[i]],i]              
            else:
                dic[target-nums[i]] = i

               
if __name__ == '__main__':
    target=int(input())  #输入字符串转化为int类型数据
    x=input()
    xlist=x.split(" ")
    nums=[int(xlist[i]) for i in range(len(xlist))] #输入字符串转化为list
    s=Solution_n()
    b=s.twoSum(nums,target)
    print(b)