# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 20:12:57 2019

@author: Administrator
"""

# Solution1
# itertools模块现成的全排列：
import itertools
for i in itertools.permutations('abcd',4):
    print (''.join(i))


# Solution2
def perm(l):  
    if(len(l)<=1):  
        return [l]  
    r=[]  
    for i in range(len(l)):  
        s=l[:i]+l[i+1:]  
        p=perm(s)  
        for x in p:  
            r.append(l[i:i+1]+x)  
    return r 


# Solution3

b="a b c".split()
a="a b c d e f g".split()
def recur(l,x):
    if len(l)==1:
        print(x+l[0])
        return
    for i in range(len(l)):
        recur(l[:i]+l[i+1:],x+l[i])
recur(b,'')


print(perm(b))