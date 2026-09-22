'''
324. Wiggle Sort II

Given an integer array nums, reorder it such that:

    nums[0] < nums[1] > nums[2] < nums[3] ...

You must rearrange the array in-place.

Example 1:
    Input:
        nums = [1,5,1,1,6,4]

    Output:
        [1,6,1,5,1,4]

Example 2:
    Input:
        nums = [1,3,2,2,3,1]

    Output:
        [2,3,1,3,1,2]

Constraints:
    1 <= nums.length <= 5 * 10^4
    0 <= nums[i] <= 5000

Follow-up:
    Can you solve it in O(n) time and/or O(1) extra space?
'''

# Quick Select + Dutch National Flag + Virtual Indexing

from typing import List
import random


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything.
        Modify nums in-place.
        """

        n = len(nums)

        # ---------- Quick Select to Find Median ----------
        def quick_select(left: int, right: int, k: int) -> int:
            if left == right:
                return nums[left]

            pivot_index = random.randint(left, right)
            pivot = nums[pivot_index]

            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            store = left

            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store], nums[i] = nums[i], nums[store]
                    store += 1

            nums[store], nums[right] = nums[right], nums[store]

            if store == k:
                return nums[store]

            if store < k:
                return quick_select(store + 1, right, k)

            return quick_select(left, store - 1, k)

        median = quick_select(0, n - 1, n // 2)

        # ---------- Virtual Index Mapping ----------
        def virtual_index(i: int) -> int:
            return (1 + 2 * i) % (n | 1)

        left = 0
        current = 0
        right = n - 1

        # ---------- Dutch National Flag Partition ----------
        while current <= right:

            mapped_current = virtual_index(current)

            if nums[mapped_current] > median:

                mapped_left = virtual_index(left)

                nums[mapped_left], nums[mapped_current] = (
                    nums[mapped_current],
                    nums[mapped_left]
                )

                left += 1
                current += 1

            elif nums[mapped_current] < median:

                mapped_right = virtual_index(right)

                nums[mapped_current], nums[mapped_right] = (
                    nums[mapped_right],
                    nums[mapped_current]
                )

                right -= 1

            else:
                current += 1


# Example usage
solution = Solution()

# Example 1
nums1 = [1,5,1,1,6,4]
solution.wiggleSort(nums1)
print(nums1)
# Possible Output: [1,6,1,5,1,4]

# Example 2
nums2 = [1,3,2,2,3,1]
solution.wiggleSort(nums2)
print(nums2)
# Possible Output: [2,3,1,3,1,2]

# Example 3
nums3 = [4,5,5,6]
solution.wiggleSort(nums3)
print(nums3)
# Possible Output: [5,6,4,5]

# Example 4
nums4 = [1,1,2,1,2,2,1]
solution.wiggleSort(nums4)
print(nums4)
# Valid wiggle ordering.

# Example 5
nums5 = [2,2,2,1,1,1]
solution.wiggleSort(nums5)
print(nums5)
# Valid wiggle ordering.
