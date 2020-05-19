"""
Problem: 3. Longest Substring Without Repeating Characters
Url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Author: David Wang
Date: 07/05/2017
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeat_dict = {}
        start = 0
        end = 0
        max_len = 0

        for i, c in enumerate(s):

            if c in repeat_dict:
                start = max(start, repeat_dict[c] + 1)

            repeat_dict[c] = i
            end = i
            length = (end - start + 1)
            max_len = max(length, max_len)

        return max_len
