'''
363. Max Sum of Rectangle No Larger Than K

Given an m x n matrix and an integer k, return the maximum sum of a rectangle
in the matrix such that its sum is no larger than k.

It is guaranteed that there will be a rectangle with a sum no larger than k.

Example 1:
    Input:
        matrix = [[1,0,1],[0,-2,3]]
        k = 2

    Output:
        2

Explanation:
        Rectangle [[0,1],[-2,3]] has sum = 2.

Example 2:
    Input:
        matrix = [[2,2,-1]]
        k = 3

    Output:
        3

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -100 <= matrix[i][j] <= 100
    -10^5 <= k <= 10^5
'''

# Prefix Sum + Binary Search (Sorted Prefix Sums)

from typing import List
from bisect import bisect_left, insort


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        answer = float("-inf")

        # Iterate over left column.
        for left in range(cols):

            row_sum = [0] * rows

            # Expand right column.
            for right in range(left, cols):

                for row in range(rows):
                    row_sum[row] += matrix[row][right]

                prefix_sum = 0
                sorted_prefix = [0]

                current_best = float("-inf")

                for value in row_sum:
                    prefix_sum += value

                    index = bisect_left(sorted_prefix, prefix_sum - k)

                    if index < len(sorted_prefix):
                        current_best = max(
                            current_best,
                            prefix_sum - sorted_prefix[index]
                        )

                    insort(sorted_prefix, prefix_sum)

                answer = max(answer, current_best)

        return answer


# Example usage
solution = Solution()

# Example 1
matrix1 = [
    [1,0,1],
    [0,-2,3]
]
k1 = 2
print(solution.maxSumSubmatrix(matrix1, k1))
# Output: 2

# Example 2
matrix2 = [[2,2,-1]]
k2 = 3
print(solution.maxSumSubmatrix(matrix2, k2))
# Output: 3

# Example 3
matrix3 = [
    [2,1],
    [-3,4]
]
k3 = 4
print(solution.maxSumSubmatrix(matrix3, k3))
# Output: 4

# Example 4
matrix4 = [
    [5,-4,-3,4],
    [-3,-4,4,5],
    [5,1,5,-4]
]
k4 = 8
print(solution.maxSumSubmatrix(matrix4, k4))
# Output: 8

# Example 5
matrix5 = [
    [1,2,-1],
    [-3,4,2],
    [5,-2,3]
]
k5 = 7
print(solution.maxSumSubmatrix(matrix5, k5))
# Output: 7

# Example 6
matrix6 = [
    [-1,-2],
    [-3,-4]
]
k6 = -2
print(solution.maxSumSubmatrix(matrix6, k6))
# Output: -2
