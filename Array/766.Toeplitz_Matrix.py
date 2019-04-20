# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 15:31:31 2019

@author: Administrator
"""

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j]!=matrix[i+1][j+1]:
                    return False
        return True