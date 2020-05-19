"""
Problem: 654. Maximum Binary Tree
Url: https://leetcode.com/problems/maximum-binary-tree/ 
Author: David Wang
Date: 10/23/2018
"""

import sys

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.createNode(0, len(nums), nums)

                
    def createNode(self, start, end, array):
        if start >= end:
            return None
        max_num = -sys.maxsize
        max_index = start
        for i in range(start, end):
            if array[i] > max_num:
                max_num = array[i]
                max_index = i
        
        node = TreeNode(max_num)
        leftNode = self.createNode(start, max_index, array)
        rightNode = self.createNode(max_index+1, end, array)
        node.left = leftNode
        node.right = rightNode
        return node
