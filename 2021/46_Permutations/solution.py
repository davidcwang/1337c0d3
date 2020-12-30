"""
Problem: 46. Permutations
Url: https://leetcode.com/problems/permutations/
Author: David Wang
Date: 12/17/2020
"""

from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(nums, start):
            if start == len(nums):
                results.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                backtrack(nums, start+1)
                nums[start], nums[i] = nums[i], nums[start]


        results = []
        backtrack(nums, 0)
        return results

if __name__ == '__main__':
    nums = [1, 2, 3]
    answer = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    output = Solution().permute(nums)
    print(answer)
    print(output)
    assert(answer == output)

    nums = [0, 1]
    answer = [[0,1],[1,0]]
    output = Solution().permute(nums)
    print(answer)
    print(output)
    assert(answer == output)

    nums = [1]
    answer = [[1]]
    output = Solution().permute(nums)
    print(answer)
    print(output)
    assert(answer == output)
