'''
361. Bomb Enemy

Given an m x n grid where:

    'W' -> Wall
    'E' -> Enemy
    '0' -> Empty Cell

You can place one bomb in an empty cell.

The bomb kills all enemies in the same row and column until blocked by a wall.

Return the maximum enemies that can be killed with one bomb.

Example 1:
    Input:
        grid = [
            ["0","E","0","0"],
            ["E","0","W","E"],
            ["0","E","0","0"]
        ]

    Output:
        3

Example 2:
    Input:
        grid = [["W","W","W"],["0","0","0"],["E","E","E"]]

    Output:
        1

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 500
    grid[i][j] is 'W', 'E', or '0'.
'''

# Matrix Prefix Counting

from typing import List


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        row_hits = 0
        col_hits = [0] * cols

        answer = 0

        for row in range(rows):
            for col in range(cols):

                # Recompute row hits after wall.
                if col == 0 or grid[row][col - 1] == "W":
                    row_hits = 0
                    current = col

                    while current < cols and grid[row][current] != "W":
                        if grid[row][current] == "E":
                            row_hits += 1
                        current += 1

                # Recompute column hits after wall.
                if row == 0 or grid[row - 1][col] == "W":
                    col_hits[col] = 0
                    current = row

                    while current < rows and grid[current][col] != "W":
                        if grid[current][col] == "E":
                            col_hits[col] += 1
                        current += 1

                if grid[row][col] == "0":
                    answer = max(answer, row_hits + col_hits[col])

        return answer


# Example usage
solution = Solution()

# Example 1
grid1 = [
    ["0","E","0","0"],
    ["E","0","W","E"],
    ["0","E","0","0"]
]
print(solution.maxKilledEnemies(grid1))
# Output: 3

# Example 2
grid2 = [
    ["W","W","W"],
    ["0","0","0"],
    ["E","E","E"]
]
print(solution.maxKilledEnemies(grid2))
# Output: 1

# Example 3
grid3 = [["0"]]
print(solution.maxKilledEnemies(grid3))
# Output: 0

# Example 4
grid4 = [
    ["E","0","E"],
    ["0","W","0"],
    ["E","0","E"]
]
print(solution.maxKilledEnemies(grid4))
# Output: 2

# Example 5
grid5 = [
    ["0","E","E","0"],
    ["E","W","E","E"],
    ["0","E","0","E"]
]
print(solution.maxKilledEnemies(grid5))
# Output: 4

# Example 6
grid6 = [
    ["E","E"],
    ["E","0"]
]
print(solution.maxKilledEnemies(grid6))
# Output: 2
