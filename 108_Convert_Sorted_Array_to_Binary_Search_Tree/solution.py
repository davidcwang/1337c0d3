"""
Problem: 108. Convert Sorted Array to Binary Search Tree
Url: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
Author: David Wang
Date: 06/27/2019
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def createBST(nums, start, end):
            if start >= end:
                return None

            mid = (start + end) / 2

            parent = TreeNode(nums[mid])
            parent.left = createBST(nums, start, mid)
            parent.right = createBST(nums, mid+1, end)

            return parent

        return createBST(nums, 0, len(nums))
