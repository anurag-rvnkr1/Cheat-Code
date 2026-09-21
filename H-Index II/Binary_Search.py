'''
275. H-Index II

Given an array of integers citations where citations[i] is the number of
citations a researcher received for their ith paper.

The citations array is sorted in ascending order.

Return the researcher's H-index.

According to the definition of H-index:

    A researcher has an index h if h of their papers have at least h citations each,
    and the remaining papers have no more than h citations each.

Example 1:
    Input: citations = [0,1,3,5,6]
    Output: 3

Explanation:
    There are 5 papers in total.
    3 papers have at least 3 citations each.

Example 2:
    Input: citations = [1,2,100]
    Output: 2

Constraints:
    n == citations.length
    1 <= n <= 10^5
    0 <= citations[i] <= 1000
    citations is sorted in ascending order.

Follow-up:
    Can you solve it in logarithmic time complexity?
'''

# Binary Search

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            papers_with_at_least_this_citation = n - mid

            if citations[mid] == papers_with_at_least_this_citation:
                return citations[mid]

            elif citations[mid] < papers_with_at_least_this_citation:
                left = mid + 1

            else:
                right = mid - 1

        return n - left

# Example usage
solution = Solution()

# Example 1
citations1 = [0, 1, 3, 5, 6]
print(solution.hIndex(citations1))
# Output: 3

# Example 2
citations2 = [1, 2, 100]
print(solution.hIndex(citations2))
# Output: 2

# Example 3
citations3 = [0, 0, 0, 5, 5]
print(solution.hIndex(citations3))
# Output: 2

# Example 4
citations4 = [0, 1, 2, 3, 4]
print(solution.hIndex(citations4))
# Output: 2

# Example 5
citations5 = [100]
print(solution.hIndex(citations5))
# Output: 1
