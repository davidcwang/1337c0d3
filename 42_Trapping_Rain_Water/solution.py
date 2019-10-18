"""
Problem: 42. Trapping Rain Water
Url: https://leetcode.com/problems/trapping-rain-water/
Author: David Wang
Date: 10/09/2019
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        return self.trap_dp(height)

    def trap_dp(self, height: List[int]) -> int:
        N = len(height)
        water = 0

        if N == 0:
            return water

        left_max = [0 for _ in range(N)]
        right_max = [0 for _ in range(N)]
        left_max[0] = height[0]
        right_max[-1] = height[-1]

        for i in range(1, N):
            left_max[i] = max(height[i], left_max[i - 1])

        for i in range(1, N):
            right_max[N - 1 - i] = max(height[N - 1 - i], right_max[N - i])

        for i in range(0, N):
            water += min(left_max[i], right_max[i]) - height[i]

        return water

    def trap_pointers(self, height: List[int]) -> int:
        N = len(height)
        l = 0
        r = N - 1
        water = 0

        if len(height) == 0:
            return water

        left_max = 0
        right_max = 0

        while l <= r:
            if height[l] <= height[r]:
                if height[l] > left_max:
                    left_max = height[l]
                else:
                    water += left_max - height[l]
                    l += 1

            else:
                if height[r] > right_max:
                    right_max = height[r]
                else:
                    water += right_max - height[r]
                    r += 1


if __name__ == '__main__':

    heights = [0,1,0,2,1,0,1,3,2,1,2,1]
    expected = 6
    output = Solution().trap(heights)
    print(output, expected)
    assert output == expected
