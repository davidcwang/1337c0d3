"""
Problem: 41. First Missing Positive
Url: https://leetcode.com/problems/first-missing-positive/
Author: David Wang
Date: 06/06/2020
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        left_index = 0
        right_index = len(nums) - 1

        smallest = float("inf")

        while left_index < right_index:
            left = nums[left_index]
            right = nums[right_index]

            if left < right:
                smallest = min(left, smallest)
                right -= 1

            else:
                smallest = min(right, smallest)
                left += 1

        return smallest + 1

if __name__ == '__main__':
    input = [0]


