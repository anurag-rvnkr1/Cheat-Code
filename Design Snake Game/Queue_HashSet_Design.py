'''
353. Design Snake Game

Design a Snake game played on a screen of width x height.

The snake starts at position (0,0).

Implement the SnakeGame class:

    SnakeGame(int width, int height, int[][] food)
        Initializes the game.

    int move(String direction)
        Moves the snake one step in the given direction.

Directions:
    "U" -> Up
    "D" -> Down
    "L" -> Left
    "R" -> Right

Return:
    Current score after eating food.
    Return -1 if the game is over.

Example 1:
    Input:
        ["SnakeGame","move","move","move","move","move","move"]

        [[3,2,[[1,2],[0,1]]],
         ["R"],["D"],["R"],["U"],["L"],["U"]]

    Output:
        [null,0,0,1,1,2,-1]

Constraints:
    1 <= width, height <= 10^4
    1 <= food.length <= 50
    food[i].length == 2
'''

# Queue + HashSet Design

from typing import List
from collections import deque


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.food_index = 0

        self.snake = deque([(0, 0)])
        self.snake_set = {(0, 0)}

        self.directions = {
            "U": (-1, 0),
            "D": (1, 0),
            "L": (0, -1),
            "R": (0, 1)
        }

    def move(self, direction: str) -> int:
        head_row, head_col = self.snake[0]
        dr, dc = self.directions[direction]

        new_row = head_row + dr
        new_col = head_col + dc

        # Remove tail temporarily.
        tail = self.snake.pop()
        self.snake_set.remove(tail)

        # Boundary or self collision.
        if (
            new_row < 0 or
            new_row >= self.height or
            new_col < 0 or
            new_col >= self.width or
            (new_row, new_col) in self.snake_set
        ):
            return -1

        # Eat food.
        if (
            self.food_index < len(self.food) and
            [new_row, new_col] == self.food[self.food_index]
        ):
            self.food_index += 1

            # Grow snake by restoring tail.
            self.snake.append(tail)
            self.snake_set.add(tail)

        self.snake.appendleft((new_row, new_col))
        self.snake_set.add((new_row, new_col))

        return self.food_index


# Example usage
game = SnakeGame(
    3,
    2,
    [[1,2],[0,1]]
)

print(game.move("R"))
# Output: 0

print(game.move("D"))
# Output: 0

print(game.move("R"))
# Output: 1

print(game.move("U"))
# Output: 1

print(game.move("L"))
# Output: 2

print(game.move("U"))
# Output: -1
