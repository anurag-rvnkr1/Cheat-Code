""'
N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9
"""
#basic backtracking solution

class Solution:
    def solveNQueens(self, n):

        result = []

        board = [["."] * n for _ in range(n)]

        cols = set()
        diagonals = set()       # row - col
        anti_diagonals = set()  # row + col

        def backtrack(row):

            # All queens placed
            if row == n:
                solution = []

                for r in board:
                    solution.append("".join(r))

                result.append(solution)
                return

            # Try every column in this row
            for col in range(n):

                # Check if queen is attacked
                if col in cols:
                    continue

                if row - col in diagonals:
                    continue

                if row + col in anti_diagonals:
                    continue

                # Place queen
                board[row][col] = "Q"

                cols.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)

                # Move to next row
                backtrack(row + 1)

                # Backtrack / remove queen
                board[row][col] = "."

                cols.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)

        backtrack(0)

        return result
