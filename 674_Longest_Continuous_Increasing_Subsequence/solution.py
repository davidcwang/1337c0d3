"""
Problem: 674. Longest Continuous Increasing Subsequence
Url: https://leetcode.com/problems/longest-continuous-increasing-subsequence/
Author: David Wang
Date: 06/01/2019
"""

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        longest = 1
        current = 1
        for i in range(0, len(nums)-1):
            if nums[i+1] <= nums[i]:
                current = 0
            current += 1
            if current > longest:
                longest = current
        return longest
