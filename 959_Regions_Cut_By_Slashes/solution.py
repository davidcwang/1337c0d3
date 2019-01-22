"""
Problem: 959. Regions Cut By Slashes
Url: https://leetcode.com/problems/regions-cut-by-slashes/
Author: David Wang
Date: 01/15/2018
"""

class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        H = len(grid)    # Height
        W = len(grid[0])    # Width
