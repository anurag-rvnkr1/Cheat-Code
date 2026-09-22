'''
385. Mini Parser

Given a string s representing a nested list of integers, implement a parser
to deserialize it into a NestedInteger object.

Each element is either:
    - An integer.
    - A list containing integers or other lists.

Example 1:
    Input:
        s = "324"

    Output:
        NestedInteger(324)

Example 2:
    Input:
        s = "[123,[456,[789]]]"

    Output:
        NestedInteger([123,[456,[789]]])

Constraints:
    1 <= s.length <= 5 * 10^4
    s consists of digits, '-', '[', ']', and ','.
    s is a valid NestedInteger representation.
'''

# Stack + String Parsing

from typing import List


# This is the interface provided by LeetCode.
# Do not implement it.
class NestedInteger:

    def __init__(self, value=None):
        pass

    def isInteger(self) -> bool:
        pass

    def add(self, elem: 'NestedInteger') -> None:
        pass

    def setInteger(self, value: int) -> None:
        pass

    def getInteger(self) -> int:
        pass

    def getList(self) -> List['NestedInteger']:
        pass


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # Single integer.
        if s[0] != "[":
            return NestedInteger(int(s))

        stack = []
        number = ""
        current = None

        for character in s:

            if character == "[":
                nested = NestedInteger()

                if current is not None:
                    stack.append(current)
                    current.add(nested)

                current = nested

            elif character == "]":

                if number:
                    current.add(NestedInteger(int(number)))
                    number = ""

                if stack:
                    parent = stack.pop()
                    current = parent

            elif character == ",":
                if number:
                    current.add(NestedInteger(int(number)))
                    number = ""

            else:
                number += character

        return current


# Example usage on LeetCode:
#
# solution = Solution()
#
# result1 = solution.deserialize("324")
# result2 = solution.deserialize("[123,[456,[789]]]")
#
# Output:
# NestedInteger(324)
# NestedInteger([123,[456,[789]]])
