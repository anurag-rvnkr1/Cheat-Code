'''
167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in
non-decreasing order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array [index1, index2],
where 1 <= index1 < index2 <= numbers.length.

Each input has exactly one solution, and you may not use the same element twice.

Your solution must use only constant extra space.

Example 1:
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]

Explanation:
    The sum of 2 and 7 is 9.
    Therefore, index1 = 1 and index2 = 2.

Example 2:
    Input: numbers = [2,3,4], target = 6
    Output: [1,3]

Example 3:
    Input: numbers = [-1,0], target = -1
    Output: [1,2]

Constraints:
    2 <= numbers.length <= 3 * 10^4
    -1000 <= numbers[i] <= 1000
    numbers is sorted in non-decreasing order.
    -1000 <= target <= 1000
    Exactly one valid solution exists.
'''

# Two Pointers

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]

            elif current_sum < target:
                left += 1

            else:
                right -= 1

        return []


# Example usage
solution = Solution()

# Example 1
numbers1 = [2, 7, 11, 15]
target1 = 9
print(solution.twoSum(numbers1, target1))  # Output: [1, 2]

# Example 2
numbers2 = [2, 3, 4]
target2 = 6
print(solution.twoSum(numbers2, target2))  # Output: [1, 3]

# Example 3
numbers3 = [-1, 0]
target3 = -1
print(solution.twoSum(numbers3, target3))  # Output: [1, 2]

# Example 4
numbers4 = [1, 2, 3, 4, 4, 9, 56, 90]
target4 = 8
print(solution.twoSum(numbers4, target4))  # Output: [4, 5]
