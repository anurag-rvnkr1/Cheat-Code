'''
503. Next Greater Element II

Given a circular integer array nums, return the next greater number for every
element.

The next greater number is the first greater element encountered while moving
clockwise. If it doesn't exist, return -1.

Example 1:
    Input:
        nums = [1,2,1]

    Output:
        [2,-1,2]

Explanation:
        Next greater for 1 -> 2
        Next greater for 2 -> -1
        Next greater for last 1 -> 2 (circular)

Example 2:
    Input:
        nums = [1,2,3,4,3]

    Output:
        [2,3,4,-1,4]

Constraints:
    1 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
'''

# Monotonic Stack + Circular Array

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)

        answer = [-1] * n
        stack = []  # Stores indices.

        # Traverse twice to simulate circular array.
        for index in range(2 * n):
            current_index = index % n

            while (
                stack and
                nums[stack[-1]] < nums[current_index]
            ):
                answer[stack.pop()] = nums[current_index]

            # Push indices only during first traversal.
            if index < n:
                stack.append(current_index)

        return answer


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------

solution = Solution()

# Example 1
nums1 = [1,2,1]
print(solution.nextGreaterElements(nums1))
# Output: [2,-1,2]

# Example 2
nums2 = [1,2,3,4,3]
print(solution.nextGreaterElements(nums2))
# Output: [2,3,4,-1,4]

# Example 3
nums3 = [5,4,3,2,1]
print(solution.nextGreaterElements(nums3))
# Output: [-1,5,5,5,5]

# Example 4
nums4 = [2,2,2]
print(solution.nextGreaterElements(nums4))
# Output: [-1,-1,-1]

# Example 5
nums5 = [3,8,4,1,2]
print(solution.nextGreaterElements(nums5))
# Output: [8,-1,8,2,3]

# Example 6
nums6 = [6,5,4,3,2,1,7]
print(solution.nextGreaterElements(nums6))
# Output: [7,7,7,7,7,7,-1]
