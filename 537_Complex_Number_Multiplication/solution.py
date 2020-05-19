"""
Problem: 537. Complex Number Multiplication 
Url: https://leetcode.com/problems/complex-number-multiplication/ 
Author: David Wang
Date: 01/01/2019
"""

class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num1, numi1 = a.split('+')
        num2, numi2 = b.split('+')

        num1 = int(num1)
        num2 = int(num2)
        numi1 = int(numi1.rstrip('i'))
        numi2 = int(numi2.rstrip('i'))

        final_num = num1 * num2 - (numi1 * numi2)
        final_numi = num1 * numi2 + num2 * numi1

        return "{}+{}i".format(final_num, final_numi)

if __name__ == '__main__':
    a = "1+-1i"
    b = "1+-1i" 
    s = Solution()
    print(s.complexNumberMultiply(a, b))
