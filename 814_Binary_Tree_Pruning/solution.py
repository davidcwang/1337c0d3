"""
Problem: 814. Binary Tree Pruning
Url: https://leetcode.com/problems/binary-tree-pruning/description/
Author: David Wang
Date: 11/1/2018
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return root if self.recurseRemove(root) else None

    def recurseRemove(self, node):
        if node == None:
            return False

        left = self.recurseRemove(node.left)
        right = self.recurseRemove(node.right)

        if not left: node.left = None
        if not right: node.right = None

        return node.val or left or right

    def inorderTraversal(self, node):
        if not node:
            return
        self.inorderTraversal(node.left)
        print('{}: {}'.format(node, node.val))
        self.inorderTraversal(node.right)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)

    print('Before')
    s.inorderTraversal(root)

    s.pruneTree(root)

    print('After')
    s.inorderTraversal(root)
