'''
321. Create Maximum Number

You are given two integer arrays nums1 and nums2 of digits (0-9).

Create the maximum number of length k from digits of the two arrays.

Rules:
    - Preserve the relative order of digits taken from each array.
    - Choose digits from both arrays.
    - Return the lexicographically largest possible sequence of length k.

Example 1:
    Input:
        nums1 = [3,4,6,5]
        nums2 = [9,1,2,5,8,3]
        k = 5

    Output:
        [9,8,6,5,3]

Example 2:
    Input:
        nums1 = [6,7]
        nums2 = [6,0,4]
        k = 5

    Output:
        [6,7,6,0,4]

Example 3:
    Input:
        nums1 = [3,9]
        nums2 = [8,9]
        k = 3

    Output:
        [9,8,9]

Constraints:
    1 <= nums1.length, nums2.length <= 500
    0 <= nums1[i], nums2[i] <= 9
    1 <= k <= nums1.length + nums2.length
'''

# Monotonic Stack + Greedy + Merge

from typing import List


class Solution:

    def createMaximumNumber(
        self,
        nums1: List[int],
        nums2: List[int],
        k: int
    ) -> List[int]:

        # Pick the largest subsequence of length size.
        def max_subsequence(nums: List[int], size: int) -> List[int]:
            stack = []
            remove = len(nums) - size

            for digit in nums:
                while remove and stack and stack[-1] < digit:
                    stack.pop()
                    remove -= 1

                stack.append(digit)

            return stack[:size]

        # Merge two subsequences into the largest lexicographical sequence.
        def merge(seq1: List[int], seq2: List[int]) -> List[int]:
            result = []

            i = 0
            j = 0

            while i < len(seq1) or j < len(seq2):

                # Lexicographical comparison of remaining suffixes.
                if seq1[i:] > seq2[j:]:
                    result.append(seq1[i])
                    i += 1
                else:
                    result.append(seq2[j])
                    j += 1

            return result

        answer = []

        start = max(0, k - len(nums2))
        end = min(k, len(nums1))

        for take_from_nums1 in range(start, end + 1):

            take_from_nums2 = k - take_from_nums1

            subsequence1 = max_subsequence(nums1, take_from_nums1)
            subsequence2 = max_subsequence(nums2, take_from_nums2)

            candidate = merge(subsequence1, subsequence2)

            answer = max(answer, candidate)

        return answer


# Example usage
solution = Solution()

# Example 1
nums1 = [3,4,6,5]
nums2 = [9,1,2,5,8,3]
k = 5

print(solution.createMaximumNumber(nums1, nums2, k))
# Output: [9,8,6,5,3]

# Example 2
nums1 = [6,7]
nums2 = [6,0,4]
k = 5

print(solution.createMaximumNumber(nums1, nums2, k))
# Output: [6,7,6,0,4]

# Example 3
nums1 = [3,9]
nums2 = [8,9]
k = 3

print(solution.createMaximumNumber(nums1, nums2, k))
# Output: [9,8,9]

# Example 4
nums1 = [5,6]
nums2 = [7,8]
k = 3

print(solution.createMaximumNumber(nums1, nums2, k))
# Output: [8,5,6]

# Example 5
nums1 = [2,5,6,4,4,0]
nums2 = [7,3,8,0,6,5,7,6,2]
k = 8

print(solution.createMaximumNumber(nums1, nums2, k))
# Output: [8,7,6,5,6,4,4,0]
