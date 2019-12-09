# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:56:47 2019

@author: Lee
"""


import math
import decimal


# 判断素数
def prime(x):
    if x<=1:
        return False
    i=2
    while i*i<=x:
        if x%i==0:
            return False
        i+=1
    return True


# 求阶乘
def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)
    
    
# 获取高精度的自然底数
def get_e(n):
    decimal.getcontext().prec=10000
    e=decimal.Decimal('1.0')
    for i in range(1,n):
        e+=1/decimal.Decimal(factorial(i))
    print(e)   
    return str(e)


# 查找第一个素数
def find(n):   
    e=get_e(n)
    for i in range(2,len(e)-9):
        number=e[i:i+10]
        if prime(int(number)):
            print(number)
            break

if __name__=='__main__':
    
    print(math.e)
    n=int(input("Please enter n:"))    
    find(n)

