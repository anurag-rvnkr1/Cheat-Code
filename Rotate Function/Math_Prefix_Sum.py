'''
396. Rotate Function

Given an integer array nums of length n.

Define the rotation function:

    F(k) = Σ(i * arr_k[i])

where arr_k is nums rotated clockwise k positions.

Return the maximum value of F(k).

Example 1:
    Input:
        nums = [4,3,2,6]

    Output:
        26

Explanation:
        F(0) = 25
        F(1) = 16
        F(2) = 23
        F(3) = 26

Example 2:
    Input:
        nums = [100]

    Output:
        0

Constraints:
    1 <= nums.length <= 10^5
    -100 <= nums[i] <= 100
'''

# Math + Prefix Sum

from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)

        total_sum = sum(nums)
        current_value = sum(index * value for index, value in enumerate(nums))

        maximum_value = current_value

        for rotation in range(1, n):
            current_value = (
                current_value +
                total_sum -
                n * nums[-rotation]
            )

            maximum_value = max(maximum_value, current_value)

        return maximum_value


# Example usage
solution = Solution()

# Example 1
nums1 = [4,3,2,6]
print(solution.maxRotateFunction(nums1))
# Output: 26

# Example 2
nums2 = [100]
print(solution.maxRotateFunction(nums2))
# Output: 0

# Example 3
nums3 = [1,2,3,4,5]
print(solution.maxRotateFunction(nums3))
# Output: 40

# Example 4
nums4 = [-1,-2,-3]
print(solution.maxRotateFunction(nums4))
# Output: -5

# Example 5
nums5 = [10,20,30]
print(solution.maxRotateFunction(nums5))
# Output: 80

# Example 6
nums6 = [7,8,9,1]
print(solution.maxRotateFunction(nums6))
# Output: 50
