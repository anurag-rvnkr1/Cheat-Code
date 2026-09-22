'''
317. Shortest Distance from All Buildings

You are given an m x n grid where:

    0 -> Empty land.
    1 -> Building.
    2 -> Obstacle.

Build a house on an empty land such that the total travel distance to all
buildings is minimized.

Return the minimum total distance. If it is impossible to reach all buildings,
return -1.

Travel distance is the Manhattan distance (4 directions).

Example 1:
    Input:
        grid = [
            [1,0,2,0,1],
            [0,0,0,0,0],
            [0,0,1,0,0]
        ]

    Output:
        7

Explanation:
    The house is built at (1,2).

    Distance to buildings:
        (0,0) -> 3
        (0,4) -> 3
        (2,2) -> 1

    Total = 7

Example 2:
    Input:
        grid = [[1,0]]

    Output:
        1

Example 3:
    Input:
        grid = [[1]]

    Output:
        -1

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    grid[i][j] is 0, 1, or 2.
'''
# Multi-Source BFS + Grid Traversal

from typing import List
from collections import deque


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # Total distance accumulated for every empty cell.
        distance_sum = [
            [0] * cols
            for _ in range(rows)
        ]

        # Number of buildings that reached each empty cell.
        reach_count = [
            [0] * cols
            for _ in range(rows)
        ]

        total_buildings = 0

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        # BFS from every building.
        for row in range(rows):
            for col in range(cols):

                if grid[row][col] != 1:
                    continue

                total_buildings += 1

                visited = [
                    [False] * cols
                    for _ in range(rows)
                ]

                queue = deque([(row, col, 0)])
                visited[row][col] = True

                while queue:
                    current_row, current_col, dist = queue.popleft()

                    for dr, dc in directions:
                        new_row = current_row + dr
                        new_col = current_col + dc

                        if (
                            0 <= new_row < rows and
                            0 <= new_col < cols and
                            not visited[new_row][new_col] and
                            grid[new_row][new_col] == 0
                        ):
                            visited[new_row][new_col] = True

                            distance_sum[new_row][new_col] += dist + 1
                            reach_count[new_row][new_col] += 1

                            queue.append(
                                (new_row, new_col, dist + 1)
                            )

        answer = float("inf")

        for row in range(rows):
            for col in range(cols):

                if (
                    grid[row][col] == 0 and
                    reach_count[row][col] == total_buildings
                ):
                    answer = min(answer, distance_sum[row][col])

        return answer if answer != float("inf") else -1


# Example usage
solution = Solution()

# Example 1
grid1 = [
    [1,0,2,0,1],
    [0,0,0,0,0],
    [0,0,1,0,0]
]

print(solution.shortestDistance(grid1))
# Output: 7

# Example 2
grid2 = [
    [1,0]
]

print(solution.shortestDistance(grid2))
# Output: 1

# Example 3
grid3 = [
    [1]
]

print(solution.shortestDistance(grid3))
# Output: -1

# Example 4
grid4 = [
    [1,2,0],
    [0,2,1],
    [0,0,0]
]

print(solution.shortestDistance(grid4))
# Output: 4

# Example 5
grid5 = [
    [1,0,0],
    [2,2,0],
    [1,0,0]
]

print(solution.shortestDistance(grid5))
# Output: 4
