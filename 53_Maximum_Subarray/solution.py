"""
Problem: 53. Maximum Subarray
Url: https://leetcode.com/problems/maximum-subarray/
Author: David Wang
Date: 07/06/2019
"""

import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start = 0
        cur_len = -sys.maxsize - 1
        max_len = -sys.maxsize - 1
        for i, x in enumerate(nums):
            if x > cur_len + x:
                start = i

            cur_len = max(x, cur_len + x)
            max_len = max(max_len, cur_len)

        return max_len
