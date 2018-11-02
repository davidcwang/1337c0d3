"""
Problem: 921 Minimum Add to Make Parentheses Valid 
Url: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/ 
Author: David Wang
Date: 10/23/2018
"""

class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        left_count = 0
        right_count = 0
        for i, p in enumerate(S):
            if p == '(':
                left_count += 1
            elif p == ')':
                if left_count <= 0:
                    right_count += 1
                else:
                    left_count -= 1
                    
        return abs(left_count) + right_count
