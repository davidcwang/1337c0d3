"""
Problem: 701 Insert into a Binary Search Tree
Url: https://leetcode.com/problems/insert-into-a-binary-search-tree/
Author: David Wang
Date: 11/3/2018
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        currentNode = root
        while currentNode != None:
            currentVal = currentNode.val

            if val < currentVal:
                if currentNode.left == None:
                    currentNode.left = TreeNode(val)
                    return root
                currentNode = currentNode.left

            else:
                if currentNode.right == None:
                    currentNode.right = TreeNode(val)
                    return root
                currentNode = currentNode.right

    def insertIntoBSTRecur(self, root, val):
        if not root:
            root = TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        return root

    def printTree(self, node):
        if node == None:
            return
        self.printTree(node.left)
        print('Node: {} Val: {} Right: {}, Left: {}'.format(
                node, node.val, node.left, node.right))
        self.printTree(node.right)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(4)
    two = TreeNode(2)
    seven = TreeNode(7)
    root.right = seven
    root.left = two

    print('Before')
    s.printTree(root)
    s.insertIntoBST(root, 5)
    print('After')
    s.printTree(root)

    li = [4,2,7,1,3]

