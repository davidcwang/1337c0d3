"""
Problem: 876. Middle of the Linked List
Url: https://leetcode.com/problems/middle-of-the-linked-list/
Author: David Wang
Date: 06/01/2019
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
