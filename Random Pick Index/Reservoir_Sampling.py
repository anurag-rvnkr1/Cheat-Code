'''
398. Random Pick Index

Given an integer array nums with possible duplicates, randomly return the index
of a given target number.

Each valid index should have an equal probability of being returned.

Implement the Solution class:

    Solution(int[] nums)
        Initializes the object with the array nums.

    int pick(int target)
        Returns a random index where nums[index] == target.

Example 1:
    Input:
        ["Solution","pick","pick","pick"]

        [[[1,2,3,3,3]],[3],[1],[3]]

    Output:
        [null,2,0,4]

Explanation:
        pick(3) should randomly return index 2, 3, or 4.
        Each index has probability 1/3.

Constraints:
    1 <= nums.length <= 2 * 10^4
    -2^31 <= nums[i] <= 2^31 - 1
    target is guaranteed to exist in nums.
    At most 10^4 calls will be made to pick().

Follow-up:
    Can you solve this without using extra space?
'''

# Reservoir Sampling

from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        chosen_index = -1
        count = 0

        for index, value in enumerate(self.nums):
            if value == target:
                count += 1

                # Replace previous choice with probability 1/count.
                if random.randint(1, count) == 1:
                    chosen_index = index

        return chosen_index


# Example usage
nums = [1,2,3,3,3]
solution = Solution(nums)

print(solution.pick(3))
# Output: 2 or 3 or 4 (equal probability)

print(solution.pick(1))
# Output: 0

print(solution.pick(3))
# Output: 2 or 3 or 4

# Example 2
nums2 = [5,5,5,5]
solution2 = Solution(nums2)

print(solution2.pick(5))
# Output: Random index from {0,1,2,3}

print(solution2.pick(5))
# Output: Random index from {0,1,2,3}

# Example 3
nums3 = [10,20,30,20,40,20]
solution3 = Solution(nums3)

print(solution3.pick(20))
# Output: Random index from {1,3,5}

print(solution3.pick(30))
# Output: 2
