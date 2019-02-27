"""
Problem: 959. Regions Cut By Slashes
Url: https://leetcode.com/problems/regions-cut-by-slashes/
Author: David Wang
Date: 02/04/2019
"""

class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        N = len(grid)
        # Each cell will have 4 numbers
        # |\ 0 /||\ 4 /|
        # |1 /\2||5 /\6|
        # |/ 3 \||/ 7 \|
        regions = DSU(4 * N * N)
        for i, row in enumerate(grid):
            for j, val in range(row):
                root = 4*N + j
                if val == '/':






class DSU(object):
    def __init__(self, N):
        self.parent = list(range(N))
        self.rank = [0] * N

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = find(self.parent(x))
        return self.parent[x] 

    def union(self, x, y):
        px = find(x)
        py = find(y)

        if self.rank[px] >= self.rank[py]:
            self.parent[py] = self.parent[px]
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = self.parent[py]
        else:
            self.root[py] = self.parent[px]
            self.rank[px] += 1


