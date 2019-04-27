# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 21:07:10 2019

@author: Administrator
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        return 2**(int(math.log(n,2)))==n