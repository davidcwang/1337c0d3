"""
Problem: 3. Longest Substring Without Repeating Characters
Url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Author: David Wang
Date: 12/27/2017

Given a string, find the length of the longest substring 
without repeating characters.

Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3.
    Note that the answer must be a substring, "pwke" is a subsequence
    and not a substring.
"""

class Solution(object):
        def lengthOfLongestSubstring(self, s):
            """
            Returns the length of the longest substring in the given string.

            Args:
                s: A given string
            Returns:
                An int representing the length of the longest substring.
            """
            longest = 0
            i = 0
            j = 0
            n = len(s)
            seen = {}
            while i < n and j < n:
                c = s[j]
                if c in seen:
                    i = seen[c] + 1
                seen[c] = j
                j += 1
                longest = max(longest, j-i)

            return longest

