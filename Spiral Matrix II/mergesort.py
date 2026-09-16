"""
59. Spiral Matrix II

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.


Example 1
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]


Example 2:
Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
"""

#mergesort solution method

class Solution:
    def generateMatrix(self, n):

        matrix = [[0] * n for _ in range(n)]

        top = 0
        bottom = n - 1
        left = 0
        right = n - 1

        num = 1

        while top <= bottom and left <= right:

            # 1. Left → Right
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1

            top += 1

            # 2. Top → Bottom
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1

            right -= 1

            # 3. Right → Left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1

                bottom -= 1

            # 4. Bottom → Top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1

                left += 1

        return matrix
