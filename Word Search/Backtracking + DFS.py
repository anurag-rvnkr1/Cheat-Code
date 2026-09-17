'''
79. Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
    Input:
        board = [["A","B","C","E"],
                 ["S","F","C","S"],
                 ["A","D","E","E"]]
        word = "ABCCED"
    Output: True

Example 2:
    Input:
        board = [["A","B","C","E"],
                 ["S","F","C","S"],
                 ["A","D","E","E"]]
        word = "SEE"
    Output: True

Example 3:
    Input:
        board = [["A","B","C","E"],
                 ["S","F","C","S"],
                 ["A","D","E","E"]]
        word = "ABCB"
    Output: False

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consist of only lowercase and uppercase English letters.
'''

# Backtracking + DFS
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, index):

            # All characters matched
            if index == len(word):
                return True

            # Out of bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            # Character doesn't match
            if board[r][c] != word[index]:
                return False

            # Mark current cell as visited
            temp = board[r][c]
            board[r][c] = '#'

            # Explore four directions
            found = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )

            # Backtrack: restore original character
            board[r][c] = temp

            return found

        # Try every cell as the starting point
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False


# Example usage
solution = Solution()

board1 = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

print(solution.exist(board1, "ABCCED"))  # Output: True

board2 = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

print(solution.exist(board2, "SEE"))  # Output: True

board3 = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

print(solution.exist(board3, "ABCB"))  # Output: False
