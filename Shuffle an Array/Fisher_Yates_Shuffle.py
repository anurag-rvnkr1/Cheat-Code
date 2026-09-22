'''
384. Shuffle an Array

Given an integer array nums, design an algorithm to randomly shuffle the array.

Implement the Solution class:

    Solution(int[] nums)
        Initializes the object with the array nums.

    int[] reset()
        Resets the array to its original configuration and returns it.

    int[] shuffle()
        Returns a random shuffling of the array.

All permutations of the array should be equally likely.

Example 1:
    Input:
        ["Solution","shuffle","reset","shuffle"]

        [[[1,2,3]],[],[],[]]

    Output:
        [null,[2,1,3],[1,2,3],[1,3,2]]

Explanation:
        Every permutation has equal probability.

Constraints:
    1 <= nums.length <= 200
    -10^6 <= nums[i] <= 10^6
    All elements of nums are unique.
    At most 5 * 10^4 calls will be made to reset() and shuffle().
'''

# Fisher-Yates Shuffle

from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.array = nums[:]

    def reset(self) -> List[int]:
        self.array = self.original[:]
        return self.array

    def shuffle(self) -> List[int]:
        shuffled = self.array[:]
        n = len(shuffled)

        for index in range(n):
            random_index = random.randint(index, n - 1)
            shuffled[index], shuffled[random_index] = (
                shuffled[random_index],
                shuffled[index]
            )

        return shuffled


# Example usage
nums = [1,2,3]
solution = Solution(nums)

print(solution.shuffle())
# Output: Random permutation (e.g., [2,1,3])

print(solution.reset())
# Output: [1,2,3]

print(solution.shuffle())
# Output: Random permutation (e.g., [3,2,1])

print(solution.shuffle())
# Output: Random permutation

nums2 = [10,20,30,40]
solution2 = Solution(nums2)

print(solution2.shuffle())
# Output: Random permutation

print(solution2.reset())
# Output: [10,20,30,40]

print(solution2.shuffle())
# Output: Random permutation
