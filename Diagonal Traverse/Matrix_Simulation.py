'''
498. Diagonal Traverse

Given an m x n matrix mat, return all elements of the matrix in diagonal order.

Traversal Pattern:
    - Even-numbered diagonals → move Up-Right.
    - Odd-numbered diagonals → move Down-Left.

Example 1:
    Input:
        mat = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]

    Output:
        [1,2,4,7,5,3,6,8,9]

Example 2:
    Input:
        mat = [
            [1,2],
            [3,4]
        ]

    Output:
        [1,2,3,4]

Constraints:
    m == mat.length
    n == mat[i].length
    1 <= m, n <= 10^4
    1 <= m * n <= 10^4
'''

# Matrix Simulation

from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        rows = len(mat)
        cols = len(mat[0])

        answer = []

        for diagonal in range(rows + cols - 1):
            current = []

            # Starting row and column for this diagonal.
            row = 0 if diagonal < cols else diagonal - cols + 1
            col = diagonal if diagonal < cols else cols - 1

            while row < rows and col >= 0:
                current.append(mat[row][col])
                row += 1
                col -= 1

            if diagonal % 2 == 0:
                answer.extend(current[::-1])
            else:
                answer.extend(current)

        return answer


# Example usage
solution = Solution()

# Example 1
mat1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(solution.findDiagonalOrder(mat1))
# Output: [1,2,4,7,5,3,6,8,9]

# Example 2
mat2 = [
    [1,2],
    [3,4]
]
print(solution.findDiagonalOrder(mat2))
# Output: [1,2,3,4]

# Example 3
mat3 = [[1,2,3,4]]
print(solution.findDiagonalOrder(mat3))
# Output: [1,2,3,4]

# Example 4
mat4 = [
    [1],
    [2],
    [3],
    [4]
]
print(solution.findDiagonalOrder(mat4))
# Output: [1,2,3,4]

# Example 5
mat5 = [
    [1,2,3],
    [4,5,6]
]
print(solution.findDiagonalOrder(mat5))
# Output: [1,2,4,5,3,6]

# Example 6
mat6 = [
    [1,2],
    [3,4],
    [5,6]
]
print(solution.findDiagonalOrder(mat6))
# Output: [1,2,3,5,4,6]
