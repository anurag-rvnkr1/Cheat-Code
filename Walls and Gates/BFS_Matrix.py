'''
286. Walls and Gates

You are given an m x n grid rooms initialized with these values:

    -1  -> A wall or obstacle.
     0  -> A gate.
     INF -> An empty room.

Fill each empty room with the distance to its nearest gate.
If it is impossible to reach a gate, it should remain INF.

INF = 2147483647 (2^31 - 1)

Modify the grid in-place.

Example 1:
    Input:
        rooms = [
            [2147483647,-1,0,2147483647],
            [2147483647,2147483647,2147483647,-1],
            [2147483647,-1,2147483647,-1],
            [0,-1,2147483647,2147483647]
        ]

    Output:
        [
            [3,-1,0,1],
            [2,2,1,-1],
            [1,-1,2,-1],
            [0,-1,3,4]
        ]

Example 2:
    Input:
        rooms = [[-1]]

    Output:
        [[-1]]

Constraints:
    m == rooms.length
    n == rooms[i].length
    1 <= m, n <= 250
'''

# Multi-Source BFS + Matrix

from typing import List
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything.
        Modify rooms in-place.
        """

        if not rooms:
            return

        ROWS = len(rooms)
        COLS = len(rooms[0])
        INF = 2147483647

        queue = deque()

        # Add every gate to the BFS queue.
        for row in range(ROWS):
            for col in range(COLS):
                if rooms[row][col] == 0:
                    queue.append((row, col))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (
                    0 <= new_row < ROWS and
                    0 <= new_col < COLS and
                    rooms[new_row][new_col] == INF
                ):
                    rooms[new_row][new_col] = rooms[row][col] + 1
                    queue.append((new_row, new_col))


# Example usage
solution = Solution()

INF = 2147483647

# Example 1
rooms1 = [
    [INF, -1, 0, INF],
    [INF, INF, INF, -1],
    [INF, -1, INF, -1],
    [0, -1, INF, INF]
]

solution.wallsAndGates(rooms1)

print(rooms1)
# Output:
# [
#   [3, -1, 0, 1],
#   [2, 2, 1, -1],
#   [1, -1, 2, -1],
#   [0, -1, 3, 4]
# ]


# Example 2
rooms2 = [[-1]]

solution.wallsAndGates(rooms2)
print(rooms2)
# Output: [[-1]]


# Example 3
rooms3 = [
    [0, INF],
    [INF, INF]
]

solution.wallsAndGates(rooms3)
print(rooms3)
# Output:
# [
#   [0, 1],
#   [1, 2]
# ]


# Example 4
rooms4 = [
    [INF, -1],
    [-1, INF]
]

solution.wallsAndGates(rooms4)
print(rooms4)
# Output:
# [
#   [2147483647, -1],
#   [-1, 2147483647]
# ]
