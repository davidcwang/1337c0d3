"""
Problem: 832. Flipping an Image
Url: https://leetcode.com/problems/flipping-an-image/
Author: David Wang
Date: 06/06/2020
"""

import math
from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i, row in enumerate(A):
            # For odd lengths we need the ceiling so that range gets to the middle index of the row.
            mid_point = math.ceil(len(row)/2)

            for j in range(mid_point):
                left_val = row[j]
                right_index = len(row) - 1 - j
                right_val = row[right_index]

                # flip and invert
                row[j] = 0 if right_val == 1 else 1

                if len(row) % 2 == 0 or j != mid_point:
                    row[right_index] = 0 if left_val == 1 else 1

        return A


if __name__ == '__main__':
    input = []
    output = Solution().flipAndInvertImage(input)
    assert output == []

    input = [
       [0, 0, 1],
       [0, 1, 1]
    ]
    output = Solution().flipAndInvertImage(input)
    assert output == [
        [0, 1, 1],
        [0, 0, 1],
    ]

