'''
370. Range Addition

You are given an integer length and an array updates where:

    updates[i] = [startIndex, endIndex, increment]

For each update, increment all elements in the inclusive range
[startIndex, endIndex] by increment.

Return the modified array after all updates.

Example 1:
    Input:
        length = 5
        updates = [
            [1,3,2],
            [2,4,3],
            [0,2,-2]
        ]

    Output:
        [-2,0,3,5,3]

Example 2:
    Input:
        length = 10
        updates = [
            [2,4,6],
            [5,6,8],
            [1,9,-4]
        ]

    Output:
        [0,-4,2,2,2,4,4,-4,-4,-4]

Constraints:
    1 <= length <= 10^5
    0 <= updates.length <= 10^4
    0 <= startIndex <= endIndex < length
    -1000 <= increment <= 1000
'''

# Difference Array + Prefix Sum

from typing import List


class Solution:
    def getModifiedArray(
        self,
        length: int,
        updates: List[List[int]]
    ) -> List[int]:

        difference = [0] * length

        # Apply difference updates.
        for start, end, increment in updates:
            difference[start] += increment

            if end + 1 < length:
                difference[end + 1] -= increment

        # Prefix sum to construct final array.
        for index in range(1, length):
            difference[index] += difference[index - 1]

        return difference


# Example usage
solution = Solution()

# Example 1
length1 = 5
updates1 = [
    [1,3,2],
    [2,4,3],
    [0,2,-2]
]

print(solution.getModifiedArray(length1, updates1))
# Output: [-2,0,3,5,3]

# Example 2
length2 = 10
updates2 = [
    [2,4,6],
    [5,6,8],
    [1,9,-4]
]

print(solution.getModifiedArray(length2, updates2))
# Output: [0,-4,2,2,2,4,4,-4,-4,-4]

# Example 3
length3 = 4
updates3 = [
    [0,3,5]
]

print(solution.getModifiedArray(length3, updates3))
# Output: [5,5,5,5]

# Example 4
length4 = 6
updates4 = [
    [1,2,3],
    [2,5,2],
    [0,0,7]
]

print(solution.getModifiedArray(length4, updates4))
# Output: [7,3,5,2,2,2]

# Example 5
length5 = 3
updates5 = []

print(solution.getModifiedArray(length5, updates5))
# Output: [0,0,0]

# Example 6
length6 = 8
updates6 = [
    [0,4,1],
    [3,7,2],
    [5,7,-1]
]

print(solution.getModifiedArray(length6, updates6))
# Output: [1,1,1,3,3,1,1,1]
