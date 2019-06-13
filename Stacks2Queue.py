# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:29:07 2019

@author: Administrator
"""

class QueueWithTwoStacks(object):
    def __init__(self):
        self._stack1 = []
        self._stack2 = []
    def appendTail(self,x):
        self._stack1.append(x)
    def deleteHead(self):
        if self._stack2:
            return self._stack2.pop()
        else:
            if self._stack1:
                while self._stack1:
                   self._stack2.append(self._stack1.pop())
                return self._stack2.pop()
            else:
                return None
    def getQueue(self):
        return self._stack1
q = QueueWithTwoStacks()
q.appendTail(1)
q.appendTail(2)
q.appendTail(3)
print(q.getQueue())
#q.deleteHead()
print(q.deleteHead())
print(q.deleteHead())
print(q.deleteHead())
