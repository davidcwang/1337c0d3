"""
Problem: 55. Jump Game
Url: https://leetcode.com/problems/jump-game/
Author: David Wang
Date: 05/26/2020
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump_bools = [False] * len(nums)
        jump_bools[-1] = True
        left_most_good = max(0, len(nums) - 1)
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= left_most_good:
                left_most_good = i
                jump_bools[i] = True

        return jump_bools[0]

if __name__ == '__main__' :
    input = [0]
    output = Solution().canJump(input)
    assert output == True

    input = [1, 0]
    output = Solution().canJump(input)
    assert output == True

    input = [0, 0]
    output = Solution().canJump(input)
    assert output == False

    input = [2, 0, 0]
    output = Solution().canJump(input)
    assert output == True

    input = [2,3,1,1,4]
    output = Solution().canJump(input)
    assert output == True

    input = [3,2,1,0,4]
    output = Solution().canJump(input)
    assert output == False

    input = [2, 0]
    output = Solution().canJump(input)
    assert output == True
