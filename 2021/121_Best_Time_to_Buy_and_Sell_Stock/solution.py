"""
Problem: 238. Product of Array Except Self
Url: https://leetcode.com/problems/product-of-array-except-self/
Author: David Wang
Date: 12/31/2020
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m_profit = 0

        if not prices:
            return 0

        min_price = prices[0]

        for i in range(len(prices) - 1):
            if prices[i] < min_price:
                min_price = prices[i]

            diff = prices[i+1] - min_price

            if diff > m_profit:
                m_profit = diff

        return m_profit

if __name__ == '__main__':
    input = [7,1,5,3,6,4]
    answer = 5
    output = Solution().maxProfit(input)
    assert(answer == output)

