'''
179. Largest Number

Given a list of non-negative integers nums, arrange them such that they form
the largest number and return it.

Since the result may be very large, return it as a string instead of an integer.

Example 1:
    Input: nums = [10,2]
    Output: "210"

Example 2:
    Input: nums = [3,30,34,5,9]
    Output: "9534330"

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 10^9
'''

# Custom Sorting

from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            return 0

        numbers = list(map(str, nums))
        numbers.sort(key=cmp_to_key(compare))

        result = "".join(numbers)

        # Handle cases like [0,0]
        return "0" if result[0] == "0" else result


# Example usage
solution = Solution()

# Example 1
nums1 = [10, 2]
print(solution.largestNumber(nums1))  # Output: "210"

# Example 2
nums2 = [3, 30, 34, 5, 9]
print(solution.largestNumber(nums2))  # Output: "9534330"

# Example 3
nums3 = [1]
print(solution.largestNumber(nums3))  # Output: "1"

# Example 4
nums4 = [0, 0]
print(solution.largestNumber(nums4))  # Output: "0"
