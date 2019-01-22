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
        to_visit = (C * R) - 1  # -1 because already visited (r0, c0)
        visited = []
        rstep = [0, 1, 0, -1]  # step increase row-wise
        cstep = [1, 0, -1, 0]  # step increase col-wise
        step_scale = 1  # step pattern size will be 1, 1, 2, 2, 3, 3, n, n, etc
        i = r0
        j = c0
        diri = 0  # step direction index
        while to_visit >= 0:
            for extra in [0, 0, 1, 1]:  # extra steps 
                for k in range(step_scale):
                    if i >= 0 and i < R and j >= 0 and j < C:
                        visited.append([i, j])
                        to_visit -= 1

                    i = rstep[diri] * (k + extra)
                    j = cstep[diri] * (k + extra)

                diri += 1
                diri = diri % len(rstep)

            step_scale += 1


if __name__ == '__main__':
    s = Solution()
    print(s.spiralMatrixIII(1, 4, 0, 0))
    #print(s.spiralMatrixIII(5, 6, 1, 4))
