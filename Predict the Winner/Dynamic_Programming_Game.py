'''
486. Predict the Winner

Two players play a game on an integer array nums.

Rules:
    - Players take turns.
    - Each player picks either the leftmost or rightmost number.
    - Both players play optimally.

Return True if Player 1 can win or tie.

Example 1:
    Input:
        nums = [1,5,2]

    Output:
        False

Example 2:
    Input:
        nums = [1,5,233,7]

    Output:
        True

Constraints:
    1 <= nums.length <= 20
    0 <= nums[i] <= 10^7
'''

# Dynamic Programming + Game Theory

from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        # dp[left][right] = maximum score difference current player can achieve.
        dp = [[0] * n for _ in range(n)]

        for index in range(n):
            dp[index][index] = nums[index]

        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                choose_left = nums[left] - dp[left + 1][right]
                choose_right = nums[right] - dp[left][right - 1]

                dp[left][right] = max(choose_left, choose_right)

        return dp[0][n - 1] >= 0


# Example usage
solution = Solution()

# Example 1
nums1 = [1,5,2]
print(solution.PredictTheWinner(nums1))
# Output: False

# Example 2
nums2 = [1,5,233,7]
print(solution.PredictTheWinner(nums2))
# Output: True

# Example 3
nums3 = [1,5,2,4,6]
print(solution.PredictTheWinner(nums3))
# Output: True

# Example 4
nums4 = [0]
print(solution.PredictTheWinner(nums4))
# Output: True

# Example 5
nums5 = [3,9,1,2]
print(solution.PredictTheWinner(nums5))
# Output: True

# Example 6
nums6 = [8,15,3,7]
print(solution.PredictTheWinner(nums6))
# Output: True
