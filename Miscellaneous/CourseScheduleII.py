## https://leetcode.com/problems/course-schedule-ii/description/

from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = self.makegraph(numCourses, prerequisites)

        if len(prerequisites) == 0:
            return [x for x in range(numCourses)]

        return self.toposort(graph)

    def toposort(self, graph):
        res, found = [], [0] * len(graph)
        stack = list(range(len(graph)))
        while stack:
            node = stack.pop()
            if node < 0:
                res.append(~node)
            elif not found[node]:
                found[node] = 1
                stack.append(~node)
                stack += graph[node]

        # cycle check
        for node in res:
            if any(found[nei] for nei in graph[node]):
                return None
            found[node] = 0

        return res[::-1]

    def makegraph(self, node_cnt, connectionList):
        graph = dict()
        for i in range(node_cnt):
            graph[i] = []
        for conn in connectionList:
            graph[conn[1]].append(conn[0])
            if conn[0] not in graph:
                graph[conn[0]] = []
        return graph