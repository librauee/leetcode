# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 13:31:37 2019

@author: Administrator
"""

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([a ** 2 for a in A])

if __name__ == '__main__':
    x=input()
    xlist=x.split(" ")
    A=[int(xlist[i]) for i in range(len(xlist))] #输入字符串转化为list
    s=Solution()
    b=s.sortedSquares(A)
    print(b)