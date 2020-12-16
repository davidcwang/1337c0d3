"""
Problem: 54. Spiral Matrix
Url: https://leetcode.com/problems/spiral-matrix/
Author: David Wang
Date: 06/06/2020
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        index = 0

        num_rows = None
        if len(matrix) > 0:
            num_rows = len(matrix)

        if num_rows and len(matrix[0]) > 0:
            num_cols = len(matrix[0])

        vert_window_size = num_rows
        horiz_window_size = num_cols

        while vert_window_size > 0:
            while horiz_window_size > 0:
                for

        for i, row in enumerate(matrix):



