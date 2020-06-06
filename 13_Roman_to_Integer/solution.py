"""
Problem: 13. Roman to Integer
Url: https://leetcode.com/problems/roman-to-integer/
Author: David Wang
Date: 06/03/2020
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        # I can be placed before V (5) and X (10) to make 4 and 9.
        # X can be placed before L (50) and C (100) to make 40 and 90.
        # C can be placed before D (500) and M (1000) to make 400 and 900.

        value = 0

        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        i = 0
        while i < len(s):
            c = s[i]

            if i < len(s) - 1:
                next_c = s[i+1]

                if ((c == 'I' and next_c == 'V')
                        or (c == 'I' and next_c == 'X')
                        or (c == 'X' and next_c == 'L')
                        or (c == 'X' and next_c == 'C')
                        or (c == 'C' and next_c == 'D')
                        or (c == 'C' and next_c == 'M')):

                    value -= mapping[c]
                    i += 1
                    continue

            value += mapping[c]
            i += 1

        return value


if __name__ == '__main__':
    input = 'III'
    output = Solution().romanToInt(input)
    assert output == 3

    input = 'MCMXCIV'
    output = Solution().romanToInt(input)
    assert output == 1994
