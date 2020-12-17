"""
Problem: 22. Generate Parentheses
Url: https://leetcode.com/problems/generate-parentheses/
Author: David Wang
Date: 12/16/2020
"""

from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(parens, n, num_open, num_close):
            if num_open == n and num_close == n:
                parens_list.append(parens)
                return

            if num_open < n:
                backtrack(parens + '(', n, num_open+1, num_close)

            if num_close < n and num_open > num_close:
                backtrack(parens + ')', n, num_open, num_close+1)

            return parens_list


        parens_list = []
        return backtrack('', n, 0, 0)

if __name__ == '__main__':
    n = 3
    answer = ["((()))","(()())","(())()","()(())","()()()"]
    output = Solution().generateParenthesis(n)
    print(answer)
    print(output)
    assert(answer == output)

    n = 1
    answer = ["()"]
    output = Solution().generateParenthesis(n)
    print(answer)
    print(output)
    assert(answer == output)
