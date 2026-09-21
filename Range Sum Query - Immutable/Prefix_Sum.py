'''
303. Range Sum Query - Immutable

Given an integer array nums, handle multiple queries of the following type:

    sumRange(left, right)

Return the sum of the elements between indices left and right (inclusive).

Implement the NumArray class:

    - NumArray(nums) Initializes the object.
    - sumRange(left, right) Returns the sum of nums[left...right].

Example 1:
    Input:
        ["NumArray","sumRange","sumRange","sumRange"]
        [[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]

    Output:
        [null,1,-1,-3]

Explanation:
    nums = [-2,0,3,-5,2,-1]

    sumRange(0,2) = -2 + 0 + 3 = 1
    sumRange(2,5) = 3 + (-5) + 2 + (-1) = -1
    sumRange(0,5) = -3

Constraints:
    1 <= nums.length <= 10^4
    -10^5 <= nums[i] <= 10^5
    0 <= left <= right < nums.length
    At most 10^4 calls will be made to sumRange().
'''

# Prefix Sum

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        # prefix_sum[i] stores sum of first i elements.
        self.prefix_sum = [0]

        for number in nums:
            self.prefix_sum.append(
                self.prefix_sum[-1] + number
            )

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


# Example usage

# Example 1
numArray = NumArray([-2, 0, 3, -5, 2, -1])

print(numArray.sumRange(0, 2))
# Output: 1

print(numArray.sumRange(2, 5))
# Output: -1

print(numArray.sumRange(0, 5))
# Output: -3


# Example 2
numArray2 = NumArray([1, 2, 3, 4, 5])

print(numArray2.sumRange(1, 3))
# Output: 9

print(numArray2.sumRange(0, 4))
# Output: 15


# Example 3
numArray3 = NumArray([10])

print(numArray3.sumRange(0, 0))
# Output: 10
