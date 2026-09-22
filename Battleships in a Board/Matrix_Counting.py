'''
419. Battleships in a Board

Given an m x n board where:

    'X' -> Part of a battleship.
    '.' -> Empty cell.

Return the number of battleships on the board.

Rules:
    - Battleships are placed horizontally or vertically.
    - Battleships are separated by at least one empty cell.
    - Do not modify the board.

Example 1:
    Input:
        board = [
            ["X",".",".","X"],
            [".",".",".","X"],
            [".",".",".","X"]
        ]

    Output:
        2

Example 2:
    Input:
        board = [["."]]

    Output:
        0

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 200
    board[i][j] is either 'X' or '.'

Follow-up:
    Solve using O(1) extra memory and one pass.
'''

# Matrix Traversal + Counting

from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board)
        cols = len(board[0])

        battleships = 0

        for row in range(rows):
            for col in range(cols):

                if board[row][col] == ".":
                    continue

                # Skip cells that are continuation of a battleship.
                if row > 0 and board[row - 1][col] == "X":
                    continue

                if col > 0 and board[row][col - 1] == "X":
                    continue

                battleships += 1

        return battleships


# Example usage
solution = Solution()

# Example 1
board1 = [
    ["X",".",".","X"],
    [".",".",".","X"],
    [".",".",".","X"]
]
print(solution.countBattleships(board1))
# Output: 2

# Example 2
board2 = [["."]]
print(solution.countBattleships(board2))
# Output: 0

# Example 3
board3 = [
    ["X","X",".","X"],
    [".",".",".","."],
    ["X",".","X","X"]
]
print(solution.countBattleships(board3))
# Output: 4

# Example 4
board4 = [
    ["X","X","X"],
    [".",".","."],
    ["X",".","X"]
]
print(solution.countBattleships(board4))
# Output: 3

# Example 5
board5 = [
    ["X"],
    ["X"],
    ["."],
    ["X"]
]
print(solution.countBattleships(board5))
# Output: 2

# Example 6
board6 = [
    [".",".","."],
    [".","X","."],
    [".",".","."]
]
print(solution.countBattleships(board6))
# Output: 1
