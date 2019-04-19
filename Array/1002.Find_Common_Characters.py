# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 18:13:01 2019

@author: Administrator
"""
import collections

class Solution:
    def commonChars(self, A):
        length=len(A)
        dic=[collections.Counter(A[i]) for i in range(length)]
        #print(dic[0])
        #以dic[0]第一项为比较
        for i in range(1,length):
            for key in dic[0]:
                dic[0][key]=min(dic[0][key],dic[i][key])
        
        res=[]
        for key in dic[0]:
            for i in range(dic[0][key]):
                res.append(key)
        return res
    
#  &运算
class Solution2:
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        compare = collections.Counter(A[0])  
        
        for a in A:
            compare &= collections.Counter(a)
                
        return list(compare.elements())
