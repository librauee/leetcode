# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 14:56:16 2019

@author: Administrator
"""

#A=[[1,2,3],[4,5,6],[7,8,9]]

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
    
        if len(A) == 0: 
            return []
        row, col = len(A), len(A[0])
        return [[A[i][j] for i in range(row)] for j in range(col)]


#zip() 压缩 zip(*)解压缩
class Solution2:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        A[::]=zip(*A)
        return A   