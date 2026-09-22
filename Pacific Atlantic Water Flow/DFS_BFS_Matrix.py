'''
417. Pacific Atlantic Water Flow

There is an m x n grid of heights.

Water can flow from a cell to neighboring cells (up, down, left, right)
with height less than or equal to the current cell.

The Pacific Ocean touches the left and top borders.
The Atlantic Ocean touches the right and bottom borders.

Return all coordinates where water can flow to both oceans.

Example 1:
    Input:
        heights = [
            [1,2,2,3,5],
            [3,2,3,4,4],
            [2,4,5,3,1],
            [6,7,1,4,5],
            [5,1,1,2,4]
        ]

    Output:
        [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Example 2:
    Input:
        heights = [[1]]

    Output:
        [[0,0]]

Constraints:
    m == heights.length
    n == heights[i].length
    1 <= m, n <= 200
    0 <= heights[r][c] <= 10^5
'''

# DFS + Matrix Traversal

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(row: int, col: int, visited: set):
            visited.add((row, col))

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[row][col]
                ):
                    dfs(nr, nc, visited)

        # Pacific borders.
        for row in range(rows):
            dfs(row, 0, pacific)
            dfs(row, cols - 1, atlantic)

        for col in range(cols):
            dfs(0, col, pacific)
            dfs(rows - 1, col, atlantic)

        result = []

        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])

        return result


# Example usage
solution = Solution()

# Example 1
heights1 = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]
print(solution.pacificAtlantic(heights1))
# Output:
# [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

# Example 2
heights2 = [[1]]
print(solution.pacificAtlantic(heights2))
# Output: [[0,0]]

# Example 3
heights3 = [
    [2,1],
    [1,2]
]
print(solution.pacificAtlantic(heights3))
# Output: [[0,0],[0,1],[1,0],[1,1]]

# Example 4
heights4 = [
    [10,10,10],
    [10,1,10],
    [10,10,10]
]
print(solution.pacificAtlantic(heights4))
# Output: All border cells.

# Example 5
heights5 = [
    [1,2,3],
    [8,9,4],
    [7,6,5]
]
print(solution.pacificAtlantic(heights5))
# Output: Cells reachable to both oceans.

# Example 6
heights6 = [
    [3,3,3],
    [3,3,3],
    [3,3,3]
]
print(solution.pacificAtlantic(heights6))
# Output: Every cell.
