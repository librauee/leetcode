# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 21:43:58 2019

@author: Administrator
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0 or n == 1:
            return 0
        minbuy=prices[0]
        maxprof=0
        for i in range(1,n):
            minbuy=min(minbuy,prices[i])
            maxprof=max(maxprof,prices[i]-minbuy)
        return maxprof