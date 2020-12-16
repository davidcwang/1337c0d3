"""
Problem: 17. Letter Combinations of a Phone Number
Url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Author: David Wang
Date: 06/09/2020
"""


from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        return self._get_combinations(digits, letter_map, [], [], 0)

    def _get_combinations(self, digits, letter_map, combinations, comb, index):
        for i in range(index, len(digits)):
            n = digits[i]

            for j, l in enumerate(letter_map[n]):
                comb.append(l)
                self._get_combinations(digits, letter_map, combinations, comb, i+1)

                if len(comb) == len(digits):
                    combinations.append(''.join(comb[:]))

                comb.pop()

        return combinations


if __name__ == '__main__':
    input = '23'
    output = Solution().letterCombinations(input)
    print(output)

