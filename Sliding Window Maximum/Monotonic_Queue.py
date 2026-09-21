'''
239. Sliding Window Maximum

You are given an array of integers nums, and there is a sliding window of size k
which is moving from the very left of the array to the very right.

You can only see the k numbers in the window. Each time the sliding window moves
right by one position.

Return the maximum value in each sliding window.

Example 1:
    Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [3,3,5,5,6,7]

Explanation:
    Window Position                Max
    ---------------               -----
    [1  3 -1] -3  5  3  6  7        3
     1 [3 -1 -3] 5  3  6  7         3
     1  3 [-1 -3 5] 3  6  7         5
     1  3 -1 [-3 5 3] 6  7          5
     1  3 -1 -3 [5 3 6] 7           6
     1  3 -1 -3 5 [3 6 7]           7

Example 2:
    Input: nums = [1], k = 1
    Output: [1]

Constraints:
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    1 <= k <= nums.length
'''

# Monotonic Queue (Deque)

from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()   # Stores indices.
        result = []

        for i in range(len(nums)):

            # Remove indices outside the current window.
            while window and window[0] <= i - k:
                window.popleft()

            # Maintain decreasing order in deque.
            while window and nums[window[-1]] <= nums[i]:
                window.pop()

            window.append(i)

            # First complete window starts at index k - 1.
            if i >= k - 1:
                result.append(nums[window[0]])

        return result


# Example usage
solution = Solution()

# Example 1
nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
k1 = 3
print(solution.maxSlidingWindow(nums1, k1))
# Output: [3, 3, 5, 5, 6, 7]

# Example 2
nums2 = [1]
k2 = 1
print(solution.maxSlidingWindow(nums2, k2))
# Output: [1]

# Example 3
nums3 = [9, 11]
k3 = 2
print(solution.maxSlidingWindow(nums3, k3))
# Output: [11]

# Example 4
nums4 = [4, -2]
k4 = 2
print(solution.maxSlidingWindow(nums4, k4))
# Output: [4]
