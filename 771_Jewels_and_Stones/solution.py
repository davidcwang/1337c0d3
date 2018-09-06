"""
Problem: 771. Jewels and Stones
Url: https://leetcode.com/problems/jewels-and-stones/description/  
Author: David Wang
Date: 9/3/2018
"""

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        """
        jewel_dict = set(J)
        num_jewels = 0
        for s in S:
            if s in jewel_dict:
                num_jewels += 1
        return num_jewels
