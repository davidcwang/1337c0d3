"""
Problem: 200. Number of Islands
Url: https://leetcode.com/problems/number-of-islands/
Author: David Wang
Date: 06/26/2019
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ones = []
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    ones.append((x,y))

        islands = 0
        while ones:
            cur = ones.pop()
            x, y = cur
            if grid[x][y] == '0':
                continue

            islands += 1

            queue = []
            queue.append(cur)

            while queue:
                cur = queue.pop()
                x, y = cur
                grid[x][y] = '0'

                if x-1 >= 0 and x-1 <= len(grid) - 1:
                    if grid[x-1][y] == '1':
                        queue.append((x-1, y))
                if x+1 >= 0 and x+1 <= len(grid) - 1:
                    if grid[x+1][y] == '1':
                        queue.append((x+1, y))
                if y-1 >= 0 and y-1 <= len(grid[0]) - 1:
                    if grid[x][y-1] == '1':
                        queue.append((x, y-1))
                if y+1 >= 0 and y+1 <= len(grid[0]) - 1:
                    if grid[x][y+1] == '1':
                        queue.append((x, y+1))


        return islands
