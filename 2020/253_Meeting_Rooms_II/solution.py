"""
Problem: 253. Meeting Rooms II
Url: https://leetcode.com/problems/meeting-rooms-ii/
Author: David Wang
Date: 05/27/2020
"""


import heapq
from typing import List



class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        sorted_intervals = sorted(intervals)

        if len(intervals) == 0:
            return 0

        heapq.heappush(rooms, sorted_intervals[0][1])

        for inter in sorted_intervals[1:]:
            if inter[0] >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, inter[1])

        return len(rooms)


if __name__ == '__main__':
    input = []
    output = Solution().minMeetingRooms(input)
    assert output == 0

    input = [[1,2]]
    output = Solution().minMeetingRooms(input)
    assert output == 1

    input = [[1,2], [2,3]]
    output = Solution().minMeetingRooms(input)
    assert output == 1

    input = [[1,2], [1,3]]
    output = Solution().minMeetingRooms(input)
    assert output == 2

    input = [[0, 30],[5, 10],[15, 20]]
    output = Solution().minMeetingRooms(input)
    assert output == 2

    input = [[7,10],[2,4]]
    output = Solution().minMeetingRooms(input)
    assert output == 1
