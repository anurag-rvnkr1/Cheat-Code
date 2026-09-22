'''
410. Split Array Largest Sum

Given an integer array nums and an integer k, split nums into k non-empty
continuous subarrays.

Minimize the largest sum among these subarrays.

Return the minimized largest sum.

Example 1:
    Input:
        nums = [7,2,5,10,8]
        k = 2

    Output:
        18

Explanation:
        Split into [7,2,5] and [10,8].
        Largest sum = 18.

Example 2:
    Input:
        nums = [1,2,3,4,5]
        k = 2

    Output:
        9

Example 3:
    Input:
        nums = [1,4,4]
        k = 3

    Output:
        4

Constraints:
    1 <= nums.length <= 1000
    0 <= nums[i] <= 10^6
    1 <= k <= min(50, nums.length)
'''

# Binary Search on Answer + Greedy

from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        def can_split(max_sum: int) -> bool:
            subarrays = 1
            current_sum = 0

            for number in nums:
                if current_sum + number > max_sum:
                    subarrays += 1
                    current_sum = number

                    if subarrays > k:
                        return False
                else:
                    current_sum += number

            return True

        while left < right:
            middle = left + (right - left) // 2

            if can_split(middle):
                right = middle
            else:
                left = middle + 1

        return left


# Example usage
solution = Solution()

# Example 1
nums1 = [7,2,5,10,8]
k1 = 2
print(solution.splitArray(nums1, k1))
# Output: 18

# Example 2
nums2 = [1,2,3,4,5]
k2 = 2
print(solution.splitArray(nums2, k2))
# Output: 9

# Example 3
nums3 = [1,4,4]
k3 = 3
print(solution.splitArray(nums3, k3))
# Output: 4

# Example 4
nums4 = [2,3,1,2,4,3]
k4 = 5
print(solution.splitArray(nums4, k4))
# Output: 4

# Example 5
nums5 = [1,1,1,1,1]
k5 = 2
print(solution.splitArray(nums5, k5))
# Output: 3

# Example 6
nums6 = [10,20,30,40]
k6 = 2
print(solution.splitArray(nums6, k6))
# Output: 60
