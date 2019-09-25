"""
Problem: 289. Game of Life
Url: https://leetcode.com/problems/game-of-life/
Author: David Wang
Date: 09/23/2019
"""


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # We will use the following convention to convey cells that need to be
        # updated after we visit every cell:
        # live --> dead
        # Label | Current | Future
        #   2   |  Alive  | Dead
        #   3   |  Dead   | Alive
        if board == None or len(board) <= 0:
            return board

        # all possible neighboring positions
        neigh_pos = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        for i, row in enumerate(board):
            for j, _ in enumerate(row):
                live_neighs = 0
                for x, y in neigh_pos:
                    # make sure indicies are within the range of the board
                    if i+x >= len(board) or i+x < 0 or j+y >= len(row) or j+y < 0:
                        continue

                    cell = board[i+x][j+y]
                    if cell == 1 or cell == 2:
                        live_neighs += 1

                # Conditions 1 and 3
                if (board[i][j] == 1 and
                    (live_neighs < 2 or live_neighs > 3)):
                    board[i][j] = 2

                # Condition 4
                elif board[i][j] == 0 and live_neighs == 3:
                    board[i][j] = 3

        # Update all cells to their new states based on the labels we gave
        for i, row in enumerate(board):
            for j, _ in enumerate(row):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1

        return board

if __name__ == '__main__':
    board = [
        [0,1,0],
        [0,0,1],
        [1,1,1],
        [0,0,0]
    ]
    target = [
        [0,0,0],
        [1,0,1],
        [0,1,1],
        [0,1,0]
    ]
    res = Solution().gameOfLife(board)
    print(res)
    assert res == target
