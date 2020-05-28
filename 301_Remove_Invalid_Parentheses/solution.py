"""
Problem: 55. Jump Game
Url: https://leetcode.com/problems/jump-game/
Author: David Wang
Date: 05/26/2020
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 2, -1, -1):
            val = nums[i]
