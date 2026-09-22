'''
341. Flatten Nested List Iterator

You are given a nested list of integers nestedList.

Each element is either:
    - An integer.
    - A list whose elements may also be integers or other lists.

Implement an iterator to flatten the nested list.

Implement the NestedIterator class:

    NestedIterator(List[NestedInteger] nestedList)
        Initializes the iterator.

    int next()
        Returns the next integer in the nested list.

    boolean hasNext()
        Returns True if there are still integers remaining.

Example 1:
    Input:
        nestedList = [[1,1],2,[1,1]]

    Output:
        [1,1,2,1,1]

Example 2:
    Input:
        nestedList = [1,[4,[6]]]

    Output:
        [1,4,6]

Constraints:
    1 <= nestedList.length <= 500
    The values of integers are in the range [-10^6, 10^6].
'''

# Stack + Iterator Design

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


class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        # Stack stores NestedInteger objects in reverse order.
        self.stack = nestedList[::-1]

    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]

            if top.isInteger():
                return True

            self.stack.pop()

            nested = top.getList()

            # Push children in reverse order.
            self.stack.extend(nested[::-1])

        return False


# Example usage on LeetCode:
#
# iterator = NestedIterator(nestedList)
#
# result = []
# while iterator.hasNext():
#     result.append(iterator.next())
#
# print(result)
#
# Example Output:
# [1,1,2,1,1]
