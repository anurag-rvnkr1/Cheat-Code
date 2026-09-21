'''
296. Best Meeting Point

A group of two or more people wants to meet and minimize the total travel distance.

You are given a 2D binary grid where:
    - 1 represents a person's home.
    - 0 represents an empty cell.

Return the minimum total Manhattan distance from all people to the meeting point.

The Manhattan Distance between two points (x1, y1) and (x2, y2) is:

    |x1 - x2| + |y1 - y2|

Example 1:
    Input:
        grid = [
            [1,0,0,0,1],
            [0,0,0,0,0],
            [0,0,1,0,0]
        ]

    Output:
        6

Explanation:
    Meeting at (0,2) gives distance:
    2 + 2 + 2 = 6

Example 2:
    Input:
        grid = [[1,1]]
    Output:
        1

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    grid[i][j] is either 0 or 1.
    There will be at least two people.
'''

# Greedy + Median

from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows = []
        cols = []

        ROWS = len(grid)
        COLS = len(grid[0])

        # Collect row indices in sorted order.
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    rows.append(row)

        # Collect column indices in sorted order.
        for col in range(COLS):
            for row in range(ROWS):
                if grid[row][col] == 1:
                    cols.append(col)

        # Median minimizes Manhattan distance.
        median_row = rows[len(rows) // 2]
        median_col = cols[len(cols) // 2]

        distance = 0

        for row in rows:
            distance += abs(row - median_row)

        for col in cols:
            distance += abs(col - median_col)

        return distance


# Example usage
solution = Solution()

# Example 1
grid1 = [
    [1,0,0,0,1],
    [0,0,0,0,0],
    [0,0,1,0,0]
]

print(solution.minTotalDistance(grid1))
# Output: 6

# Example 2
grid2 = [
    [1,1]
]

print(solution.minTotalDistance(grid2))
# Output: 1

# Example 3
grid3 = [
    [1],
    [0],
    [1]
]

print(solution.minTotalDistance(grid3))
# Output: 2

# Example 4
grid4 = [
    [1,0,1],
    [0,0,0],
    [1,0,1]
]

print(solution.minTotalDistance(grid4))
# Output: 8
