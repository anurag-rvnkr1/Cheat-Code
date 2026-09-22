'''
327. Count of Range Sum

Given an integer array nums and two integers lower and upper,
return the number of range sums that lie in [lower, upper].

Range sum S(i, j) is the sum of nums[i...j] where i <= j.

Example 1:
    Input:
        nums = [-2,5,-1]
        lower = -2
        upper = 2

    Output:
        3

Explanation:
    Valid range sums are:
        [-2]
        [-1]
        [-2,5,-1] = 2

Example 2:
    Input:
        nums = [0]
        lower = 0
        upper = 0

    Output:
        1

Constraints:
    1 <= nums.length <= 10^5
    -2^31 <= nums[i] <= 2^31 - 1
    -10^5 <= lower <= upper <= 10^5
'''

# Prefix Sum + Modified Merge Sort

from typing import List


class Solution:
    def countRangeSum(
        self,
        nums: List[int],
        lower: int,
        upper: int
    ) -> int:

        # ---------- Prefix Sum ----------
        prefix = [0]

        for number in nums:
            prefix.append(prefix[-1] + number)

        # ---------- Merge Sort ----------
        def merge_sort(left: int, right: int) -> int:

            if right - left <= 1:
                return 0

            middle = (left + right) // 2

            count = (
                merge_sort(left, middle)
                + merge_sort(middle, right)
            )

            # Count valid pairs.
            start = end = middle

            for i in range(left, middle):

                while (
                    start < right and
                    prefix[start] - prefix[i] < lower
                ):
                    start += 1

                while (
                    end < right and
                    prefix[end] - prefix[i] <= upper
                ):
                    end += 1

                count += end - start

            # Merge sorted halves.
            merged = []
            p1 = left
            p2 = middle

            while p1 < middle and p2 < right:
                if prefix[p1] <= prefix[p2]:
                    merged.append(prefix[p1])
                    p1 += 1
                else:
                    merged.append(prefix[p2])
                    p2 += 1

            merged.extend(prefix[p1:middle])
            merged.extend(prefix[p2:right])

            prefix[left:right] = merged

            return count

        return merge_sort(0, len(prefix))


# Example usage
solution = Solution()

# Example 1
nums1 = [-2, 5, -1]
lower1 = -2
upper1 = 2

print(solution.countRangeSum(nums1, lower1, upper1))
# Output: 3

# Example 2
nums2 = [0]
lower2 = 0
upper2 = 0

print(solution.countRangeSum(nums2, lower2, upper2))
# Output: 1

# Example 3
nums3 = [1, -1, 2]
lower3 = 0
upper3 = 2

print(solution.countRangeSum(nums3, lower3, upper3))
# Output: 5

# Example 4
nums4 = [3, -2, 4, -1]
lower4 = 2
upper4 = 5

print(solution.countRangeSum(nums4, lower4, upper4))
# Output: 6

# Example 5
nums5 = [-3, 1, 2, -2, 2]
lower5 = -2
upper5 = 2

print(solution.countRangeSum(nums5, lower5, upper5))
# Output: 11
