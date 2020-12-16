"""
Problem: 759. Employee Free Time
Url: https://leetcode.com/problems/employee-free-time/
Author: David Wang
Date: 05/25/2020
"""

# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: [[Interval]]) -> [Interval]:
        free_times = []
        sorted_schedule = self._sort_schedule(schedule)

        start = -float('inf')
        end = -float('inf')

        for interval in sorted_schedule:
            s = interval.start
            e = interval.end

            if s > end:
                free_times.append(Interval(end, s))

            start = max(start, s)
            end = max(end, e)


        return self._remove_unbounded_intervals(free_times)

    def _sort_schedule(self, schedule):
        sorted_schedule = []

        while len(schedule):
            s = schedule.pop(0)
            for interval in s:
                sorted_schedule.append(interval)

        return sorted(sorted_schedule, key=lambda i: i.start)

    def _remove_unbounded_intervals(self, intervals):
        if len(intervals) == 0:
            return intervals

        elif intervals[0].start == -float('inf'):
            intervals.pop(0)

        return intervals

    def create_schedule(self, input):
        schedule = []
        while len(input) > 0:
            employee_schedule = []
            interval = input.pop(0)

            for i in interval:
                employee_schedule.append(Interval(i[0], i[1]))

            schedule.append(employee_schedule)

        return schedule

    def interval_to_list(self, intervals):
        interval_list = []
        while len(intervals) > 0:
            inter = intervals.pop(0)
            interval_list.append([inter.start, inter.end])

        return interval_list


if __name__ == '__main__':
    input = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
    schedule = Solution().create_schedule(input)
    intervals = Solution().employeeFreeTime(schedule)
    print(Solution().interval_to_list(intervals))

    input =  [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
    schedule = Solution().create_schedule(input)
    intervals = Solution().employeeFreeTime(schedule)
    print(Solution().interval_to_list(intervals))
