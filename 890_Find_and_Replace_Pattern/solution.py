"""
Problem: 890. Find and Replace Pattern
Url: https://leetcode.com/problems/find-and-replace-pattern/
Author: David Wang
Date: 10/29/2018
"""

class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        matches = []
        for word in words:
            if self.is_match(word, pattern):
                matches.append(word)
        return matches

    def is_match(self, word, pattern):
        p2w = {}
        w2p = {}
        for w, p in zip(word, pattern):
            if p not in p2w: p2w[p] = w
            if w not in w2p: w2p[w] = p
            if p2w[p] != w or w2p[w] != p:
                return False

        return True

if __name__ == '__main__':
    words = ["abc","deq","mee","aqq","dkd","ccc"]
    pattern = 'abb'
    s = Solution()
    print(s.findAndReplacePattern(words, pattern))
