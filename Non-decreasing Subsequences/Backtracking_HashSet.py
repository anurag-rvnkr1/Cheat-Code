'''
491. Non-decreasing Subsequences

Given an integer array nums, return all different non-decreasing subsequences
of length at least 2.

A subsequence is obtained by deleting some elements without changing order.

Example 1:
    Input:
        nums = [4,6,7,7]

    Output:
        [
            [4,6],
            [4,7],
            [4,6,7],
            [4,6,7,7],
            [6,7],
            [6,7,7],
            [7,7],
            [4,7,7]
        ]

Example 2:
    Input:
        nums = [4,4,3,2,1]

    Output:
        [[4,4]]

Constraints:
    1 <= nums.length <= 15
    -100 <= nums[i] <= 100
'''

# Backtracking + HashSet

from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answer = []
        current_subsequence = []

        def backtrack(index: int):
            if len(current_subsequence) >= 2:
                answer.append(current_subsequence[:])

            used = set()

            for position in range(index, len(nums)):
                if nums[position] in used:
                    continue

                if (
                    current_subsequence and
                    nums[position] < current_subsequence[-1]
                ):
                    continue

                used.add(nums[position])

                current_subsequence.append(nums[position])

                backtrack(position + 1)

                current_subsequence.pop()

        backtrack(0)

        return answer


# Example usage
solution = Solution()

# Example 1
nums1 = [4,6,7,7]
print(solution.findSubsequences(nums1))
# Output:
# [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],
#  [6,7],[6,7,7],[7,7]]

# Example 2
nums2 = [4,4,3,2,1]
print(solution.findSubsequences(nums2))
# Output: [[4,4]]

# Example 3
nums3 = [1,2,3]
print(solution.findSubsequences(nums3))
# Output:
# [[1,2],[1,2,3],[1,3],[2,3]]

# Example 4
nums4 = [1,1,1]
print(solution.findSubsequences(nums4))
# Output:
# [[1,1],[1,1,1]]

# Example 5
nums5 = [3,2,1]
print(solution.findSubsequences(nums5))
# Output: []

# Example 6
nums6 = [2,5,4,5]
print(solution.findSubsequences(nums6))
# Output:
# [[2,5],[2,5,5],[2,4],[2,4,5],[5,5],[4,5]]
