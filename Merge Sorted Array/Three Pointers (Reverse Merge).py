'''
88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored.

Example 1:
    Input:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    Explanation:
        The arrays being merged are [1,2,3] and [2,5,6].

Example 2:
    Input:
        nums1 = [1], m = 1
        nums2 = [], n = 0
    Output: [1]

Example 3:
    Input:
        nums1 = [0], m = 0
        nums2 = [1], n = 1
    Output: [1]
    Explanation:
        nums1 initially has no valid elements. The trailing 0 is placeholder space.

Constraints:
    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -10^9 <= nums1[i], nums2[j] <= 10^9
'''

# Three Pointers (Reverse Merge)
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:

            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1

            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        # Copy remaining elements from nums2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


# Example usage
solution = Solution()

nums1 = [1, 2, 3, 0, 0, 0]
solution.merge(nums1, 3, [2, 5, 6], 3)
print(nums1)  # Output: [1,2,2,3,5,6]

nums2 = [1]
solution.merge(nums2, 1, [], 0)
print(nums2)  # Output: [1]

nums3 = [0]
solution.merge(nums3, 0, [1], 1)
print(nums3)  # Output: [1]
