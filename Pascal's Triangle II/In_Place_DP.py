'''
119. Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth (0-indexed) row of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example 1:
    Input: rowIndex = 3
    Output: [1,3,3,1]

Example 2:
    Input: rowIndex = 0
    Output: [1]

Example 3:
    Input: rowIndex = 1
    Output: [1,1]

Constraints:
    0 <= rowIndex <= 33
'''

# In-Place Dynamic Programming

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)

        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j - 1]

        return row


# Example usage
solution = Solution()

# Example 1
print(solution.getRow(3))  # Output: [1, 3, 3, 1]

# Example 2
print(solution.getRow(0))  # Output: [1]

# Example 3
print(solution.getRow(1))  # Output: [1, 1]

# Example 4
print(solution.getRow(4))  # Output: [1, 4, 6, 4, 1]
