"""
Problem: 155. Min Stack
Url: https://leetcode.com/problems/min-stack/
Author: David Wang
Date: 06/01/2019
"""
import sys

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.stack:
            cur_min = self.stack[-1][1]
            self.stack.append((x, min(cur_min, x)))
        else:
            self.stack.append((x, x))


    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]



    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
