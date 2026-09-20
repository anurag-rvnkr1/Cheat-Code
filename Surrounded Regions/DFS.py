'''
130. Surrounded Regions

You are given an m x n matrix board containing letters 'X' and 'O'.
Capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:
    Input: board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ]
    Output: [
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","O","X","X"]
    ]

Example 2:
    Input: board = [["X"]]
    Output: [["X"]]

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 200
    board[i][j] is 'X' or 'O'.
'''

# Depth-First Search (DFS)

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != "O"
            ):
                return

            board[r][c] = "#"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Mark border-connected 'O's
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # Flip surrounded regions and restore border regions
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"


# Example usage
solution = Solution()

# Example 1
board1 = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
]

solution.solve(board1)
print(board1)
# Output:
# [['X','X','X','X'],
#  ['X','X','X','X'],
#  ['X','X','X','X'],
#  ['X','O','X','X']]

# Example 2
board2 = [["X"]]

solution.solve(board2)
print(board2)
# Output: [['X']]
