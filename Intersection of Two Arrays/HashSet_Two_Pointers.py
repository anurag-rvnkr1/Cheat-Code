'''
349. Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection.

Each element in the result must be unique, and you may return the result
in any order.

Example 1:
    Input:
        nums1 = [1,2,2,1]
        nums2 = [2,2]

    Output:
        [2]

Example 2:
    Input:
        nums1 = [4,9,5]
        nums2 = [9,4,9,8,4]

    Output:
        [9,4]

Constraints:
    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 1000
'''

# HashSet

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


# Example usage
solution = Solution()

# Example 1
nums1 = [1,2,2,1]
nums2 = [2,2]
print(solution.intersection(nums1, nums2))
# Output: [2]

# Example 2
nums3 = [4,9,5]
nums4 = [9,4,9,8,4]
print(solution.intersection(nums3, nums4))
# Output: [9,4]

# Example 3
nums5 = [1,3,5,7]
nums6 = [2,4,6,8]
print(solution.intersection(nums5, nums6))
# Output: []

# Example 4
nums7 = [1,1,2,3,4]
nums8 = [2,2,4,4]
print(solution.intersection(nums7, nums8))
# Output: [2,4]

# Example 5
nums9 = [10,20,30]
nums10 = [30,40,50]
print(solution.intersection(nums9, nums10))
# Output: [30]

# Example 6
nums11 = [5]
nums12 = [5]
print(solution.intersection(nums11, nums12))
# Output: [5]
