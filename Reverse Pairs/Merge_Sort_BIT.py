'''
493. Reverse Pairs

Given an integer array nums, return the number of reverse pairs.

A reverse pair is defined as:

    i < j
    nums[i] > 2 * nums[j]

Example 1:
    Input:
        nums = [1,3,2,3,1]

    Output:
        2

Explanation:
        Reverse pairs:
        (3,1)
        (3,1)

Example 2:
    Input:
        nums = [2,4,3,5,1]

    Output:
        3

Constraints:
    1 <= nums.length <= 5 * 10^4
    -2^31 <= nums[i] <= 2^31 - 1
'''

# Merge Sort + Divide and Conquer

from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(left: int, right: int) -> int:
            if left >= right:
                return 0

            middle = (left + right) // 2

            count = (
                merge_sort(left, middle) +
                merge_sort(middle + 1, right)
            )

            # Count reverse pairs.
            pointer = middle + 1

            for i in range(left, middle + 1):
                while (
                    pointer <= right and
                    nums[i] > 2 * nums[pointer]
                ):
                    pointer += 1

                count += pointer - (middle + 1)

            # Merge sorted halves.
            merged = []

            first = left
            second = middle + 1

            while first <= middle and second <= right:
                if nums[first] <= nums[second]:
                    merged.append(nums[first])
                    first += 1
                else:
                    merged.append(nums[second])
                    second += 1

            while first <= middle:
                merged.append(nums[first])
                first += 1

            while second <= right:
                merged.append(nums[second])
                second += 1

            nums[left:right + 1] = merged

            return count

        return merge_sort(0, len(nums) - 1)


# Example usage
solution = Solution()

# Example 1
nums1 = [1,3,2,3,1]
print(solution.reversePairs(nums1))
# Output: 2

# Example 2
nums2 = [2,4,3,5,1]
print(solution.reversePairs(nums2))
# Output: 3

# Example 3
nums3 = [5,4,3,2,1]
print(solution.reversePairs(nums3))
# Output: 4

# Example 4
nums4 = [1,2,3,4,5]
print(solution.reversePairs(nums4))
# Output: 0

# Example 5
nums5 = [-5,-5]
print(solution.reversePairs(nums5))
# Output: 1

# Example 6
nums6 = [2147483647,2147483647,-2147483648]
print(solution.reversePairs(nums6))
# Output: 2
