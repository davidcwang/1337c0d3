"""
Problem: 763. Partition Labels
Url: https://leetcode.com/problems/partition-labels/ 
Author: David Wang
Date: 11/15/2018
"""
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # index of last occurence of a particular letter
        ll_map = {l:  i for i, l in enumerate(S)}
        part = []
        last = 0
        length = 0
        for i, s in enumerate(S):
            last = max(last, ll_map[s])
            # only one occurence of the letter
            if i == last:
                part.append(i - length + 1)
                length = i + 1
        return part
