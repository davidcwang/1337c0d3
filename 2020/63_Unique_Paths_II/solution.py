"""
Problem: 63. Unique Paths II
Url: https://leetcode.com/problems/unique-paths-ii/
Author: David Wang
Date: 06/23/2020
"""

from typing import List


class Solution:
  def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    if len(obstacleGrid) == 0:
      return 0

    if len(obstacleGrid[0]) == 0:
      return 0

    paths = [[0] * len(row) for i, row in enumerate(obstacleGrid)]

    # Set the origin with a path of 1 if there is no obstacle.
    paths[0][0] = 1 if not obstacleGrid[0][0] else 0

    # Set a cell in the first row to whatever the cell is left of it unless the
    # current position has an obstacle in which we'll have to set the path to 0.
    for j in range(1, len(obstacleGrid[0])):
      paths[0][j] = paths[0][j-1] if not obstacleGrid[0][j-1] else 0

    # Set a cell in the first column to whatever the cell is left of it unless
    # the current position has an obstacle in which we'll have to set the path
    # to 0.
    for i in range(1, len(obstacleGrid)):
      paths[i][0] = paths[i-1][0] if not obstacleGrid[i-1][0] else 0

    for i, row in enumerate(obstacleGrid):
      for j, val in enumerate(row):
        if obstacleGrid[i][j] == 1:
          paths[i][j] = 0
          continue

        # Check if top space above current position is not an obstacle.
        if i > 0 and j > 0 and not obstacleGrid[i-1][j]:
          paths[i][j] += paths[i-1][j]

        if i > 0 and j > 0 and not obstacleGrid[i][j-1]:
          paths[i][j] += paths[i][j-1]

    m = len(obstacleGrid) - 1
    n = len(obstacleGrid[0]) - 1
    return paths[m][n]


if __name__ == '__main__':
  input = [
      [0,0,0],
      [0,1,0],
      [0,0,0]
  ]
  output = Solution().uniquePathsWithObstacles(input)
  assert output == 2

  input = [[1]]
  output = Solution().uniquePathsWithObstacles(input)
  assert output == 0

  input = [[1,0]]
  output = Solution().uniquePathsWithObstacles(input)
  assert output == 0

  input = [[0, 0], [0, 1]]
  output = Solution().uniquePathsWithObstacles(input)
  assert output == 0

  input = [
    [0,1,0,0,0],
    [1,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
  ]
  output = Solution().uniquePathsWithObstacles(input)
  assert output == 0
