"""
Problem: 861 Score After Flipping Matrix 
Url: https://leetcode.com/problems/score-after-flipping-matrix/ 
Author: David Wang
Date: 11/3/2018
"""
class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        # if left column is partially 0's and partially 1's we will perform row
        # flips to make the left most column all 1's.
        if not self._col_all_ones(A, 0) and not self._col_all_zeros(A, 0):
            self._flip_col(A, 0)
            self._greedy_flip_rows(A)

        # if left column is all 0's then we want to flip the column
        elif self._col_all_zeros(A, 0):
            self._flip_col(A, 0)

        # After converting the left most col to all 1's we will no longer do
        # any row operations and only do col operations from 1 -> length(row) - 1
        self._greedy_flip_cols(A)
        return self._calculate_score(A)

    def _calculate_score(self, A):
        # convert each binary row to a decimal value
        score = 0
        for i, row in enumerate(A):
            score += sum([2**j if val == 1 else 0 for j, val in enumerate(row)])
        return score 

    def _greedy_flip_rows(self, A):
        for i, row in enumerate(A):
            if row[0] == 0:
                self._flip_row(A, i)

    def _greedy_flip_cols(self, A):
        if len(A[0]) > 1:
            for i in range(1, len(A[0])):
                if self._should_flip_col(A, i):
                    self._flip_col(A, i)

    def _flip_row(self, A, index):
        A[index] = [0 if val == 1 else 1 for val in A[index]]
    
    def _flip_col(self, A, index):
        for row in A:
            row[index] = 0 if row[index] else 1

    def _should_flip_row(self, A, index):
        # if less than half of the row are 1's we should flip
        return A[index].count(1) < len(A[index]) / 2

    def _should_flip_col(self, A, index):
        # if less than half of the column are 1's we should flip
        num_ones = 0
        for row in A:
            if row[index]:
                num_ones += 1
        return num_ones < len(A) / 2

    def _col_all_ones(self, A, index):
        num_ones = 0
        for row in A:
            if row[index]:
                num_ones += 1
        return num_ones == len(A)

    def _col_all_zeros(self, A, index):
        return A[index].count(0) == len(A)

if __name__ == '__main__':
    s = Solution()
    A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    print(s.matrixScore(A))
