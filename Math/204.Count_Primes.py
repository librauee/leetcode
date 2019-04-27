# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 17:01:14 2019

@author: Administrator
"""
#time limit exceeded
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        else:
            result=[]
        for i in range(2,n):
            flag=0
            for j in range(2,i):
                if i%j ==0:
                    flag=1
            if flag==0:
                result.append(i)
        return len(result)
    
class Solution2:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0

        digits = [1]*n
        digits[0] = digits[1] = 0

        for i in range(2, int(n**0.5)+1):
            if digits[i] == 1:
                for j in range(i+i, n, i):
                    digits[j] = 0

        return sum(digits)