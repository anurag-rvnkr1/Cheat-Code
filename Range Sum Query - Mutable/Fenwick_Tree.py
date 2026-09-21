'''
307. Range Sum Query - Mutable

Given an integer array nums, handle multiple queries of the following types:

    1. update(index, val)
       Update nums[index] to val.

    2. sumRange(left, right)
       Return the sum of the elements between indices left and right (inclusive).

Implement the NumArray class:

    - NumArray(nums) Initializes the object.
    - update(index, val) Updates the value at index.
    - sumRange(left, right) Returns the sum of nums[left...right].

Example 1:
    Input:
        ["NumArray","sumRange","update","sumRange"]
        [[[1,3,5]],[0,2],[1,2],[0,2]]

    Output:
        [null,9,null,8]

Explanation:
    nums = [1,3,5]

    sumRange(0,2) = 9
    update(1,2)
    nums becomes [1,2,5]
    sumRange(0,2) = 8

Constraints:
    1 <= nums.length <= 3 * 10^4
    -100 <= nums[i] <= 100
    0 <= index < nums.length
    -100 <= val <= 100
    0 <= left <= right < nums.length
    At most 3 * 10^4 calls will be made to update() and sumRange().
'''

# Binary Indexed Tree (Fenwick Tree)

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums[:]

        # Fenwick Tree uses 1-based indexing.
        self.bit = [0] * (self.n + 1)

        for i, value in enumerate(nums):
            self._add(i + 1, value)

    def _add(self, index: int, delta: int) -> None:
        while index <= self.n:
            self.bit[index] += delta
            index += index & -index

    def _prefix_sum(self, index: int) -> int:
        total = 0

        while index > 0:
            total += self.bit[index]
            index -= index & -index

        return total

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val

        self._add(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        return (
            self._prefix_sum(right + 1)
            - self._prefix_sum(left)
        )


# Example usage

# Example 1
numArray = NumArray([1, 3, 5])

print(numArray.sumRange(0, 2))
# Output: 9

numArray.update(1, 2)

print(numArray.sumRange(0, 2))
# Output: 8


# Example 2
numArray2 = NumArray([2, 4, 6, 8])

print(numArray2.sumRange(1, 3))
# Output: 18

numArray2.update(2, 10)

print(numArray2.sumRange(1, 3))
# Output: 22


# Example 3
numArray3 = NumArray([5])

print(numArray3.sumRange(0, 0))
# Output: 5

numArray3.update(0, 7)

print(numArray3.sumRange(0, 0))
# Output: 7
