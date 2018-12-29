"""
Problem: 419. Battleships in a Board 
Url: https://leetcode.com/problems/battleships-in-a-board/
Author: David Wang
Date: 12/28/2018
"""

class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ships = 0
        for i, row in enumerate(board):
            for j, val in enumerate(board[i]):

                if board[i][j] == '.':
                    continue
                elif i > 0 and board[i-1][j] == 'X': continue
                elif j > 0 and board[i][j-1] == 'X': continue

                ships += 1

        return ships

if __name__ == '__main__':
    s = Solution()
    board = [['X', '.', '.', 'X'],
	     ['.', '.', '.', 'X'],
	     ['.', '.', '.', 'X']]
    assert s.countBattleships(board) == 2

