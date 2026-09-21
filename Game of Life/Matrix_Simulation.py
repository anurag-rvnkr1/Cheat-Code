'''
289. Game of Life

According to Conway's Game of Life, each cell interacts with its eight neighbors.

Rules:
    1. Any live cell with fewer than two live neighbors dies.
    2. Any live cell with two or three live neighbors lives.
    3. Any live cell with more than three live neighbors dies.
    4. Any dead cell with exactly three live neighbors becomes a live cell.

Given the current state of the board, update it to the next state.

You must modify the board in-place.

Example 1:
    Input:
        board = [
            [0,1,0],
            [0,0,1],
            [1,1,1],
            [0,0,0]
        ]

    Output:
        [
            [0,0,0],
            [1,0,1],
            [0,1,1],
            [0,1,0]
        ]

Example 2:
    Input:
        board = [
            [1,1],
            [1,0]
        ]

    Output:
        [
            [1,1],
            [1,1]
        ]

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 25
    board[i][j] is either 0 or 1.
'''

# Matrix Simulation

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything.
        Modify board in-place.
        """

        ROWS = len(board)
        COLS = len(board[0])

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        # First pass: mark transitions.
        for row in range(ROWS):
            for col in range(COLS):

                live_neighbors = 0

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        abs(board[nr][nc]) == 1
                    ):
                        live_neighbors += 1

                if board[row][col] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[row][col] = -1      # Live → Dead

                else:
                    if live_neighbors == 3:
                        board[row][col] = 2       # Dead → Live

        # Second pass: finalize states.
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0


# Example usage
solution = Solution()

# Example 1
board1 = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]

solution.gameOfLife(board1)
print(board1)
# Output:
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]

# Example 2
board2 = [
    [1, 1],
    [1, 0]
]

solution.gameOfLife(board2)
print(board2)
# Output:
# [
#   [1,1],
#   [1,1]
# ]

# Example 3
board3 = [
    [1, 0],
    [0, 1]
]

solution.gameOfLife(board3)
print(board3)
# Output:
# [
#   [0,0],
#   [0,0]
# ]

# Example 4
board4 = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

solution.gameOfLife(board4)
print(board4)
# Output:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
