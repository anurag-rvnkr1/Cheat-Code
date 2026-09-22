'''
373. Find K Pairs with Smallest Sums

You are given two sorted integer arrays nums1 and nums2 and an integer k.

Return the k pairs (u, v) consisting of one element from nums1 and one element
from nums2 with the smallest sums.

Example 1:
    Input:
        nums1 = [1,7,11]
        nums2 = [2,4,6]
        k = 3

    Output:
        [[1,2],[1,4],[1,6]]

Example 2:
    Input:
        nums1 = [1,1,2]
        nums2 = [1,2,3]
        k = 2

    Output:
        [[1,1],[1,1]]

Constraints:
    1 <= nums1.length, nums2.length <= 10^5
    -10^9 <= nums1[i], nums2[i] <= 10^9
    nums1 and nums2 are sorted in ascending order.
    1 <= k <= 10^4
'''

# Min Heap + BFS

from typing import List
import heapq


class Solution:
    def kSmallestPairs(
        self,
        nums1: List[int],
        nums2: List[int],
        k: int
    ) -> List[List[int]]:

        if not nums1 or not nums2 or k == 0:
            return []

        heap = []

        # Initialize heap with pairs (nums1[i], nums2[0]).
        for i in range(min(len(nums1), k)):
            heapq.heappush(
                heap,
                (nums1[i] + nums2[0], i, 0)
            )

        result = []

        while heap and len(result) < k:
            _, i, j = heapq.heappop(heap)

            result.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(
                    heap,
                    (
                        nums1[i] + nums2[j + 1],
                        i,
                        j + 1
                    )
                )

        return result


# Example usage
solution = Solution()

# Example 1
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(solution.kSmallestPairs(nums1, nums2, k))
# Output: [[1,2],[1,4],[1,6]]

# Example 2
nums3 = [1,1,2]
nums4 = [1,2,3]
k2 = 2
print(solution.kSmallestPairs(nums3, nums4, k2))
# Output: [[1,1],[1,1]]

# Example 3
nums5 = [1,2]
nums6 = [3]
k3 = 3
print(solution.kSmallestPairs(nums5, nums6, k3))
# Output: [[1,3],[2,3]]

# Example 4
nums7 = [1,2,4,5]
nums8 = [1,2,3]
k4 = 5
print(solution.kSmallestPairs(nums7, nums8, k4))
# Output: [[1,1],[2,1],[1,2],[2,2],[1,3]]

# Example 5
nums9 = [-2,-1,0]
nums10 = [3,4]
k5 = 4
print(solution.kSmallestPairs(nums9, nums10, k5))
# Output: [[-2,3],[-1,3],[-2,4],[0,3]]

# Example 6
nums11 = [5,10,15]
nums12 = [1,2,3]
k6 = 6
print(solution.kSmallestPairs(nums11, nums12, k6))
# Output: [[5,1],[5,2],[5,3],[10,1],[10,2],[10,3]]
