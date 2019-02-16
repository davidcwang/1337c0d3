"""
Problem: 366. Find Leaves of Binary Tree
Url: https://leetcode.com/problems/find-leaves-of-binary-tree
Author: David Wang
Date: 01/19/2019
"""

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class NodeInfo(object):
    def __init__(self, parent=None, child_count=0):
        self.parent = parent
        self.child_count = child_count


class Solution(object):
    def find_leaves_recur(self, node):
        leaves = []
        self._recur_helper(node, leaves)
        return leaves

    def _recur_helper(self, node, leaves):
        if node == None:
            return -1

        height = max(self._recur_helper(node.left, leaves),
                self._recur_helper(node.right, leaves)) + 1

        if len(leaves) <= height:
            leaves.append([])
        leaves[height].append(node.val)

        return height

    def find_leaves_iter(self, node):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """    
        ni_dict = {}
        queue = []
        leaves = []

        self.get_initial_leaves(node, ni_dict, queue)

        while queue:
            node_list = []
            for i in queue:
                node = queue.pop(0)
                node_list.append(node.val)
                ni = ni_dict[node]
                parent = ni.parent
                if parent in ni_dict:
                    parent_ni = ni_dict[parent]
                    parent_ni.child_count -= 1
                    if parent_ni.child_count == 0:
                        queue.append(parent)

            leaves.append(node_list)
        return leaves

        
    def get_initial_leaves(self, node, ni_dict, queue):
        if not node:
            return

        child_count = 0
        if node.left:
            child_count += 1
            ni_dict[node.left] = NodeInfo(node)
            self.get_initial_leaves(node.left, ni_dict, queue)
        if node.right:
            child_count += 1
            ni_dict[node.right] = NodeInfo(node)
            self.get_initial_leaves(node.right, ni_dict, queue)

        if node not in ni_dict:
            ni_dict[node] = NodeInfo(None, child_count)
        else:
            ni_dict[node].child_count = child_count
        if child_count == 0:
            queue.append(node)


if __name__ == '__main__':
    s = Solution()
    lleft = Node(-1)
    left = Node(1, lleft)
    right = Node(3)
    root = Node(2, left, right)

    leaves = []
    print(s.find_leaves_iter(root))
