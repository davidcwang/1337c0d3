"""
Problem: 987. Vertical Order Traversal of a Binary Tree
Url: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
Author: David Wang
Date: 05/27/2020
"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.left_most = 0
        self.index_map = {}

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        traversal = []
        self.bfs(root)

        index = self.left_most

        while index in self.index_map:
            traversal.append(list(map(lambda x: x[0], sorted(self.index_map[index], key=(lambda x: (x[1], x[0]))))))
            index += 1

        return traversal

    def bfs(self, node):
        queue = []
        queue.append((node, 0, 0))

        while queue:
            node, c, generation = queue.pop(0)

            if c not in self.index_map:
                self.index_map[c] = []

            self.index_map[c].append((node.val, generation))

            if node.left and node.left.val:
                self.left_most = min(self.left_most, c-1)
                queue.append((node.left, c-1, generation+1))

            if node.right and node.right.val:
                queue.append((node.right, c+1, generation+1))

