"""
Problem: 684. Redundant Connection
Url: https://leetcode.com/problems/redundant-connection/
Author: David Wang
Date: 01/18/2019
"""

import sys

class Solution(object):
    self.rank = [0] * 1000
    self.root= range(1000) 

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        redun = None
        for e in edges:
            src, dest = e
            srcr = find(src)
            destr = find(dest)

            if rank[srcr] > rank[destr]:
                self.root[destr] = srcr
                self.root = map(lambda i: self.root[i] = destr, srcrpar)
            elif rank[srcr] < rank[destr]:
                self.root[srcr] = destr 
                self.root = map(lambda i: self.root[i] = srcr, destr)
            else:
                self.root[destr] = srcr
                self.root = map(lambda i: self.root[i] = destr, srcrpar)
                self.rank[destr] += len(srcrpar)

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = find(self.root[x])
        return x 
