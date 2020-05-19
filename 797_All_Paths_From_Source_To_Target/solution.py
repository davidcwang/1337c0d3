import copy
"""
Problem: 797. All Paths From Source to Target
Url: https://leetcode.com/problems/all-paths-from-source-to-target/ 
Author: David Wang
Date: 11/1/2018
"""

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        path_list = []
        src = 0
        currentPath = [src]
        dest = len(graph) - 1
        self.traverseGraph(path_list, graph, src, dest, currentPath)
        return path_list

    def traverseGraph(self, path_list, graph, i, dest, currentPathList):
        if graph[i] == None:
            return
        for neighbor in graph[i]:
            newPath = copy.deepcopy(currentPathList)
            path = newPath.append(neighbor)
            if dest == neighbor:
                path_list.append(newPath)
                continue
            self.traverseGraph(path_list, graph, neighbor, dest, newPath)

if __name__ == '__main__':
    graph = [[1,2], [3], [3], []]
    s = Solution()
    path_list = s.allPathsSourceTarget(graph)
    print(path_list)
