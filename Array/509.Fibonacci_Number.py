# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 17:31:03 2019

@author: Administrator
"""

class Solution:
    def fib(self, N: int) -> int:
        if N==0:
            return 0
        elif N==1:
            return 1
        else:            
            return self.fib(N-1)+self.fib(N-2)
        
#iteration,better
class Solution2:
    
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N==0: return 0
        pre = 1 #f(n-1)
        ppre = 0 #f(n-1)
        for i in range(1,N):
            pre,ppre =  pre+ppre,pre
            
        return pre
