# -*- coding: utf-8 -*-
"""
Created on Wed May 29 20:27:27 2019

@author: Administrator
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:]=sorted((nums1[:m]+nums2[:n]))