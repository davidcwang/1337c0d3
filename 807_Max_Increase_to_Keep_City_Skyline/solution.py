"""
Problem: 807. Max Increase to Keep City Skyline
Url: https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/
Author: David Wang
Date: 9/5/2018
"""

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_i = [0] * len(grid)
        max_j = [0] * len(grid[0])
        orig_sum = 0
        new_sum = 0

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x > max_i[i]:
                    max_i[i] = x
                if x > max_j[j]:
                    max_j[j] = x

                orig_sum += x

        for i, x in enumerate(max_i):
            for j, y in enumerate(max_j):
                if x > y:
                    new_sum += y
                else:
                    new_sum += x

        return new_sum - orig_sum
        
