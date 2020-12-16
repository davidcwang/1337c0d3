"""
Problem: 20. Valid Parentheses
Url: https://leetcode.com/problems/valid-parentheses/
Author: David Wang
Date: 05/26/2020
"""


class Solution:
    def isValid(self, s: str) -> bool:
        open_stack = []
        for c in s:
            if c in '({[':
                open_stack.append(c)

            # else we know we have a closing character.
            else:

                if len(open_stack) == 0:
                    return False

                open = open_stack.pop()

                if ((c == ')' and open != '(')
                        or (c == '}' and open != '{')
                        or (c == ']' and open != '[')):

                    return False

        if len(open_stack) == 0:
            return True

        return False


if __name__ == '__main__':
    input = "()"
    assert Solution().isValid(input) == True

    input = "()[]{}"
    assert Solution().isValid(input) == True

    input = "(]"
    assert Solution().isValid(input) == False

    input = "([)]"
    assert Solution().isValid(input) == False

    input = "{[]}"
    assert Solution().isValid(input) == True

    input = "]"
    assert Solution().isValid(input) == False
