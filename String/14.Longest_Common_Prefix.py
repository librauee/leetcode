# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:26:25 2019

@author: Administrator
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs==[]:
            return ""
        else:
            for i in range(1,len(strs)):
                l0=len(strs[0])
                li=len(strs[i])
                if l0 > li:
                    lenth = li
                else:
                    lenth = l0
                strs[0] = strs[0][:lenth]
                for j in range(lenth):
                    if strs[0][j] != strs[i][j]:
                        strs[0] = strs[0][0:j]
                        break
            return strs[0]

class Solution2(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if strs == []:
            return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            if not prefix:
                return ""
            else:
                while prefix not in strs[i][:len(prefix)] and len(prefix)>0:
                    prefix = prefix[:len(prefix)-1]
        return prefix
