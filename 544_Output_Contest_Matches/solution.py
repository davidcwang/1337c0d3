import math

"""
Problem: 544. Output Contest Matches
Url: https://leetcode.com/articles/output-contest-matches/ 
Author: David Wang
Date: 9/10/2018
"""

class Solution(object):

    def findContestMatch(self, n):
        matches = [i+1 for i in range(n)]
        # Property of Logs: logb(a) = log(a)/log(b)
        print(self.matchIter(n, matches)[0])

    def findContestMatchRecur(self, n):
        matches = [i+1 for i in range(n)]
        # Property of Logs: logb(a) = log(a)/log(b)
        self.matchRecur(n, matches)
        print(matches[0])

    def matchIter(self, n, matches):
        for i in range(int(math.log(n, 2))):
            cur_match = []
            size = len(matches)
            for j in range(int(size/2)):
                cur_match.append('({},{})'.format(matches[j], matches[int(n/(i+1)) - 1 - j]))
            matches = cur_match
        return matches

    def matchRecur(self, n, matches):
        if n == 1:
            return
        for i in range(n):
            matches[i] = '({},{})'.format(matches[i], matches[n-1-i])

        self.matchRecur(int(n/2), matches)

if __name__ == '__main__':
    s = Solution()
    #s.findContestMatchRecur(8)
    s.findContestMatch(8)
