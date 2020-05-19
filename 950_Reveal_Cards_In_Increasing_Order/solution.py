"""
Problem: 950. Reveal Cards In Increasing Order
Url: https://leetcode.com/problems/reveal-cards-in-increasing-order/
Author: David Wang
Date: 01/02/2019
"""

class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        indices = list(range(len(deck)))
        skip_deck = [None] * len(deck)

        for card in sorted(deck):
            skip_deck[indices.pop(0)] = card
            if indices:
                indices.append(indices.pop(0))

        return skip_deck

if __name__ == '__main__':
    deck = [17,13,11,2,3,5,7]
    s = Solution()
    print(s.deckRevealedIncreasing(deck))
