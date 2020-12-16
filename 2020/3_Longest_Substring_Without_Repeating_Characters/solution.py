"""
Problem: 3. Longest Substring Without Repeating Characters
Url: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Author: David Wang
Date: 06/04/2020
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # char_dict = {}
        # max_length: int = 0
        # cur_str = []
        #
        # for i, c in enumerate(s):
        #     if c not in char_dict:
        #         char_dict[c] = 0
        #
        #     while char_dict[c] > 0:
        #         pop_c = cur_str.pop(0)
        #         char_dict[pop_c] -= 1
        #
        #     cur_str.append(c)
        #     char_dict[c] += 1
        #     max_length = max(len(cur_str), max_length)
        #
        # return max_length

        index_dict = {}
        max_length: int = 0
        cur_start = 0

        for i, c in enumerate(s):
            if c in index_dict:
                cur_start = max(index_dict[c] + 1, cur_start)

            index_dict[c] = i
            max_length = max(i - cur_start + 1, max_length)

        return max_length

if __name__ == '__main__':
    input = ''
    output = Solution().lengthOfLongestSubstring(input)
    assert output == 0

    input = 'a'
    output = Solution().lengthOfLongestSubstring(input)
    assert output == 1

    input = 'aaaa'
    output = Solution().lengthOfLongestSubstring(input)
    assert output == 1

    input = 'abc'
    output = Solution().lengthOfLongestSubstring(input)
    assert output == 3

    input = "abcabcbb"
    output = Solution().lengthOfLongestSubstring(input)
    assert output == 3

    input = "pwwkew"
    output = Solution().lengthOfLongestSubstring(input)
    assert output == 3
