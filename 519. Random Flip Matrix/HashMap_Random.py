'''
519. Random Flip Matrix

You are given an m x n binary matrix initialized with all 0's.

Implement:

    Solution(m, n)
        Initializes the matrix.

    flip()
        Randomly chooses one 0, changes it to 1,
        and returns its position [row, col].

    reset()
        Changes all values back to 0.

All zero cells must have equal probability of being chosen.

Example 1:
    Input:
        ["Solution","flip","flip","flip","reset","flip"]
        [[2,3],[],[],[],[],[]]

    Output:
        Random unique positions until reset.
'''

# HashMap + Random Sampling

from typing import List
import random


class Solution:
    def __init__(self, m: int, n: int):
        self.rows = m
        self.cols = n
        self.total = m * n
        self.map = {}

    def flip(self) -> List[int]:
        # Pick a random remaining index.
        rand = random.randint(0, self.total - 1)
        self.total -= 1

        index = self.map.get(rand, rand)

        # Swap with the last available index.
        self.map[rand] = self.map.get(self.total, self.total)

        return [index // self.cols, index % self.cols]

    def reset(self) -> None:
        self.total = self.rows * self.cols
        self.map.clear()


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------

solution = Solution(2, 3)

# Example 1
print(solution.flip())   # Random cell
print(solution.flip())   # Random unused cell
print(solution.flip())   # Random unused cell

# Example 2
solution.reset()
print(solution.flip())   # Random cell after reset

# Example 3
solution2 = Solution(1, 1)
print(solution2.flip())  # [0,0]

# Example 4
solution3 = Solution(3, 3)
for _ in range(5):
    print(solution3.flip())

# Example 5
solution3.reset()
print(solution3.flip())

# Example 6
solution4 = Solution(2, 2)
cells = [solution4.flip() for _ in range(4)]
print(cells)
