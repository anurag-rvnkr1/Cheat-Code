'''
80. Remove Duplicates from Sorted Array II

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:
    int[] nums = [...];
    int[] expectedNums = [...];

    int k = removeDuplicates(nums);

    assert k == expectedNums.length;
    for (int i = 0; i < k; i++) {
        assert nums[i] == expectedNums[i];
    }

Example 1:
    Input: nums = [1,1,1,2,2,3]
    Output: 5, nums = [1,1,2,2,3,_]
    Explanation:
    The first five elements of nums become [1,1,2,2,3].

Example 2:
    Input: nums = [0,0,1,1,1,1,2,3,3]
    Output: 7, nums = [0,0,1,1,2,3,3,_,_]
    Explanation:
    The first seven elements of nums become [0,0,1,1,2,3,3].

Constraints:
    1 <= nums.length <= 3 * 10^4
    -10^4 <= nums[i] <= 10^4
    nums is sorted in non-decreasing order.
'''

# Two Pointers (Allow At Most Twice)
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        write = 0

        for num in nums:

            if write < 2 or num != nums[write - 2]:
                nums[write] = num
                write += 1

        return write


# Example usage
solution = Solution()

nums1 = [1, 1, 1, 2, 2, 3]
k1 = solution.removeDuplicates(nums1)
print(k1, nums1[:k1])  # Output: 5 [1,1,2,2,3]

nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
k2 = solution.removeDuplicates(nums2)
print(k2, nums2[:k2])  # Output: 7 [0,0,1,1,2,3,3]
