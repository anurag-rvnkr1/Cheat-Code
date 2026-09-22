'''
480. Sliding Window Median

Given an integer array nums and an integer k, there is a sliding window of size k
moving from the left of the array to the right. Return the median of each window.

Median Rules:
    - If k is odd, median is the middle element.
    - If k is even, median is the average of the two middle elements.

Example 1:
    Input:
        nums = [1,3,-1,-3,5,3,6,7]
        k = 3

    Output:
        [1,-1,-1,3,5,6]

Example 2:
    Input:
        nums = [1,2]
        k = 1

    Output:
        [1,2]

Constraints:
    1 <= nums.length <= 10^5
    -2^31 <= nums[i] <= 2^31 - 1
    1 <= k <= nums.length
'''

# Heap + Sliding Window + Lazy Deletion

from typing import List
import heapq
from collections import defaultdict


class DualHeap:
    def __init__(self, k: int):
        self.small = []                     # Max Heap (negative values)
        self.large = []                     # Min Heap
        self.delayed = defaultdict(int)

        self.small_size = 0
        self.large_size = 0
        self.k = k

    # Remove invalid elements from heap top.
    def prune(self, heap):
        while heap:
            num = -heap[0] if heap is self.small else heap[0]

            if self.delayed[num]:
                self.delayed[num] -= 1

                if self.delayed[num] == 0:
                    del self.delayed[num]

                heapq.heappop(heap)
            else:
                break

    # Keep heap sizes balanced.
    def make_balance(self):
        if self.small_size > self.large_size + 1:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

            self.small_size -= 1
            self.large_size += 1

            self.prune(self.small)

        elif self.small_size < self.large_size:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

            self.large_size -= 1
            self.small_size += 1

            self.prune(self.large)

    def insert(self, num: int):
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_size += 1
        else:
            heapq.heappush(self.large, num)
            self.large_size += 1

        self.make_balance()

    def erase(self, num: int):
        self.delayed[num] += 1

        if num <= -self.small[0]:
            self.small_size -= 1

            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.large_size -= 1

            if self.large and num == self.large[0]:
                self.prune(self.large)

        self.make_balance()

    def get_median(self):
        if self.k % 2 == 1:
            return float(-self.small[0])

        return (-self.small[0] + self.large[0]) / 2.0


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        dual_heap = DualHeap(k)

        # First window.
        for index in range(k):
            dual_heap.insert(nums[index])

        answer = [dual_heap.get_median()]

        for index in range(k, len(nums)):
            dual_heap.insert(nums[index])
            dual_heap.erase(nums[index - k])

            answer.append(dual_heap.get_median())

        return answer


# Example usage
solution = Solution()

# Example 1
nums1 = [1,3,-1,-3,5,3,6,7]
print(solution.medianSlidingWindow(nums1, 3))
# Output: [1,-1,-1,3,5,6]

# Example 2
nums2 = [1,2]
print(solution.medianSlidingWindow(nums2, 1))
# Output: [1,2]

# Example 3
nums3 = [1,4,2,3]
print(solution.medianSlidingWindow(nums3, 4))
# Output: [2.5]

# Example 4
nums4 = [5,2,2,7,3,7,9,0,2,3]
print(solution.medianSlidingWindow(nums4, 2))
# Output: [3.5,2.0,4.5,5.0,5.0,8.0,4.5,1.0,2.5]

# Example 5
nums5 = [1,1,1,1,1]
print(solution.medianSlidingWindow(nums5, 3))
# Output: [1,1,1]

# Example 6
nums6 = [-5,-3,-1,0,2,4]
print(solution.medianSlidingWindow(nums6, 2))
# Output: [-4.0,-2.0,-0.5,1.0,3.0]
