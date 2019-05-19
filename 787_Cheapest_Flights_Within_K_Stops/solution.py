"""
Problem: 787. Cheapest Flights Within K Stops
Url: https://leetcode.com/problems/cheapest-flights-within-k-stops/
Author: David Wang
Date: 05/18/2019
"""

import sys

class Node(object):
    def __init__(self, city, cost, stops):
        self.city = city
        self.cost = cost
        self.stops = stops


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        dists = self.initialize_dists(n)
        graph = self.create_graph(n, flights)
        return self.cheapest_flight(graph, dists, src, dst, K)

    def initialize_dists(self, n):
        return {i: sys.maxint for i in range(n)}

    def create_graph(self, n, flights):
        graph = {i: {} for i in range(n)}

        for f in flights:
            src = f[0]
            dest = f[1]
            cost = f[2]
            graph[src][dest] = cost

        return graph

    def cheapest_flight(self, graph, dists, src, dst, K):
        queue = [Node(src, 0, 0)]

        while queue:
            node = queue.pop(0)
            city = node.city
            node_cost = node.cost

            if node.stops >= K + 1:
                break

            for neigh, cost in graph[city].items():
                new_cost = node_cost + cost
                new_stops = node.stops + 1

                if dists[neigh] > new_cost and new_stops <= K + 1:
                    queue.append(Node(neigh, new_cost, new_stops))
                    dists[neigh] = new_cost

        if dists[dst] == sys.maxint:
            return -1

        return dists[dst]

if __name__ == '__main__':
    n, src, dst, k = 3, 0, 2, 0
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    print(Solution().findCheapestPrice(n, flights, src, dst, k))

    n, src, dst, k = 5, 2, 1, 1
    flights = [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
    print(Solution().findCheapestPrice(n, flights, src, dst, k))

    n, src, dst, k = 10, 6, 0, 7
    flights = [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
    print(Solution().findCheapestPrice(n, flights, src, dst, k))

    n, src, dst, k = 15, 1, 4, 10
    flights = [[10,14,43],[1,12,62],[4,2,62],[14,10,49],[9,5,29],[13,7,53],[4,12,90],[14,9,38],[11,2,64],[2,13,92],[11,5,42],[10,1,89],[14,0,32],[9,4,81],[3,6,97],[7,13,35],[11,9,63],[5,7,82],[13,6,57],[4,5,100],[2,9,34],[11,13,1],[14,8,1],[12,10,42],[2,4,41],[0,6,55],[5,12,1],[13,3,67],[3,13,36],[3,12,73],[7,5,72],[5,6,100],[7,6,52],[4,7,43],[6,3,67],[3,1,66],[8,12,30],[8,3,42],[9,3,57],[12,6,31],[2,7,10],[14,4,91],[2,3,29],[8,9,29],[2,11,65],[3,8,49],[6,14,22],[4,6,38],[13,0,78],[1,10,97],[8,14,40],[7,9,3],[14,6,4],[4,8,75],[1,6,56]]
    print(Solution().findCheapestPrice(n, flights, src, dst, k))
