'''
350. Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection.

Each element in the result should appear as many times as it appears in both arrays,
and you may return the result in any order.

Example 1:
    Input:
        nums1 = [1,2,2,1]
        nums2 = [2,2]

    Output:
        [2,2]

Example 2:
    Input:
        nums1 = [4,9,5]
        nums2 = [9,4,9,8,4]

    Output:
        [4,9]

Constraints:
    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 1000

Follow-up:
    - What if the arrays are already sorted?
    - What if nums1 is much smaller than nums2?
    - What if nums2 is stored on disk and memory is limited?
'''

# HashMap Frequency Counting

from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        frequency = Counter(nums1)

        result = []

        for number in nums2:
            if frequency[number] > 0:
                result.append(number)
                frequency[number] -= 1

        return result


# Example usage
solution = Solution()

# Example 1
nums1 = [1,2,2,1]
nums2 = [2,2]
print(solution.intersect(nums1, nums2))
# Output: [2,2]

# Example 2
nums3 = [4,9,5]
nums4 = [9,4,9,8,4]
print(solution.intersect(nums3, nums4))
# Output: [4,9]

# Example 3
nums5 = [1,2,2,3]
nums6 = [2,2,2]
print(solution.intersect(nums5, nums6))
# Output: [2,2]

# Example 4
nums7 = [5,5,5,6]
nums8 = [5,5,7]
print(solution.intersect(nums7, nums8))
# Output: [5,5]

# Example 5
nums9 = [10,20,30]
nums10 = [40,50,60]
print(solution.intersect(nums9, nums10))
# Output: []

# Example 6
nums11 = [3,1,2]
nums12 = [1,1]
print(solution.intersect(nums11, nums12))
# Output: [1]
