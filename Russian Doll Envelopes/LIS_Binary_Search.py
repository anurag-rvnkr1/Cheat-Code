'''
354. Russian Doll Envelopes

You are given a 2D array envelopes where envelopes[i] = [wi, hi]
represents the width and height of an envelope.

One envelope can fit into another if and only if both the width and height
of one envelope are greater than the width and height of the other envelope.

Return the maximum number of envelopes you can Russian doll.

Example 1:
    Input:
        envelopes = [[5,4],[6,4],[6,7],[2,3]]

    Output:
        3

Explanation:
        [2,3] -> [5,4] -> [6,7]

Example 2:
    Input:
        envelopes = [[1,1],[1,1],[1,1]]

    Output:
        1

Constraints:
    1 <= envelopes.length <= 10^5
    envelopes[i].length == 2
    1 <= wi, hi <= 10^5
'''

# Longest Increasing Subsequence + Binary Search

from typing import List
from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort width ascending and height descending.
        envelopes.sort(key=lambda envelope: (envelope[0], -envelope[1]))

        lis = []

        for _, height in envelopes:
            position = bisect_left(lis, height)

            if position == len(lis):
                lis.append(height)
            else:
                lis[position] = height

        return len(lis)


# Example usage
solution = Solution()

# Example 1
envelopes1 = [[5,4],[6,4],[6,7],[2,3]]
print(solution.maxEnvelopes(envelopes1))
# Output: 3

# Example 2
envelopes2 = [[1,1],[1,1],[1,1]]
print(solution.maxEnvelopes(envelopes2))
# Output: 1

# Example 3
envelopes3 = [[4,5],[4,6],[6,7],[2,3],[1,1]]
print(solution.maxEnvelopes(envelopes3))
# Output: 4

# Example 4
envelopes4 = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
print(solution.maxEnvelopes(envelopes4))
# Output: 5

# Example 5
envelopes5 = [[30,50],[12,2],[3,4],[12,15]]
print(solution.maxEnvelopes(envelopes5))
# Output: 3

# Example 6
envelopes6 = [[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]
print(solution.maxEnvelopes(envelopes6))
# Output: 3
