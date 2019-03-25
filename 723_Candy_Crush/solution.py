"""
Problem: 723 Candy Crush  
Url: https://leetcode.com/problems/candy-crush/
Author: David Wang
Date: 03/24/2019
"""


class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        self.M = len(board)
        self.N = len(board[0])
        while self.match(board):
            self.drop(board)
            self.printBoard(board)
        return board

    def match(self, board):
        change = False
        crush = [[False]*self.N for row in board]
        for i in range(self.M):
            for j in range(self.N):
                val = board[i][j]
                if val:
#                    if i < self.M - 2:
#                        print(i, j, val, board[i+1][j], board[i+2][j])
                    if (i < self.M - 2 and val == board[i+1][j] and
                            val == board[i+2][j]):
                        change = True
                        for k in range(3):
                            crush[i+k][j] = True
#                    if j < self.N - 2:
#                        print(i, j, val, board[i][j+1], board[i][j+2])
                    if (j < self.N - 2 and val == board[i][j+1] and
                            val == board[i][j+2]):
                        change = True
                        for k in range(3):
                            crush[i][j+k] = True

        if change:
            for i in range(self.M):
                for j in range(self.N):
                    if crush[i][j]:
                        board[i][j] = 0

        self.printBoard(board)

        return change

    def drop(self, board):
        for j in range(self.N):
            index = self.M - 1
            for i in range(self.M-1, -1, -1):
                if board[i][j]:
                    board[index][j] = board[i][j]
                    index -= 1

            while index >= 0:
                board[index][j] = 0
                index -= 1

    def printBoard(self, board):
        for i, _ in enumerate(board):
            for j, _ in enumerate(board[0]):
                print('|{:^5}|'.format(board[i][j]), end='')
            print()
        print()

if __name__ == '__main__':
    s = Solution()
#    board = [
#            [1,1,1,13,11,11,1,],
#            [1,2,1,11,1,42,2,],
#            [7,7,7,1,7,7,7,],
#            ]

    board = [[110,5,112,113,114],
             [210,211,5,213,214],
             [310,311,3,313,314],
             [410,411,412,5,414],
             [5,1,512,3,3],
             [610,4,1,613,614],
             [710,1,2,713,714],
             [810,1,2,1,1],
             [1,2,1,2,2],
             [4,1,4,4,1014]]
    
    s.printBoard(board)
    s.printBoard(s.candyCrush(board))
