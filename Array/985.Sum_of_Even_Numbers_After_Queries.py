# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 09:16:40 2019

@author: Administrator
"""
#timeout
#A = [1,2,3,4]
#queries = [[1,0],[-3,1],[-4,0],[2,3]]
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        sum1=[]

        for query in queries:
            A[query[1]]+=query[0]
            sum0=0
            for i in range(len(A)):
                if A[i]%2==0:
                    sum0+=A[i]   
            sum1.append(sum0)
        return sum1
    
#Success
class Solution2:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        total=sum([a for a in A if a%2==0])
        res=[]
        for v,i in queries:
            if A[i]%2==0:
                total-=A[i]
            A[i]+=v
            if A[i]%2==0:
                total+=A[i]
            res.append(total)
        return res