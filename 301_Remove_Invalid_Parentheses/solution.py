"""
Problem: 301. Remove Invalid Parentheses
Url: https://leetcode.com/problems/remove-invalid-parentheses/
Author: David Wang
Date: 05/27/2020
"""

from typing import List


class Solution:
    def __init__(self):
        self.longest = 0

    def removeInvalidParentheses(self, s: str) -> List[str]:
        valid_list = []
        seen = set()

        if self._isValid(s):
            self.longest = len(s)
            seen.add(s)
            valid_list.append(s)

        self._removeInvalidRecurse(valid_list, seen, list(s))

        return self._remove_non_longest(valid_list)


    def _removeInvalidRecurse(self, valid_list, seen, s):

        for i in range(len(s)-1, -1, -1):
            current = s[:]
            current.pop(i)
            current_str = ''.join(current)

            if (self._isValid(current_str) and len(current_str) >= self.longest
                    and current_str not in seen):
                self.longest = len(current_str)
                seen.add(current_str)
                valid_list.append(current_str)

            if len(current_str) >= self.longest or not self._more_close_parens(current_str):
                self._removeInvalidRecurse(valid_list, seen, list(current_str))


    def _remove_non_longest(self, valid_list):
        only_longes_list = []

        for valid in valid_list:
            if len(valid) >= self.longest:
                only_longes_list.append(valid)

        return only_longes_list

    def _isValid(self, s):
        count = 0
        for c in s:

            if c == ')':
                if count == 0:
                    return False
                count -= 1

            elif c == '(':
                count += 1

        return count == 0

    def _more_close_parens(self, s):
        count = 0
        for c in s:

            if c == ')':
                if count == 0:
                    return True
                count -= 1

            elif c == '(':
                count += 1

        return False


if __name__ == '__main__':
    s = "()())()"
    output = Solution().removeInvalidParentheses(s)
    assert output == ["()()()", "(())()"]

    s = "(a)())()"
    output = Solution().removeInvalidParentheses(s)
    assert output == ["(a)()()", "(a())()"]

    s = ")("
    output = Solution().removeInvalidParentheses(s)
    assert output == [""]

    s = ")(f"
    output = Solution().removeInvalidParentheses(s)
    assert output == ["f"]

    s = "())))()v(k"
    output = Solution().removeInvalidParentheses(s)
    print(output)
    assert output == ["()()vk"]

    s = "()(((((((()"
    output = Solution().removeInvalidParentheses(s)
    print(output)
    assert output == ["()()"]
