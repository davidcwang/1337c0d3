"""
Problem: 750 Number Of Corner Rectangles 
Url: https://leetcode.com/problems/number-of-corner-rectangles 
Author: David Wang
Date: 02/04/2019
"""

class Solution(object):
    def corner_rectangles(self, grid):
        total = 0
        for i, _ in enumerate(grid):
            for j in range(i+1, len(grid)):

                count = 0
                for k, _ in enumerate(grid[i]):
                    # increase count if both are 1
                    count += grid[i][k] * grid[j][k]  
                total += int(count * (count-1) / 2)

        return total

if __name__ == '__main__':
    s = Solution()

    grid1 = [[1, 0, 0, 1, 0],
            [0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0],
            [1, 0, 1, 0, 1]]

    grid2 = [[1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]]

    grid3 = [[1, 1, 1, 1]]

    print(s.corner_rectangles(grid1))
    print(s.corner_rectangles(grid2))
    print(s.corner_rectangles(grid3))
