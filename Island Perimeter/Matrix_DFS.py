'''
463. Island Perimeter

You are given a row x col grid representing a map where:

    - grid[i][j] = 1 represents land.
    - grid[i][j] = 0 represents water.

Grid cells are connected horizontally or vertically (not diagonally).

The grid contains exactly one island (one or more connected land cells).

Return the perimeter of the island.

Example 1:
    Input:
        grid = [
            [0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]
        ]

    Output:
        16

Example 2:
    Input:
        grid = [[1]]

    Output:
        4

Example 3:
    Input:
        grid = [[1,0]]

    Output:
        4

Constraints:
    row == grid.length
    col == grid[i].length
    1 <= row, col <= 100
    grid[i][j] is either 0 or 1.
    There is exactly one island.
'''

# Matrix Traversal (DFS / Simulation)

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        perimeter = 0

        directions = [
            (-1, 0),   # Up
            (1, 0),    # Down
            (0, -1),   # Left
            (0, 1)     # Right
        ]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    perimeter += 4

                    for dr, dc in directions:
                        new_row = row + dr
                        new_col = col + dc

                        if (
                            0 <= new_row < rows and
                            0 <= new_col < cols and
                            grid[new_row][new_col] == 1
                        ):
                            perimeter -= 1

        return perimeter


# Example usage
solution = Solution()

# Example 1
grid1 = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]
]
print(solution.islandPerimeter(grid1))
# Output: 16

# Example 2
grid2 = [[1]]
print(solution.islandPerimeter(grid2))
# Output: 4

# Example 3
grid3 = [[1,0]]
print(solution.islandPerimeter(grid3))
# Output: 4

# Example 4
grid4 = [
    [1,1],
    [1,1]
]
print(solution.islandPerimeter(grid4))
# Output: 8

# Example 5
grid5 = [
    [1,0,1],
    [0,0,0],
    [1,0,1]
]
print(solution.islandPerimeter(grid5))
# Output: 16

# Example 6
grid6 = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
print(solution.islandPerimeter(grid6))
# Output: 4
