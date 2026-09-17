'''
90. Subsets II

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
    Input: nums = [1,2,2]
    Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
    Input: nums = [0]
    Output: [[],[0]]

Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
'''

# Backtracking with Duplicate Skipping
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result = []
        path = []

        def backtrack(start):

            # Every path is a valid subset
            result.append(path.copy())

            for i in range(start, len(nums)):

                # Skip duplicates at the same recursion level
                if i > start and nums[i] == nums[i - 1]:
                    continue

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

print(solution.subsetsWithDup([1, 2, 2]))
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

print(solution.subsetsWithDup([0]))
# Output: [[],[0]]

print(solution.subsetsWithDup([1, 1]))
# Output: [[],[1],[1,1]]
