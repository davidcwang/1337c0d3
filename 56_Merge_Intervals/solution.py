"""
Problem: 56. Merge Intervals
Url: https://leetcode.com/problems/merge-intervals/
Author: David Wang
Date: 05/26/2020
"""


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals = []
        sorted_intervals = sorted(intervals)

        for interval in sorted_intervals:

            if len(merged_intervals) == 0:
                merged_intervals.append(interval)

            start, end = interval
            prev_start, prev_end = merged_intervals[-1]

            # No overlap so append new interval.
            if start > prev_end:
                merged_intervals.append([start, end])

            # There is overlap in the intervals so merge them.
            else:
                max_end = max(prev_end, end)
                merged_intervals.pop()
                merged_intervals.append([prev_start, max_end])

        return merged_intervals


if __name__ == '__main__':
    input = [[1,3],[2,6],[8,10],[15,18]]
    print(Solution().merge(input))
