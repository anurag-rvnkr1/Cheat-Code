'''
378. Kth Smallest Element in a Sorted Matrix

Given an n x n matrix where each row and each column is sorted in ascending order,
return the kth smallest element in the matrix.

Note:
    It is the kth smallest element in the sorted order,
    not the kth distinct element.

Example 1:
    Input:
        matrix = [
            [1,5,9],
            [10,11,13],
            [12,13,15]
        ]
        k = 8

    Output:
        13

Example 2:
    Input:
        matrix = [[-5]]
        k = 1

    Output:
        -5

Constraints:
    n == matrix.length == matrix[i].length
    1 <= n <= 300
    -10^9 <= matrix[i][j] <= 10^9
    All rows and columns are sorted.
    1 <= k <= n^2

Follow-up:
    Solve with O(n log(max-min)) time complexity.
'''

# Binary Search on Answer

from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        left = matrix[0][0]
        right = matrix[-1][-1]

        def count_less_equal(target: int) -> int:
            count = 0
            row = n - 1
            col = 0

            while row >= 0 and col < n:
                if matrix[row][col] <= target:
                    count += row + 1
                    col += 1
                else:
                    row -= 1

            return count

        while left < right:
            middle = left + (right - left) // 2

            if count_less_equal(middle) < k:
                left = middle + 1
            else:
                right = middle

        return left


# Example usage
solution = Solution()

# Example 1
matrix1 = [
    [1,5,9],
    [10,11,13],
    [12,13,15]
]
k1 = 8
print(solution.kthSmallest(matrix1, k1))
# Output: 13

# Example 2
matrix2 = [[-5]]
k2 = 1
print(solution.kthSmallest(matrix2, k2))
# Output: -5

# Example 3
matrix3 = [
    [1,2],
    [1,3]
]
k3 = 2
print(solution.kthSmallest(matrix3, k3))
# Output: 1

# Example 4
matrix4 = [
    [1,3,5],
    [6,7,12],
    [11,14,14]
]
k4 = 6
print(solution.kthSmallest(matrix4, k4))
# Output: 11

# Example 5
matrix5 = [
    [2,4,6],
    [3,5,7],
    [8,9,10]
]
k5 = 5
print(solution.kthSmallest(matrix5, k5))
# Output: 5

# Example 6
matrix6 = [
    [-10,-5,0],
    [-4,-2,3],
    [1,5,8]
]
k6 = 7
print(solution.kthSmallest(matrix6, k6))
# Output: 3
