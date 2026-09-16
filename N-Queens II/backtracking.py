"""
 N-Queens II

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 9
"""
#backtracking solution

class Solution:
    def totalNQueens(self, n):

        count = 0

        cols = set()
        diagonals = set()       # row - col
        anti_diagonals = set()  # row + col

        def backtrack(row):

            nonlocal count

            # All queens successfully placed
            if row == n:
                count += 1
                return

            # Try every column
            for col in range(n):

                # Check column
                if col in cols:
                    continue

                # Check \ diagonal
                if row - col in diagonals:
                    continue

                # Check / diagonal
                if row + col in anti_diagonals:
                    continue

                # Place queen
                cols.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)

                # Move to next row
                backtrack(row + 1)

                # Backtrack
                cols.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)

        backtrack(0)

        return count
