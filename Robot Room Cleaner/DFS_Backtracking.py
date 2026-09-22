'''
489. Robot Room Cleaner

You are controlling a robot inside an unknown room.

Robot API (provided by LeetCode):

    robot.move()
        Returns True if the cell in front is open and the robot moves forward.

    robot.turnLeft()
        Rotates the robot 90 degrees left.

    robot.turnRight()
        Rotates the robot 90 degrees right.

    robot.clean()
        Cleans the current cell.

The room layout is unknown.
Blocked cells cannot be entered.

Return nothing. Clean every reachable cell exactly once.

Example:
    Input:
        Room Grid (hidden from your solution)

    Output:
        All reachable cells are cleaned.

Constraints:
    The grid is unknown.
    The robot starts on an empty cell facing up.
'''

# DFS + Backtracking

# ---------------------------------------------------------------------
# NOTE:
# Robot interface is provided by LeetCode.
#
# class Robot:
#     def move(self) -> bool:
#     def turnLeft(self) -> None:
#     def turnRight(self) -> None:
#     def clean(self) -> None:
# ---------------------------------------------------------------------

from typing import Set, Tuple


class Solution:
    def cleanRoom(self, robot) -> None:
        visited: Set[Tuple[int, int]] = set()

        # Up, Right, Down, Left
        directions = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]

        def go_back():
            robot.turnRight()
            robot.turnRight()

            robot.move()

            robot.turnRight()
            robot.turnRight()

        def dfs(row: int, col: int, direction: int):
            visited.add((row, col))
            robot.clean()

            for step in range(4):
                new_direction = (direction + step) % 4

                dx, dy = directions[new_direction]

                next_row = row + dx
                next_col = col + dy

                if (next_row, next_col) not in visited:
                    if robot.move():
                        dfs(next_row, next_col, new_direction)

                        # Return robot to previous cell.
                        go_back()

                robot.turnRight()

        dfs(0, 0, 0)


# ---------------------------------------------------------------------
# Example Usage (Illustrative Only)
# ---------------------------------------------------------------------

'''
LeetCode provides the Robot object automatically.

Example:

robot = Robot()
solution = Solution()
solution.cleanRoom(robot)

The function cleans every reachable cell in the unknown room.

There are no printable test cases because the robot API interacts with
a hidden environment during evaluation.
'''
