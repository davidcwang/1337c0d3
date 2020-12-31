"""
Problem: 56. Merge Intervals
Url: https://leetcode.com/problems/merge-intervals/
Author: David Wang
Date: 12/30/2020
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        results = []

        intervals = sorted(intervals)
        results.append(intervals.pop(0))

        while intervals:
            n_start, n_end = intervals.pop(0)

            start, end = results[-1]

            if n_start > end:
                results.append([n_start, n_end])
                continue

            else:
                results[-1][1] = max(end, n_end)

        return results


if __name__ == '__main__':
    input = [[1,3],[2,6],[8,10],[15,18]]
    answer = [[1,6],[8,10],[15,18]]
    output = Solution().merge(input)
    assert(answer == output)

    input = [[1,4],[4,5]]
    answer = [[1,5]]
    output = Solution().merge(input)
    assert(answer == output)
