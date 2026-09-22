'''
490. The Maze

There is a ball in a maze with empty spaces (0) and walls (1).

The ball can roll in four directions:
    Up, Down, Left, Right

The ball keeps rolling until it hits a wall.
It stops at the cell just before the wall.

Return True if the ball can stop exactly at the destination.

Example 1:
    Input:
        maze =
        [
            [0,0,1,0,0],
            [0,0,0,0,0],
            [0,0,0,1,0],
            [1,1,0,1,1],
            [0,0,0,0,0]
        ]

        start = [0,4]
        destination = [4,4]

    Output:
        True

Example 2:
    Input:
        maze =
        [
            [0,0,1,0,0],
            [0,0,0,0,0],
            [0,0,0,1,0],
            [1,1,0,1,1],
            [0,0,0,0,0]
        ]

        start = [0,4]
        destination = [3,2]

    Output:
        False

Constraints:
    1 <= rows, cols <= 100
    maze[i][j] is 0 or 1.
'''

# BFS + Matrix Traversal

from typing import List
from collections import deque


class Solution:
    def hasPath(
        self,
        maze: List[List[int]],
        start: List[int],
        destination: List[int]
    ) -> bool:

        rows = len(maze)
        cols = len(maze[0])

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        queue = deque([tuple(start)])
        visited = {tuple(start)}

        while queue:
            row, col = queue.popleft()

            if [row, col] == destination:
                return True

            for dx, dy in directions:
                new_row = row
                new_col = col

                # Roll until hitting a wall.
                while (
                    0 <= new_row + dx < rows and
                    0 <= new_col + dy < cols and
                    maze[new_row + dx][new_col + dy] == 0
                ):
                    new_row += dx
                    new_col += dy

                if (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col))

        return False


# Example usage
solution = Solution()

# Example 1
maze1 = [
    [0,0,1,0,0],
    [0,0,0,0,0],
    [0,0,0,1,0],
    [1,1,0,1,1],
    [0,0,0,0,0]
]

print(solution.hasPath(maze1, [0,4], [4,4]))
# Output: True

# Example 2
print(solution.hasPath(maze1, [0,4], [3,2]))
# Output: False

# Example 3
maze2 = [
    [0,0,0],
    [1,1,0],
    [0,0,0]
]

print(solution.hasPath(maze2, [0,0], [2,2]))
# Output: True

# Example 4
maze3 = [
    [0,1],
    [0,0]
]

print(solution.hasPath(maze3, [0,0], [1,1]))
# Output: True

# Example 5
maze4 = [
    [0,0],
    [0,1]
]

print(solution.hasPath(maze4, [0,0], [1,0]))
# Output: True

# Example 6
maze5 = [
    [0,1,0],
    [0,1,0],
    [0,0,0]
]

print(solution.hasPath(maze5, [0,0], [0,2]))
# Output: False
