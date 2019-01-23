"""
Problem: 885. Spiral Matrix III
Url: https://leetcode.com/problems/spiral-matrix-iii/
Author: David Wang
Date: 01/15/2018
"""

class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        grid = [[0] * C for i in range(R)]
        visited = []
        rstep = [0, 1, 0, -1]  # step increase row-wise
        cstep = [1, 0, -1, 0]  # step increase col-wise
        i = r0
        j = c0
        # step pattern size will be 1, 1, 2, 2, 3, 3, n, n, etc
        # Max amount of direction changes would be 4 * the total number of cells
        # Each cell might need an entire spiral to get to it potentially.
        for step in range(1, 4*R*C, 2):
            for d in range(4):
                dsteps = step + int(d/2)
                for ds in range(dsteps):  # extra steps 
                    if i >= 0 and i < R and j >= 0 and j < C:
                        visited.append([i, j])
                        if len(visited) == R*C:
                            return visited

                    i += rstep[d]
                    j += cstep[d]



if __name__ == '__main__':
    s = Solution()
    #print(s.spiralMatrixIII(1, 4, 0, 0))
    print(s.spiralMatrixIII(5, 6, 1, 4))
