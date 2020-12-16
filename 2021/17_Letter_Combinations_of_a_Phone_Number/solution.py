"""
Problem: 17. Letter Combinations of a Phone Number
Url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Author: David Wang
Date: 12/16/2020
"""

from typing import List


digit2let = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}

class Solution:

    def letterCombinations(self, digits: str) -> List[str]:

        def backtrack(comb, digits, index):
            if index >= len(digits):
                combs.append(comb)
                return

            d = digits[index]

            for let in (digit2let[d]):

                backtrack(comb + let, digits, index+1)

        combs = []
        if digits:
            backtrack('', digits, 0)
        return combs


if __name__ == '__main__':
    # digits = "23"
    # answer = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    # output = Solution().letterCombinations(digits)
    # print(answer)
    # print(output)
    # assert(answer == output)

    digits = ""
    answer = []
    output = Solution().letterCombinations(digits)
    print(answer)
    print(output)
    assert(answer == output)

    # digits = "2"
    # answer = ['a','b','c']
    # output = Solution().letterCombinations(digits)
    # print(answer)
    # print(output)
    # assert(answer == output)


