# -*- coding: utf-8 -*-
"""
Created on Wed May 29 21:25:48 2019

@author: Administrator
"""

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        table = dict(zip(order, 'abcdefghijklmnopqrstuvwxyz'))
        return words == sorted(words, key=lambda w: ''.join(table[c] for c in w))