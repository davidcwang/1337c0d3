"""
Problem: 986. Interval List Intersections 
Url: https://leetcode.com/problems/interval-list-intersections/ 
Author: David Wang
Date: 03/23/2019
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """
        # Case 1
        # |----|
        #        |---|
        #
        # Case 2
        # |----|
        #    |----|
        #
        # Case 3
        # |----|
        #   |-|

        i = 0
        j = 0
        inter = []
        while i < len(A) and j < len(B):
            startA = A[i].start
            startB = B[j].start

            endA = A[i].end
            endB = B[j].end
            
            if startA > endB: 
                j += 1
                continue
            elif startB > endA:
                i += 1
                continue
            elif startA >= startB and endA <= endB:
                inter.append(Interval(startA, endA))
                i += 1
            elif startB >= startA and endB <= endA:
                inter.append(Interval(startB, endB))
                j += 1
            elif startA <= startB and endA <= endB:
                inter.append(Interval(startB, endA))
                i += 1
            elif startB <= startA and endB <= endA:
                inter.append(Interval(startA, endB))
                j += 1

        return inter

if __name__ == '__main__':
    s = Solution()
    A = [[0,2],[5,10],[13,23],[24,25]]
    B = [[1,5],[8,12],[15,24],[25,26]]
    print(s.intervalIntersection(A, B))
