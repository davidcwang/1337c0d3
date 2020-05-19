"""
Problem: 122. Best Time to Buy and Sell Stock II
Url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/ 
Author: David Wang
Date: 06/12/2019
"""

import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        gain = 0
        for i in range(0, len(prices) - 1):
            diff = prices[i+1] - prices[i]
            if diff > 0:
                gain += diff
        return gain

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))

    prices = [1,2,3,4,5]
    print(Solution().maxProfit(prices))

    prices = [7,6,4,3,1]
    print(Solution().maxProfit(prices))
