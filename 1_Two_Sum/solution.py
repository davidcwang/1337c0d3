"""
Problem: 1. Two Sum
Url: https://leetcode.com/problems/two-sum/description/
Author: David Wang
Date: 12/26/2017
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        Returns the indicies of the two numbers from nums that add up to target

        Args:
            nums: list of numbers
            target: the sum to match

        Returns:
            The index of the two numbers that add up to 'target'
        """
        value_to_indicies = {} # contains indicies that have this value
        for i, n in enumerate(nums):
            if n not in value_to_indicies:
                value_to_indicies[n] = []
                value_to_indicies[n].append(i)
            else:
                value_to_indicies[n].append(i)

        for i, n in enumerate(nums):
            diff = target - n
            if diff in value_to_indicies:
                for j in value_to_indicies[diff]:
                    if j != i:
                        return [i, j]

            

