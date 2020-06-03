"""
Problem: 15. 3Sum
Url: https://leetcode.com/problems/3sum/
Author: David Wang
Date: 05/31/2020
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        zero_sum_triplets = []

        for i in range(len(sorted_nums)):
            left_i = i + 1
            right_i = len(sorted_nums) - 1


            if i > 0 and sorted_nums[i-1] == sorted_nums[i]:
                continue

            a = sorted_nums[i]
            if a > 0:
                break

            while left_i < right_i:
                b = sorted_nums[left_i]
                c = sorted_nums[right_i]

                total = a + b + c

                if total > 0 or (right_i < len(sorted_nums) - 1 and c == sorted_nums[right_i + 1]):
                    right_i -= 1

                elif total < 0 or (left_i - 1 > i and b == sorted_nums[left_i - 1]):
                    left_i += 1

                # total == 0
                else:
                    zero_sum_triplets.append([a, b, c])
                    left_i += 1
                    right_i -= 1

        return zero_sum_triplets


if __name__ == '__main__':
    input = [-1, 0, 1, 2, -1, -4]
    output = Solution().threeSum(input)
    print(output)
    assert output == [ [-1, 0, 1], [-1, -1, 2] ]