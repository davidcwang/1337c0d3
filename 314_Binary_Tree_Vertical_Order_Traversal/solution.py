"""
Problem: 314. Binary Tree Vertical Order Traversal
Url: https://leetcode.com/problems/binary-tree-vertical-order-traversal/
Author: David Wang
Date: 10/16/2019
"""

from typing import Dict, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        vert_list = self._get_vert_list_iter(root)
        return vert_list

    def _get_vert_list_iter(self, root: TreeNode) -> List[List[int]]:
        smallest_horiz = 0
        horiz_map = {smallest_horiz: [root.val]}
        queue = [(smallest_horiz, root)]

        # level order traversal
        while queue:
            horiz_i, current = queue.pop(0)

            left = current.left
            right = current.right

            if left:
                left_i = horiz_i - 1
                if left_i < smallest_horiz:
                    smallest_horiz = left_i
                queue.append((left_i, left))

                if left_i not in horiz_map:
                    horiz_map[left_i] = []
                horiz_map[left_i].append(left.val)

            if right:
                right_i = horiz_i + 1
                if right_i < smallest_horiz:
                    smallest_horiz = right_i
                queue.append((right_i, right))

                if right_i not in horiz_map:
                    horiz_map[right_i] = []
                horiz_map[right_i].append(right.val)

        vert_list = self._build_vert_list(horiz_map, smallest_horiz)

        return vert_list

    def _build_vert_list(self, horiz_map: Dict[int, List[int]],
                         smallest_horiz: int) -> List[List[int]]:
        i = smallest_horiz
        traversal_list = []

        while True:
            nodes = horiz_map[i]
            traversal_list.append(nodes)

            i += 1
            if i not in horiz_map:
                break

        return traversal_list
