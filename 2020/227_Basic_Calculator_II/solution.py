"""
Problem: 227. Basic Calculator II
Url: https://leetcode.com/problems/basic-calculator-ii/
Author: David Wang
Date: 05/29/2020
"""

class Solution:
    def calculate(self, s: str) -> int:
        return self.eval_recurse(s)

    def _eval_recurse(self, expression):
        expr_list = expression.split('*')
        expr_list = expression.split('/')
        expr_list = expression.split('+')
        expr_list = expression.split('-')


    def _split_by_operand(self, expr_str, operand_list):
        split_start = 0
        split_end = 0

        while split_end < len(expr_str):
            if expr_str[split_end] in operand_list:

