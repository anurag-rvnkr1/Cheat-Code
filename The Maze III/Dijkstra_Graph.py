'''
499. The Maze III

There is a ball in a maze represented by:

    0 -> Empty cell
    1 -> Wall

The ball rolls continuously until it hits a wall or falls into the hole.

Return the lexicographically smallest path that allows the ball to fall into
the hole using the shortest possible distance.

Directions:
    u = up
    d = down
    l = left
    r = right

If impossible, return "impossible".

Example 1:
    Input:
        maze =
        [
            [0,0,0,0,0],
            [1,1,0,0,1],
            [0,0,0,0,0],
            [0,1,0,0,1],
            [0,1,0,0,0]
        ]

        ball = [4,3]
        hole = [0,1]

    Output:
        "lul"

Example 2:
    Input:
        maze =
        [
            [0,0,0,0,0],
            [1,1,0,0,1],
            [0,0,0,0,0],
            [0,1,0,0,1],
            [0,1,0,0,0]
        ]

        ball = [4,3]
        hole = [3,0]

    Output:
        "impossible"

Constraints:
    1 <= rows, cols <= 30
    maze[i][j] is 0 or 1.
'''

# Dijkstra + Graph + Priority Queue

from typing import List
import heapq


class Solution:
    def findShortestWay(
        self,
        maze: List[List[int]],
        ball: List[int],
        hole: List[int]
    ) -> str:

        rows = len(maze)
        cols = len(maze[0])

        directions = [
            ("d", 1, 0),
            ("l", 0, -1),
            ("r", 0, 1),
            ("u", -1, 0)
        ]

        priority_queue = [
            (0, "", ball[0], ball[1])
        ]

        best = {}

        while priority_queue:
            distance, path, row, col = heapq.heappop(priority_queue)

            if (row, col) in best:
                continue

            best[(row, col)] = (distance, path)

            if [row, col] == hole:
                return path

            for move, dx, dy in directions:
                new_row = row
                new_col = col
                steps = distance

                while (
                    0 <= new_row + dx < rows and
                    0 <= new_col + dy < cols and
                    maze[new_row + dx][new_col + dy] == 0
                ):
                    new_row += dx
                    new_col += dy
                    steps += 1

                    # Stop immediately if hole is reached.
                    if [new_row, new_col] == hole:
                        break

                if (new_row, new_col) not in best:
                    heapq.heappush(
                        priority_queue,
                        (steps, path + move, new_row, new_col)
                    )

        return "impossible"


# Example usage
solution = Solution()

# Example 1
maze1 = [
    [0,0,0,0,0],
    [1,1,0,0,1],
    [0,0,0,0,0],
    [0,1,0,0,1],
    [0,1,0,0,0]
]

ball1 = [4,3]
hole1 = [0,1]

print(solution.findShortestWay(maze1, ball1, hole1))
# Output: "lul"

# Example 2
ball2 = [4,3]
hole2 = [3,0]

print(solution.findShortestWay(maze1, ball2, hole2))
# Output: "impossible"

# Example 3
maze2 = [
    [0,0,1],
    [0,0,0],
    [1,0,0]
]

ball3 = [0,0]
hole3 = [2,2]

print(solution.findShortestWay(maze2, ball3, hole3))
# Output: "dr"

# Example 4
maze3 = [
    [0,0],
    [0,0]
]

ball4 = [0,0]
hole4 = [1,1]

print(solution.findShortestWay(maze3, ball4, hole4))
# Output: "dr"

# Example 5
maze4 = [
    [0,0,0],
    [1,1,0],
    [0,0,0]
]

ball5 = [2,0]
hole5 = [0,2]

print(solution.findShortestWay(maze4, ball5, hole5))
# Output: "ru"

# Example 6
maze5 = [
    [0,1,0],
    [0,1,0],
    [0,0,0]
]

ball6 = [2,0]
hole6 = [0,2]

print(solution.findShortestWay(maze5, ball6, hole6))
# Output: "ru"
