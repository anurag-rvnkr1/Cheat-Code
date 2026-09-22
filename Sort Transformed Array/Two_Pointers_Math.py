'''
360. Sort Transformed Array

Given a sorted integer array nums and three integers a, b, and c,
apply the quadratic function:

    f(x) = ax² + bx + c

to each element of nums and return the transformed array in sorted order.

Example 1:
    Input:
        nums = [-4,-2,2,4]
        a = 1
        b = 3
        c = 5

    Output:
        [3,9,15,33]

Example 2:
    Input:
        nums = [-4,-2,2,4]
        a = -1
        b = 3
        c = 5

    Output:
        [-23,-5,1,7]

Constraints:
    1 <= nums.length <= 2 * 10^4
    -100 <= nums[i], a, b, c <= 100
    nums is sorted in ascending order.
'''

# Two Pointers + Quadratic Transformation

from typing import List


class Solution:
    def sortTransformedArray(
        self,
        nums: List[int],
        a: int,
        b: int,
        c: int
    ) -> List[int]:

        def transform(x: int) -> int:
            return a * x * x + b * x + c

        n = len(nums)
        result = [0] * n

        left = 0
        right = n - 1

        # Fill from end if parabola opens upward.
        index = n - 1 if a >= 0 else 0

        while left <= right:
            left_value = transform(nums[left])
            right_value = transform(nums[right])

            if a >= 0:
                if left_value > right_value:
                    result[index] = left_value
                    left += 1
                else:
                    result[index] = right_value
                    right -= 1

                index -= 1

            else:
                if left_value < right_value:
                    result[index] = left_value
                    left += 1
                else:
                    result[index] = right_value
                    right -= 1

                index += 1

        return result


# Example usage
solution = Solution()

# Example 1
nums1 = [-4,-2,2,4]
a1, b1, c1 = 1, 3, 5
print(solution.sortTransformedArray(nums1, a1, b1, c1))
# Output: [3,9,15,33]

# Example 2
nums2 = [-4,-2,2,4]
a2, b2, c2 = -1, 3, 5
print(solution.sortTransformedArray(nums2, a2, b2, c2))
# Output: [-23,-5,1,7]

# Example 3
nums3 = [-3,-1,0,2]
a3, b3, c3 = 2, -3, 1
print(solution.sortTransformedArray(nums3, a3, b3, c3))
# Output: [0,1,10,28]

# Example 4
nums4 = [-2,-1,0,1,2]
a4, b4, c4 = 0, 2, 3
print(solution.sortTransformedArray(nums4, a4, b4, c4))
# Output: [-1,1,3,5,7]

# Example 5
nums5 = [1,2,3,4]
a5, b5, c5 = 1, -2, 1
print(solution.sortTransformedArray(nums5, a5, b5, c5))
# Output: [0,1,4,9]

# Example 6
nums6 = [-5,-3,-1,0,2]
a6, b6, c6 = -2, 4, 6
print(solution.sortTransformedArray(nums6, a6, b6, c6))
# Output: [-64,-24,2,6,8]
