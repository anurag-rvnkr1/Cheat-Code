'''
215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element
in the array.

Note:
    It is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:
    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5

Example 2:
    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4

Constraints:
    1 <= k <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
'''

# Heap (Min Heap)

from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)

            # Keep only k largest elements in the heap.
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]


# Example usage
solution = Solution()

# Example 1
nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2
print(solution.findKthLargest(nums1, k1))  # Output: 5

# Example 2
nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 4
print(solution.findKthLargest(nums2, k2))  # Output: 4

# Example 3
nums3 = [1]
k3 = 1
print(solution.findKthLargest(nums3, k3))  # Output: 1

# Example 4
nums4 = [7, 10, 4, 3, 20, 15]
k4 = 3
print(solution.findKthLargest(nums4, k4))  # Output: 10
