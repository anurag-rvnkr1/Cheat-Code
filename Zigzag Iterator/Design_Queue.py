'''
281. Zigzag Iterator

Given two vectors of integers v1 and v2, implement an iterator that returns
their elements alternately.

Implement the ZigzagIterator class:

    - ZigzagIterator(v1, v2) Initializes the object with the two vectors.
    - next() Returns the next element in the zigzag order.
    - hasNext() Returns True if there are still elements remaining.

Example 1:
    Input:
        v1 = [1,2]
        v2 = [3,4,5,6]

    Output:
        [1,3,2,4,5,6]

Explanation:
    Elements are returned alternately from each vector.
    When one vector becomes empty, continue with the remaining vector.

Example 2:
    Input:
        v1 = [1]
        v2 = []

    Output:
        [1]

Constraints:
    0 <= len(v1), len(v2) <= 1000
    1 <= len(v1) + len(v2) <= 2000

Follow-up:
    What if you are given k vectors instead of two?
'''

# Design + Queue

from typing import List
from collections import deque


class ZigzagIterator:

    def __init__(self, v1: List[int], v2: List[int]):
        # Queue stores (vector, current_index)
        self.queue = deque()

        if v1:
            self.queue.append((v1, 0))

        if v2:
            self.queue.append((v2, 0))

    def next(self) -> int:
        vector, index = self.queue.popleft()

        value = vector[index]

        # Push the vector back if elements remain.
        if index + 1 < len(vector):
            self.queue.append((vector, index + 1))

        return value

    def hasNext(self) -> bool:
        return len(self.queue) > 0


# Example usage

# Example 1
iterator1 = ZigzagIterator([1, 2], [3, 4, 5, 6])

result1 = []
while iterator1.hasNext():
    result1.append(iterator1.next())

print(result1)
# Output: [1, 3, 2, 4, 5, 6]


# Example 2
iterator2 = ZigzagIterator([1], [])

result2 = []
while iterator2.hasNext():
    result2.append(iterator2.next())

print(result2)
# Output: [1]


# Example 3
iterator3 = ZigzagIterator([], [10, 20, 30])

result3 = []
while iterator3.hasNext():
    result3.append(iterator3.next())

print(result3)
# Output: [10, 20, 30]


# Example 4
iterator4 = ZigzagIterator([1, 2, 3], [4])

result4 = []
while iterator4.hasNext():
    result4.append(iterator4.next())

print(result4)
# Output: [1, 4, 2, 3]
