# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:35:56 2019

@author: Lee
"""
# 校验身份证末位
def check(number):
    t=2
    sum1=0
    for i in range(1,len(number)):
        sum1+=int(number[-1-i])*t
        t*=2
    a=sum1%11
    b=(12-a)%11
    return True if b==int(number[-1]) else False
    
if __name__=="__main__":
    print("请输入您要验证的身份证号码：")
    input1=input()
    print(check(input1))