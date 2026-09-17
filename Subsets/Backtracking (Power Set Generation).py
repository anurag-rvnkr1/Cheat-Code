'''
78. Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
    Input: nums = [0]
    Output: [[],[0]]

Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.
'''

# Backtracking (Power Set Generation)
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        path = []

        def backtrack(start):

            # Every path is a valid subset
            result.append(path.copy())

            for i in range(start, len(nums)):

                # Choose
                path.append(nums[i])

                # Explore
                backtrack(i + 1)

                # Undo choice
                path.pop()

        backtrack(0)

        return result


# Example usage
solution = Solution()

print(solution.subsets([1, 2, 3]))
# Output: [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]

print(solution.subsets([0]))
# Output: [[],[0]]

print(solution.subsets([1, 2]))
# Output: [[],[1],[1,2],[2]]
