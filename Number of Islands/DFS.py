'''
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land)
and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are
all surrounded by water.

Example 1:
    Input: grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    Output: 1

Example 2:
    Input: grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    Output: 3

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
'''

# Depth-First Search (DFS)

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(r: int, c: int):
            # Boundary check and water/visited check.
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == "0"
            ):
                return

            # Mark current land as visited.
            grid[r][c] = "0"

            # Explore four directions.
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands


# Example usage
solution = Solution()

# Example 1
grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

print(solution.numIslands(grid1))  # Output: 1

# Example 2
grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(solution.numIslands(grid2))  # Output: 3

# Example 3
grid3 = [
    ["1", "0", "1", "0"],
    ["0", "1", "0", "1"],
    ["1", "0", "1", "0"]
]

print(solution.numIslands(grid3))  # Output: 6

# Example 4
grid4 = [["0"]]

print(solution.numIslands(grid4))  # Output: 0
