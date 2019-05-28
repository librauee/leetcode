# -*- coding: utf-8 -*-
"""
Created on Tue May 28 20:18:33 2019

@author: Administrator
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        while ransomNote:
            tem = ransomNote.pop()
            if tem not in magazine:
                return False
            else:
                magazine.remove(tem)

        return True
    
    
import collections
class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:        
        return not collections.Counter(ransomNote) - collections.Counter(magazine)