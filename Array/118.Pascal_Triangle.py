# -*- coding: utf-8 -*-
"""
Created on Wed May 29 20:34:54 2019

@author: Administrator
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
 
        n,b,res=0,[1],[]
        while n<numRows:
            res.append(b)
            b=[1]+[b[i]+b[i+1] for i in range(len(b)-1)]+[1]
            n+=1
        return res