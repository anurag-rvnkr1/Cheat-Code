'''
210. Course Schedule II

There are a total of numCourses courses you have to take, labeled from
0 to numCourses - 1.

You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.

Return the ordering of courses you should take to finish all courses.
If there are multiple valid answers, return any of them.
If it is impossible to finish all courses, return an empty list.

Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: [0,1]

Explanation:
    There are 2 courses.
    To take course 1, you must first take course 0.

Example 2:
    Input: numCourses = 4,
           prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,2,1,3]

Explanation:
    One valid course order is [0,2,1,3].
    Another valid order is [0,1,2,3].

Example 3:
    Input: numCourses = 1, prerequisites = []
    Output: [0]

Constraints:
    1 <= numCourses <= 2000
    0 <= prerequisites.length <= numCourses * (numCourses - 1)
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All prerequisite pairs are distinct.
'''

# Topological Sort (Kahn's Algorithm)

from typing import List
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Build graph and indegree array.
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        # Add all courses with no prerequisites.
        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        order = []

        while queue:
            current = queue.popleft()
            order.append(current)

            for neighbor in graph[current]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == numCourses else []


# Example usage
solution = Solution()

# Example 1
numCourses1 = 2
prerequisites1 = [[1, 0]]
print(solution.findOrder(numCourses1, prerequisites1))
# Output: [0, 1]

# Example 2
numCourses2 = 4
prerequisites2 = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(solution.findOrder(numCourses2, prerequisites2))
# Output: [0, 2, 1, 3] (or [0, 1, 2, 3])

# Example 3
numCourses3 = 1
prerequisites3 = []
print(solution.findOrder(numCourses3, prerequisites3))
# Output: [0]

# Example 4
numCourses4 = 2
prerequisites4 = [[1, 0], [0, 1]]
print(solution.findOrder(numCourses4, prerequisites4))
# Output: []
