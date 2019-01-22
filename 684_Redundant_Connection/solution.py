"""
Problem: 684. Redundant Connection
Url: https://leetcode.com/problems/redundant-connection/
Author: David Wang
Date: 01/18/2019
"""

import sys

class Solution(object):
    self.rank = {}
    self.root= {}
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        redun = None
        for e in edges:
            src, dest = e
            srcr, srcpar = get_root(src)
            destr, destpar = get_root(dest)
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


    def get_root(self, i, parents=[]):
        if self.root[i] == i:
            return i, parents
        parents.append(i)
        get_root(self.root[i], parents)

    def union(

