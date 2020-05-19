"""
Problem: 684. Redundant Connection
Url: https://leetcode.com/problems/redundant-connection/
Author: David Wang
Date: 01/18/2019
"""

import sys

class Solution(object):
    def __init__(self):
        N = 1001
        self.rank = [0] * N
        self.root = [x for x in range(N)]

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        redun = None
        for e in edges:
            src, dest = e
            srcr = self.find(src)
            destr = self.find(dest)

            # If an edge that has not been added yet and the two numbers that
            # are being added point to the same root, this means that we have
            # created a cycle.
            if self.root[src] == self.root[dest]:
                redun = [src, dest]

            if self.rank[srcr] > self.rank[destr]:
                self.root[destr] = srcr
            elif self.rank[srcr] < self.rank[destr]:
                self.root[srcr] = destr
            else:
                self.root[destr] = srcr
                self.rank[srcr] += 1

        return redun

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

if __name__ == '__main__':
    edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    print(Solution().findRedundantConnection(edges))
