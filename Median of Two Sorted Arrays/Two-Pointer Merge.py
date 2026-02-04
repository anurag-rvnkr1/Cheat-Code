"""
4. Median of Two Sorted Arrays
Solved
Hard
Topics
premium lock icon
Companies
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

#Two-Pointer Merge approach
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        prev = cur = 0
        total = len(nums1) + len(nums2)

        for _ in range(total//2 + 1):
            prev = cur

            if i < len(nums1) and (j >= len(nums2) or nums1[i] < nums2[j]):
                cur = nums1[i]
                i += 1
            else:
                cur = nums2[j]
                j += 1

        if total % 2:
            return cur
        return (prev + cur) / 2
# Example usage:
solution = Solution()
print(solution.findMedianSortedArrays([1, 3], [2]))  # Output: 2.0
print(solution.findMedianSortedArrays([1, 2], [3, 4]))  # Output: 2.5
print(solution.findMedianSortedArrays([0, 0], [0, 0]))  # Output: 0.0