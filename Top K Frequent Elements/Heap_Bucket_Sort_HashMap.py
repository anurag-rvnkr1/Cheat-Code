'''
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements.

You may return the answer in any order.

Example 1:
    Input:
        nums = [1,1,1,2,2,3]
        k = 2

    Output:
        [1,2]

Example 2:
    Input:
        nums = [1]
        k = 1

    Output:
        [1]

Example 3:
    Input:
        nums = [4,4,4,6,6,1,1,1,2]
        k = 2

    Output:
        [4,1]

Constraints:
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    k is in the range [1, number of unique elements].
    It is guaranteed that the answer is unique.

Follow-up:
    Your algorithm's time complexity must be better than O(n log n).
'''

# Bucket Sort + HashMap (Optimal O(n))

from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)

        # bucket[i] contains numbers appearing exactly i times.
        bucket = [[] for _ in range(len(nums) + 1)]

        for number, count in frequency.items():
            bucket[count].append(number)

        result = []

        # Traverse frequencies from highest to lowest.
        for count in range(len(bucket) - 1, 0, -1):
            for number in bucket[count]:
                result.append(number)

                if len(result) == k:
                    return result

        return result


# Example usage
solution = Solution()

# Example 1
nums1 = [1,1,1,2,2,3]
k1 = 2
print(solution.topKFrequent(nums1, k1))
# Output: [1,2]

# Example 2
nums2 = [1]
k2 = 1
print(solution.topKFrequent(nums2, k2))
# Output: [1]

# Example 3
nums3 = [4,4,4,6,6,1,1,1,2]
k3 = 2
print(solution.topKFrequent(nums3, k3))
# Output: [4,1]

# Example 4
nums4 = [5,5,6,6,6,7,7,8]
k4 = 3
print(solution.topKFrequent(nums4, k4))
# Output: [6,5,7]

# Example 5
nums5 = [9,9,9,8,8,7,7,7,7]
k5 = 2
print(solution.topKFrequent(nums5, k5))
# Output: [7,9]

# Example 6
nums6 = [3,0,1,0]
k6 = 1
print(solution.topKFrequent(nums6, k6))
# Output: [0]
