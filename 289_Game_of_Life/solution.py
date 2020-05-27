"""
Problem: 289. Game of Life
Url: https://leetcode.com/problems/game-of-life/
Author: David Wang
Date: 05/19/2020
"""

from typing import List

ALIVE = 1
DEAD = 0
ALIVE_PLACE_HOLDER = -1
DEAD_PLACE_HOLDER = -2

class Solution:


    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self._mark_next_step(board)
        self._update_board(board)

    def _mark_next_step(self, board):
        """
        Use non-zero numbers to mark placeholders for 0's and 1's that should
        be mutated into the next stage.
        """
        for i, row in enumerate(board):
            for j, cell in enumerate(row):

                num_neighbors = 0

                # Check Top alive
                if i > 0 and (board[i-1][j] == 1 or board[i-1][j] == DEAD_PLACE_HOLDER):
                    num_neighbors +=1

                # Check Left alive
                if j > 0 and (board[i][j-1] == 1 or board[i][j-1] == DEAD_PLACE_HOLDER):
                    num_neighbors +=1

                # Check Bottom alive
                if i < len(board) - 1 and (board[i+1][j] == 1 or board[i+1][j] == DEAD_PLACE_HOLDER):
                    num_neighbors += 1

                # Check Right alive
                if j < len(row) - 1 and (board[i][j+1] == 1 or board[i][j+1] == DEAD_PLACE_HOLDER):
                    num_neighbors += 1

                # Check Top Left alive
                if i > 0 and j > 0 and (board[i-1][j-1] == 1 or board[i-1][j-1] == DEAD_PLACE_HOLDER):
                    num_neighbors += 1

                # Check Top Right Alive
                if i > 0 and j < len(row) - 1 and (board[i-1][j+1] == 1 or board[i-1][j+1] == DEAD_PLACE_HOLDER):
                    num_neighbors += 1

                # Check Bottom Right Alive
                if i < len(board) - 1 and j < len(row) - 1 and (board[i+1][j+1] == 1 or board[i+1][j+1] == DEAD_PLACE_HOLDER):
                    num_neighbors += 1

                # Check Bottom Left Alive
                if i < len(board) - 1 and j > 0 and (board[i+1][j-1] == 1 or board[i+1][j-1] == DEAD_PLACE_HOLDER):
                    num_neighbors += 1

                self._mark_next_cell_state(board, i, j, num_neighbors)


    def _mark_next_cell_state(self, board, i, j, num_neighbors):
        """
        # 1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
        # 2. Any live cell with two or three live neighbors lives on to the next generation.
        # 3. Any live cell with more than three live neighbors dies, as if by over-population..
        # 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        # Mark the next state of the cell.
        """
        cell_state = board[i][j]

        # 1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
        if cell_state == ALIVE and (num_neighbors < 2):
            board[i][j] = DEAD_PLACE_HOLDER

        # 3. Any live cell with more than three live neighbors dies, as if by over-population..
        if cell_state == ALIVE and (num_neighbors > 3):
            board[i][j] = DEAD_PLACE_HOLDER

        # 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        if cell_state == DEAD and num_neighbors == 3:
            board[i][j] = ALIVE_PLACE_HOLDER

        # All other states will cause the cells to stay in the same state.

    def _update_board(self, board):
        for i, row in enumerate(board):
            for j, cell in enumerate(row):

                if cell == ALIVE_PLACE_HOLDER:
                    board[i][j] = ALIVE

                elif cell == DEAD_PLACE_HOLDER:
                    board[i][j] = DEAD

    def print_board(self, board):
        for row in board:
            print(row)

        print()

if __name__ == '__main__':
    board = [
        [0,1,0],
        [0,0,1],
        [1,1,1],
        [0,0,0]
    ]
    Solution().print_board(board)
    Solution().gameOfLife(board)
    Solution().print_board(board)

