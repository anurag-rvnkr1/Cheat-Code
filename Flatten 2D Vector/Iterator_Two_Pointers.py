'''
251. Flatten 2D Vector

Design an iterator to flatten a 2D vector. It should support the operations:

    - next() -> Returns the next element in the 2D vector.
    - hasNext() -> Returns True if there are still elements remaining.

Implement the Vector2D class:

    - Vector2D(vec) Initializes the object with the 2D vector vec.
    - next() Returns the next element from the 2D vector.
    - hasNext() Returns True if there are more elements to iterate over.

Example 1:
    Input:
        vec = [[1,2],[3],[4]]

        hasNext()
        next()
        next()
        next()
        hasNext()
        next()
        hasNext()

    Output:
        True
        1
        2
        3
        True
        4
        False

Explanation:
    The iterator returns elements in row-major order:
    [1,2,3,4]

Example 2:
    Input:
        vec = [[],[1],[],[2,3],[]]

    Output:
        1, 2, 3

Constraints:
    0 <= vec.length <= 200
    0 <= vec[i].length <= 500
    -500 <= vec[i][j] <= 500
    At most 10^5 calls will be made to next() and hasNext().
'''

# Iterator + Two Pointers

from typing import List


class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.row = 0
        self.col = 0
        self._advance()

    def _advance(self) -> None:
        # Skip empty rows.
        while self.row < len(self.vec) and self.col == len(self.vec[self.row]):
            self.row += 1
            self.col = 0

    def next(self) -> int:
        value = self.vec[self.row][self.col]
        self.col += 1
        self._advance()
        return value

    def hasNext(self) -> bool:
        return self.row < len(self.vec)


# Example usage

# Example 1
vec1 = [[1, 2], [3], [4]]
iterator1 = Vector2D(vec1)

output1 = []
while iterator1.hasNext():
    output1.append(iterator1.next())

print(output1)
# Output: [1, 2, 3, 4]

# Example 2
vec2 = [[], [1], [], [2, 3], []]
iterator2 = Vector2D(vec2)

output2 = []
while iterator2.hasNext():
    output2.append(iterator2.next())

print(output2)
# Output: [1, 2, 3]

# Example 3
vec3 = [[], [], []]
iterator3 = Vector2D(vec3)

print(iterator3.hasNext())
# Output: False

# Example 4
vec4 = [[5], [6, 7], [8, 9, 10]]
iterator4 = Vector2D(vec4)

output4 = []
while iterator4.hasNext():
    output4.append(iterator4.next())

print(output4)
# Output: [5, 6, 7, 8, 9, 10]
