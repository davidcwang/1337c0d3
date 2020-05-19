"""
Problem: 973. K Closest Points to Origin 
Url: https://leetcode.com/problems/k-closest-points-to-origin/ 
Author: David Wang
Date: 03/23/2019
"""


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        distances = [(i, p, self.dist(p)) for i, p in enumerate(points)]
        sorted_dist = sorted(distances, key=lambda x: x[2])[:K]
        return list(map(lambda x: x[1], sorted_dist))

    def dist(self, p):
        # get the euclidian distance to the origin
        return ((p[0])**2 + (p[1])**2)**0.5

if __name__ == '__main__':
    s = Solution()
    print(s.kClosest([[1,3],[-2,2]], 1))
    print(s.kClosest([[3,3],[5,-1],[-2,4]], 2))
