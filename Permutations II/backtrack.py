"""
47. Permutations II
Solved
Medium
Topics
premium lock icon
Companies
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""
#bakctra Method
class Solution:
    def permuteUnique(self, nums):

        nums.sort()

        result = []
        used = [False] * len(nums)

        def backtrack(path):

            # Complete permutation
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):

                # Already used
                if used[i]:
                    continue

                # Skip duplicate choices
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                # Choose
                used[i] = True
                path.append(nums[i])

                # Explore
                backtrack(path)

                # Undo
                path.pop()
                used[i] = False

        backtrack([])

        return result
