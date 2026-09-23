'''
505. The Maze II

There is a ball in a maze represented by:

    0 -> Empty cell
    1 -> Wall

The ball rolls continuously in one direction until it hits a wall.
It stops at the cell before the wall.

Return the shortest distance for the ball to stop at the destination.
If it cannot stop at the destination, return -1.

Distance = number of empty spaces traveled.

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
        12

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
        -1

Constraints:
    1 <= rows, cols <= 100
    maze[i][j] is either 0 or 1.
'''

# Dijkstra + BFS + Priority Queue

from typing import List
import heapq


class Solution:
    def shortestDistance(
        self,
        maze: List[List[int]],
        start: List[int],
        destination: List[int]
    ) -> int:

        rows = len(maze)
        cols = len(maze[0])

        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        distances = [
            [float("inf")] * cols
            for _ in range(rows)
        ]

        distances[start[0]][start[1]] = 0

        priority_queue = [(0, start[0], start[1])]

        while priority_queue:
            current_distance, row, col = heapq.heappop(priority_queue)

            if [row, col] == destination:
                return current_distance

            if current_distance > distances[row][col]:
                continue

            for dx, dy in directions:
                new_row = row
                new_col = col
                travelled = current_distance

                # Roll until hitting a wall.
                while (
                    0 <= new_row + dx < rows and
                    0 <= new_col + dy < cols and
                    maze[new_row + dx][new_col + dy] == 0
                ):
                    new_row += dx
                    new_col += dy
                    travelled += 1

                if travelled < distances[new_row][new_col]:
                    distances[new_row][new_col] = travelled

                    heapq.heappush(
                        priority_queue,
                        (travelled, new_row, new_col)
                    )

        return -1


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------

solution = Solution()

# Example 1
maze1 = [
    [0,0,1,0,0],
    [0,0,0,0,0],
    [0,0,0,1,0],
    [1,1,0,1,1],
    [0,0,0,0,0]
]

print(solution.shortestDistance(
    maze1,
    [0,4],
    [4,4]
))
# Output: 12

# Example 2
print(solution.shortestDistance(
    maze1,
    [0,4],
    [3,2]
))
# Output: -1

# Example 3
maze2 = [
    [0,0,0],
    [1,1,0],
    [0,0,0]
]

print(solution.shortestDistance(
    maze2,
    [0,0],
    [2,2]
))
# Output: 4

# Example 4
maze3 = [
    [0,1],
    [0,0]
]

print(solution.shortestDistance(
    maze3,
    [0,0],
    [1,1]
))
# Output: 2

# Example 5
maze4 = [
    [0,0],
    [0,1]
]

print(solution.shortestDistance(
    maze4,
    [0,0],
    [1,0]
))
# Output: 1

# Example 6
maze5 = [
    [0,1,0],
    [0,1,0],
    [0,0,0]
]

print(solution.shortestDistance(
    maze5,
    [2,0],
    [0,2]
))
# Output: 6
