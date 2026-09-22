'''
312. Burst Balloons

You are given n balloons, indexed from 0 to n - 1.

Each balloon is painted with a number on it represented by nums.

You are asked to burst all the balloons.

If you burst balloon i, you will gain:

    nums[left] * nums[i] * nums[right]

coins.

Where:
    - left and right are adjacent balloons of i.
    - After the burst, left and right become adjacent.
    - If left or right goes out of bounds, treat it as 1.

Return the maximum coins you can collect by bursting all balloons wisely.

Example 1:
    Input:
        nums = [3,1,5,8]

    Output:
        167

Explanation:

        nums = [3,1,5,8]

        Burst 1  -> gain 3*1*5 = 15
        Burst 5  -> gain 3*5*8 = 120
        Burst 3  -> gain 1*3*8 = 24
        Burst 8  -> gain 1*8*1 = 8

        Total = 167

Example 2:
    Input:
        nums = [1,5]

    Output:
        10

Constraints:
    1 <= nums.length <= 300
    0 <= nums[i] <= 100
'''

# Interval Dynamic Programming

from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        # Add virtual balloons.
        balloons = [1] + nums + [1]

        n = len(balloons)

        # dp[left][right]
        dp = [
            [0] * n
            for _ in range(n)
        ]

        # Length of interval.
        for length in range(2, n):

            for left in range(n - length):

                right = left + length

                # Last balloon to burst.
                for k in range(left + 1, right):

                    coins = (
                        balloons[left]
                        * balloons[k]
                        * balloons[right]
                    )

                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][k]
                        + dp[k][right]
                        + coins
                    )

        return dp[0][n - 1]

# Example usage
solution = Solution()

# Example 1
nums1 = [3,1,5,8]
print(solution.maxCoins(nums1))
# Output: 167

# Example 2
nums2 = [1,5]
print(solution.maxCoins(nums2))
# Output: 10

# Example 3
nums3 = [7]
print(solution.maxCoins(nums3))
# Output: 7

# Example 4
nums4 = [1,2,3]
print(solution.maxCoins(nums4))
# Output: 12

# Example 5
nums5 = [9,7,1]
print(solution.maxCoins(nums5))
# Output: 135
