# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 22:15:01 2019

@author: Administrator
"""

class Solution:
    def countBits(self, num: int) -> List[int]:
        List1 = [0]
        while(len(List1)<=num):
            List2 = [i+1 for i in List1]
            List1 = List1+List2

        return List1[:num+1]