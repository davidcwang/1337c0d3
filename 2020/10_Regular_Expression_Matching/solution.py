"""
Problem: 10. Regular Expression Matching
Url: https://leetcode.com/problems/regular-expression-matching/
Author: David Wang
Date: 06/12/2020
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        regex = ''
        all = False
        for i in range(p):
            regex = p[i]
