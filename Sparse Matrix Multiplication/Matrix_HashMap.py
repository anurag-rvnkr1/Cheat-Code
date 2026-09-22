'''
311. Sparse Matrix Multiplication

Given two sparse matrices mat1 and mat2, return the result of mat1 x mat2.

You may assume that multiplication is always possible.

Example 1:
    Input:
        mat1 = [
            [1,0,0],
            [-1,0,3]
        ]

        mat2 = [
            [7,0,0],
            [0,0,0],
            [0,0,1]
        ]

    Output:
        [
            [7,0,0],
            [-7,0,3]
        ]

Example 2:
    Input:
        mat1 = [[0]]
        mat2 = [[0]]

    Output:
        [[0]]

Constraints:
    m == mat1.length
    k == mat1[i].length
    k == mat2.length
    n == mat2[i].length

    1 <= m, n, k <= 100
    -100 <= mat1[i][j], mat2[i][j] <= 100
'''

# Matrix + Sparse Optimization

from typing import List

class Solution:
    def multiply(
        self,
        mat1: List[List[int]],
        mat2: List[List[int]]
    ) -> List[List[int]]:

        rows = len(mat1)
        common = len(mat1[0])
        cols = len(mat2[0])

        result = [
            [0] * cols
            for _ in range(rows)
        ]

        # Store only non-zero values of mat2.
        non_zero = {}

        for row in range(common):
            non_zero[row] = []

            for col in range(cols):
                if mat2[row][col] != 0:
                    non_zero[row].append(
                        (col, mat2[row][col])
                    )

        for row in range(rows):
            for k in range(common):

                if mat1[row][k] == 0:
                    continue

                for col, value in non_zero[k]:
                    result[row][col] += (
                        mat1[row][k] * value
                    )

        return result

# Example usage
solution = Solution()

# Example 1
mat1 = [
    [1,0,0],
    [-1,0,3]
]

mat2 = [
    [7,0,0],
    [0,0,0],
    [0,0,1]
]

print(solution.multiply(mat1, mat2))
# Output:
# [
#   [7,0,0],
#   [-7,0,3]
# ]

# Example 2
mat1 = [[0]]
mat2 = [[0]]

print(solution.multiply(mat1, mat2))
# Output: [[0]]

# Example 3
mat1 = [
    [1,2],
    [3,4]
]

mat2 = [
    [5,6],
    [7,8]
]

print(solution.multiply(mat1, mat2))
# Output:
# [
#   [19,22],
#   [43,50]
# ]

# Example 4
mat1 = [
    [0,0,1]
]

mat2 = [
    [0],
    [0],
    [5]
]

print(solution.multiply(mat1, mat2))
# Output: [[5]]
