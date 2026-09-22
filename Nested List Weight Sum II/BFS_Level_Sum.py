'''
364. Nested List Weight Sum II

Given a nested list of integers nestedList, return the sum of all integers
weighted by their inverse depth.

The deepest level has weight 1.
The level above has weight 2, and so on.

Example 1:
    Input:
        nestedList = [[1,1],2,[1,1]]

    Output:
        8

Explanation:
        Four 1's at depth 2 -> weight 1
        One 2 at depth 1 -> weight 2
        Total = 8

Example 2:
    Input:
        nestedList = [1,[4,[6]]]

    Output:
        17

Explanation:
        Depths:
            1 -> weight 3
            4 -> weight 2
            6 -> weight 1

        Total = 1×3 + 4×2 + 6×1 = 17

Constraints:
    1 <= nestedList.length <= 50
    The values of integers are in the range [-100, 100].
    Maximum nesting depth is at most 50.
'''

# BFS Level Sum

from typing import List


# This is the interface provided by LeetCode.
# Do not implement it.
class NestedInteger:
    def isInteger(self) -> bool:
        pass

    def getInteger(self) -> int:
        pass

    def getList(self) -> List['NestedInteger']:
        pass


class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        unweighted_sum = 0
        weighted_sum = 0

        current_level = nestedList

        while current_level:
            next_level = []

            for item in current_level:
                if item.isInteger():
                    unweighted_sum += item.getInteger()
                else:
                    next_level.extend(item.getList())

            weighted_sum += unweighted_sum
            current_level = next_level

        return weighted_sum
