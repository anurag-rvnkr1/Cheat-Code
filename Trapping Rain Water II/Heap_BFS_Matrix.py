'''
407. Trapping Rain Water II

Given an m x n integer matrix heightMap representing the height of each unit cell
in a 2D elevation map, return the volume of water it can trap after raining.

Example 1:
    Input:
        heightMap = [
            [1,4,3,1,3,2],
            [3,2,1,3,2,4],
            [2,3,3,2,3,1]
        ]

    Output:
        4

Example 2:
    Input:
        heightMap = [
            [3,3,3,3,3],
            [3,2,2,2,3],
            [3,2,1,2,3],
            [3,2,2,2,3],
            [3,3,3,3,3]
        ]

    Output:
        10

Constraints:
    m == heightMap.length
    n == heightMap[i].length
    1 <= m, n <= 200
    0 <= heightMap[i][j] <= 2 * 10^4
'''

# Min Heap + BFS (Dijkstra-like Flood Fill)

from typing import List
import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        rows = len(heightMap)
        cols = len(heightMap[0])

        if rows < 3 or cols < 3:
            return 0

        visited = [[False] * cols for _ in range(rows)]
        min_heap = []

        # Add all boundary cells.
        for row in range(rows):
            heapq.heappush(min_heap, (heightMap[row][0], row, 0))
            heapq.heappush(min_heap, (heightMap[row][cols - 1], row, cols - 1))
            visited[row][0] = True
            visited[row][cols - 1] = True

        for col in range(1, cols - 1):
            heapq.heappush(min_heap, (heightMap[0][col], 0, col))
            heapq.heappush(min_heap, (heightMap[rows - 1][col], rows - 1, col))
            visited[0][col] = True
            visited[rows - 1][col] = True

        water = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while min_heap:
            height, row, col = heapq.heappop(min_heap)

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    not visited[nr][nc]
                ):
                    visited[nr][nc] = True

                    water += max(0, height - heightMap[nr][nc])

                    heapq.heappush(
                        min_heap,
                        (
                            max(height, heightMap[nr][nc]),
                            nr,
                            nc
                        )
                    )

        return water


# Example usage
solution = Solution()

# Example 1
heightMap1 = [
    [1,4,3,1,3,2],
    [3,2,1,3,2,4],
    [2,3,3,2,3,1]
]
print(solution.trapRainWater(heightMap1))
# Output: 4

# Example 2
heightMap2 = [
    [3,3,3,3,3],
    [3,2,2,2,3],
    [3,2,1,2,3],
    [3,2,2,2,3],
    [3,3,3,3,3]
]
print(solution.trapRainWater(heightMap2))
# Output: 10

# Example 3
heightMap3 = [
    [5,5,5],
    [5,1,5],
    [5,5,5]
]
print(solution.trapRainWater(heightMap3))
# Output: 4

# Example 4
heightMap4 = [
    [1,1,1,1],
    [1,0,0,1],
    [1,1,1,1]
]
print(solution.trapRainWater(heightMap4))
# Output: 2

# Example 5
heightMap5 = [
    [12,13,1,12],
    [13,4,13,12],
    [13,8,10,12],
    [12,13,12,12],
    [13,13,13,13]
]
print(solution.trapRainWater(heightMap5))
# Output: 14

# Example 6
heightMap6 = [
    [2,2,2],
    [2,2,2],
    [2,2,2]
]
print(solution.trapRainWater(heightMap6))
# Output: 0
