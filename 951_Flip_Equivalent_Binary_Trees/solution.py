"""
Problem: 951. Flip Equivalent Binary Trees
Url: https://leetcode.com/problems/flip-equivalent-binary-trees/ 
Author: David Wang
Date: 12/28/2018
"""

class Solution:
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 is None or root2 is None:
            return root1 is root2
        elif root1.val != root2.val:
            return False
        else:
            return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right,
                root2.right) or self.flipEquiv(root1.left, root2.right) and 
                self.flipEquiv(root1.right, root2.left))
