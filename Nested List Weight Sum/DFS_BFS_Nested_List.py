'''
339. Nested List Weight Sum

You are given a nested list of integers nestedList.

Each element is either:
    - An integer.
    - A list whose elements may also be integers or other lists.

The depth of an integer is the number of lists inside which it is nested.

Return the sum of each integer multiplied by its depth.

Example 1:
    Input:
        nestedList = [[1,1],2,[1,1]]

    Output:
        10

Explanation:
        Four 1's at depth 2 -> 4 * 2 = 8
        One 2 at depth 1 -> 2 * 1 = 2
        Total = 10

Example 2:
    Input:
        nestedList = [1,[4,[6]]]

    Output:
        27

Explanation:
        1 * 1 + 4 * 2 + 6 * 3 = 27

Constraints:
    1 <= nestedList.length <= 50
    The values of integers are in the range [-100, 100].
    Maximum nesting depth is at most 50.
'''

# DFS (Depth-First Search)

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
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        def dfs(current_list: List[NestedInteger], depth: int) -> int:
            total = 0

            for item in current_list:
                if item.isInteger():
                    total += item.getInteger() * depth
                else:
                    total += dfs(item.getList(), depth + 1)

            return total

        return dfs(nestedList, 1)
