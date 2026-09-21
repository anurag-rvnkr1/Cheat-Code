'''
207. Course Schedule

There are a total of numCourses courses you have to take, labeled from
0 to numCourses - 1.

You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.

Return True if you can finish all courses. Otherwise, return False.

Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: True

Explanation:
    There are 2 courses to take.
    To take course 1 you should have finished course 0.

Example 2:
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: False

Explanation:
    There is a cycle between courses 0 and 1.

Constraints:
    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All prerequisite pairs are unique.
'''

# Topological Sort (Kahn's Algorithm)

from typing import List
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Build graph and indegree array.
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        # Start with courses having no prerequisites.
        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        completed_courses = 0

        while queue:
            current = queue.popleft()
            completed_courses += 1

            for neighbor in graph[current]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return completed_courses == numCourses


# Example usage
solution = Solution()

# Example 1
numCourses1 = 2
prerequisites1 = [[1, 0]]
print(solution.canFinish(numCourses1, prerequisites1))  # Output: True

# Example 2
numCourses2 = 2
prerequisites2 = [[1, 0], [0, 1]]
print(solution.canFinish(numCourses2, prerequisites2))  # Output: False

# Example 3
numCourses3 = 4
prerequisites3 = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(solution.canFinish(numCourses3, prerequisites3))  # Output: True

# Example 4
numCourses4 = 3
prerequisites4 = [[1, 0], [2, 1], [0, 2]]
print(solution.canFinish(numCourses4, prerequisites4))  # Output: False
