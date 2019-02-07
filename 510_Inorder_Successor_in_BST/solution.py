"""
Problem: 510 Inorder Successor in BST 
Url: https://leetcode.com/problems/inorder-successor-in-bst-ii
Author: David Wang
Date: 02/06/2019
"""

class Solution(object):
    def inorder_succ(self, cur, x):
        successor = Node()
        left = Node()
        right = Node()

        while cur.val != x and cur.val != None:
            val = cur.val
            left = cur.left
            right = cur.right

            if x < val:
                successor = cur
                cur = left
            else:
                cur = right

        if x == val:
            if right:
                successor = right
                while successor.left:
                    successor == successor.left
        return successor.val


class Node(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == '__main__':
    s = Solution()

     #   2
     #  /
     # 1
    root1 = Node(2, Node(1))
    print(s.inorder_succ(root1, 1))

    #    2
    #   / \
    #  1   3
    root2 = Node(2, Node(1), Node(3))
    print(s.inorder_succ(root2, 1))

    #    2
    #   / \
    #  1   3
    #       \
    #        4
    root3 = Node(2, Node(1), Node(3, None, Node(4)))
    print(s.inorder_succ(root3, 2))

