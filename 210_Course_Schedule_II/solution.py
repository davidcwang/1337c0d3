"""
Problem: 210. Course Schedule II
Url: https://leetcode.com/problems/course-schedule-ii/
Author: David Wang
Date: 05/18/2019
"""

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph, indegrees = self.create_graph(numCourses, prerequisites)
        start_list = self.get_start_nodes(numCourses, prerequisites)
        return self.topological_sort(start_list, graph, indegrees)

    def create_graph(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        indegrees = {i: 0 for i in range(numCourses)}

        for edge in prerequisites:
            course, dep = edge
            graph[dep].append(course)
            indegrees[course] += 1

        return graph, indegrees

    def get_start_nodes(self, numCourses, prerequisites):
        start_list = []

        course_with_dep = set()
        for edge in prerequisites:
            course, dep = edge
            course_with_dep.add(course)

        for i in range(numCourses):
            if i not in course_with_dep:
                start_list.append(i)

        return start_list


    def topological_sort(self, start_list, graph, indegrees):
        return self.dfs_iter(start_list, graph, indegrees)

    def dfs_iter(self, start_list, graph, indegrees):
        stack = start_list
        ordering = []
        while stack:
            node = stack.pop()

            if indegrees[node] > 1:
                indegrees[node] -= 1
                continue

            ordering.append(node)
            stack.extend(graph[node])

        if len(ordering) < len(graph.keys()):
            return []

        return ordering

if __name__ == '__main__':
    numCourses1 = 2
    prerequisites1 = [[1,0]]
    print(Solution().findOrder(numCourses1, prerequisites1))

    numCourses2 = 4
    prerequisites2 = [[1,0],[2,0],[3,1],[3,2]]
    print(Solution().findOrder(numCourses2, prerequisites2))

    numCourses3 = 3
    prerequisites3 = [[1,0],[1,2],[0,1]]
    print(Solution().findOrder(numCourses3, prerequisites3))

