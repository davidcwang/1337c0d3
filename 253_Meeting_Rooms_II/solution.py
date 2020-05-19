class Solution(object):
    """
    We will use a greedy approach by sorting by the start interval.
    """
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        min_rooms = 0

        if not intervals or len(intervals) == 0:
            return min_rooms

        rooms = []
        sorted_intervals = sorted(intervals)

        while sorted_intervals:
            inter = sorted_intervals.pop(0)
            cur_start, cur_end = inter

            schedulable = False
            # Iterate over all the rooms to see if there is a free room.
            for r in rooms:
                # If the start time of the interval comes before the time that
                # the room is free, then there is a conflict.
                if cur_start >= r[-1][1]:
                    r.append(inter)
                    schedulable = True
                    break

            if not schedulable:
                 new_room = [inter]
                 rooms.append(new_room)
                 min_rooms += 1

        return min_rooms


if __name__ == '__main__':
    intervals = [[0, 30],[5, 10],[15, 20]]
    target = 2
    res = Solution().minMeetingRooms(intervals)
    assert res == target

    intervals =  [[7,10],[2,4]]
    target = 1
    res = Solution().minMeetingRooms(intervals)
    assert res == target

    """
    Case 1:
    intervals = [[0, 30],[5, 10],[15, 20]]
    
    min_rooms = 2
    rooms = [
        [[0, 30]],
        [[5, 10], [15,20]],
    ]
    
    
    Case 2:
    intervals = [[7,10],[2,4]]
    sorted_intervals = [[2,4],[7,10]] 
    min_rooms = 0
    rooms = [
        [[2,4], [7,10]],
    ]
    
    Case 3:
    intervals = []
    min_rooms = 0
    
    Case 4:
    intervals = [[0,5], [0,5]]
    min_rooms = 0
    rooms = [
        [[0,5]],
        [[0,5]],
    ]
    """