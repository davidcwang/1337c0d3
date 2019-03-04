"""
Problem: 841. Keys and Rooms 
Url: https://leetcode.com/problems/keys-and-rooms/ 
Author: David Wang
Date: 03/04/2019
"""

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        return self.canVisitRecur(rooms)

    def canVisitIter(self, rooms):
        # visited array with visited=True and not-visited=False
        # queue of rooms able to visit, only add not already in queue
        # if visited is all True then all visited
        visited = [False] * len(rooms)
        visited[0] = True
        queue = []
        queue.append(0)
        while len(queue):
            i = queue.pop(0)
            for k in rooms[i]:
                if not visited[k]:
                    visited[k] = True
                    queue.append(k)

        return all(visited)

    def canVisitRecur(self, rooms):
        visited = [False] * len(rooms)
        visited[0] = True
        self.visitRoom(rooms, rooms[0], visited)
        return all(visited)

    def visitRoom(self, rooms, keys, visited):
        # visited array with visited=True and not-visited=False
        # for each key:
        # set the room for that key as visited
        # visit the room if haven't been visited before
        # if all visited return True
        for k in keys:
            if not visited[k]:
                visited[k] = True
                self.visitRoom(rooms, rooms[k], visited)

if __name__ == '__main__':
    # Example 1
    rooms = [[1],[2],[3],[]] 
    print(Solution().canVisitAllRooms(rooms))

    # Example 1
    rooms = [[1,3],[3,0,1],[2],[0]] 
    print(Solution().canVisitAllRooms(rooms))
