"""
Problem: 894. All Possible Full Binary Trees
Url: https://leetcode.com/problems/all-possible-full-binary-trees/
Author: David Wang
Date: 11/18/2018
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # N should always be >= 1 since a tree with 0 nodes cannot be a valid FBT
    # but we set the 0 key in the treedict in this case so that we we don't get
    # a key error for FBT(0)
    treedict = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N not in Solution.treedict:
            fbt = []
            for leftsize in range(N):
                # rightsize will always be >= 0 since leftsize = [0, N-1]
                rightsize = N - 1 - leftsize
                for left in self.allPossibleFBT(leftsize):
                    for right in self.allPossibleFBT(rightsize):
                        node = TreeNode(0)
                        node.left = left
                        node.right = right
                        fbt.append(node)
            Solution.treedict[N] = fbt

        return Solution.treedict[N]

