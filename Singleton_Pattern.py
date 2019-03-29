# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 20:20:23 2019

@author: Administrator

"""
#单例模式（Singleton Pattern）是一种常用的软件设计模式
#该模式的主要目的是确保某一个类只有一个实例存在。
#当你希望在整个系统中，某个类只能出现一个实例时，单例对象就能派上用场。

#1.使用模块
#my_singleton.py

class My_Singleton(object):
    def foo(self):
        pass
    
my_singleton=My_Singleton()

from mysingleton import my_singleton
my_singleton.foo()


#2.使用__new__
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)  
        return cls._instance  
 
class MyClass(Singleton):  
    a = 1
    
one=MyClass()
two=MyClass()
print(one==two)
print(one is two)
print(id(one),id(two))
'''
True
True
3206951584432 3206951584432
'''


#3.使用装饰器
from functools import wraps
 
def singleton(cls):
    instances = {}
    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance
 
@singleton
class MyClass(object):
    a = 1

#使用 metaclass
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass(metaclass=Singleton):
    pass












