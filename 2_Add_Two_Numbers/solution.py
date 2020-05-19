"""
Problem: 2. Add Two Numbers
Url: https://leetcode.com/problems/add-two-numbers/description/
Author: David Wang
Date: 12/26/2017

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a 
single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, 
except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        self.start_node = None

    def __add_node(self, value, prev_node):
            value = value % 10
            node = ListNode(value)
            if prev_node == None:
                self.start_node = node
            else:
                prev_node.next = node
            return node

    def addTwoNumbers(self, l1, l2):
        """
        Returns a linked linked list that is the sum of the other two linked
        lists.

        Args:
            l1: The first linked list.
            l2: The second linked list.
        Returns:
            A linked list that contains the sum of the other two linked lists.
        """
        carry_over = 0
        prev_node = None
        l1_current = l1
        l2_current = l2
        while l1_current != None and l2_current != None:
            value = l1_current.val + l2_current.val + (1 if carry_over else 0)
            carry_over = value / 10

            node = self.__add_node(value, prev_node)
            prev_node = node
            l1_current = l1_current.next
            l2_current = l2_current.next
    
        while l1_current != None:
            value = l1_current.val + (1 if carry_over else 0)
            node = self.__add_node(value, prev_node)
            prev_node = node
            carry_over = value / 10
            l1_current = l1_current.next
        while l2_current != None:
            value = l2_current.val + (1 if carry_over else 0)
            node = self.__add_node(value, prev_node)
            prev_node = node
            carry_over = value / 10
            l2_current = l2_current.next

        # add extra node at end if 
        if carry_over == True:
            node = self.__add_node(1, prev_node)
            node.next = None # since last node

        return self.start_node
