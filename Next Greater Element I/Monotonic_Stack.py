'''
496. Next Greater Element I

The next greater element of an element x in nums1 is the first greater element
to its right in nums2.

If no greater element exists, return -1.

Example 1:
    Input:
        nums1 = [4,1,2]
        nums2 = [1,3,4,2]

    Output:
        [-1,3,-1]

Example 2:
    Input:
        nums1 = [2,4]
        nums2 = [1,2,3,4]

    Output:
        [3,-1]

Constraints:
    1 <= nums1.length <= nums2.length <= 1000
    All integers in nums1 and nums2 are unique.
    nums1 is a subset of nums2.
'''

# Monotonic Stack

from typing import List


class Solution:
    def nextGreaterElement(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> List[int]:

        stack = []
        next_greater = {}

        # Build mapping for nums2.
        for number in nums2:
            while stack and stack[-1] < number:
                next_greater[stack.pop()] = number

            stack.append(number)

        while stack:
            next_greater[stack.pop()] = -1

        return [next_greater[number] for number in nums1]


# Example usage
solution = Solution()

# Example 1
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(solution.nextGreaterElement(nums1, nums2))
# Output: [-1,3,-1]

# Example 2
nums3 = [2,4]
nums4 = [1,2,3,4]
print(solution.nextGreaterElement(nums3, nums4))
# Output: [3,-1]

# Example 3
nums5 = [1,3,5]
nums6 = [6,5,4,3,2,1,7]
print(solution.nextGreaterElement(nums5, nums6))
# Output: [7,7,7]

# Example 4
nums7 = [2]
nums8 = [2]
print(solution.nextGreaterElement(nums7, nums8))
# Output: [-1]

# Example 5
nums9 = [3,1]
nums10 = [1,2,3,4]
print(solution.nextGreaterElement(nums9, nums10))
# Output: [4,2]

# Example 6
nums11 = [5,2,8]
nums12 = [2,5,1,8,9]
print(solution.nextGreaterElement(nums11, nums12))
# Output: [8,8,9]
