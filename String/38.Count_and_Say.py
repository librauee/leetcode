# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 14:16:29 2019

@author: Administrator
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        if n==2:
            return "11"
        pre="11"
        for i in range(3,n+1):
            result=''
            count=1
            for j in range(1,len(pre)):
                if pre[j-1]==pre[j]:
                    count+=1
                else:
                    result+=str(count)+pre[j-1]  
                    count=1

            result+=str(count)+pre[j]  
            pre=result
        return pre