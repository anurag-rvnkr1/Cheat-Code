'''
274. H-Index

Given an array of integers citations where citations[i] is the number of
citations a researcher received for their ith paper, return the researcher's
H-index.

According to the definition of H-index:

    A researcher has an index h if h of their papers have at least h citations each,
    and the remaining papers have no more than h citations each.

If there are several possible values for h, return the maximum one.

Example 1:
    Input: citations = [3,0,6,1,5]
    Output: 3

Explanation:
    The researcher has 5 papers.
    3 papers have at least 3 citations each.

Example 2:
    Input: citations = [1,3,1]
    Output: 1

Constraints:
    n == citations.length
    1 <= n <= 5000
    0 <= citations[i] <= 1000
'''

# Sorting + Array

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        h_index = 0

        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h_index = i + 1
            else:
                break

        return h_index


# Example usage
solution = Solution()

# Example 1
citations1 = [3, 0, 6, 1, 5]
print(solution.hIndex(citations1))
# Output: 3

# Example 2
citations2 = [1, 3, 1]
print(solution.hIndex(citations2))
# Output: 1

# Example 3
citations3 = [10, 8, 5, 4, 3]
print(solution.hIndex(citations3))
# Output: 4

# Example 4
citations4 = [25, 8, 5, 3, 3]
print(solution.hIndex(citations4))
# Output: 3

# Example 5
citations5 = [0, 0, 0, 0]
print(solution.hIndex(citations5))
# Output: 0
