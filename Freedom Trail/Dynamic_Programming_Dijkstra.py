'''
514. Freedom Trail

In the video game Fallout 4, the quest "Freedom Trail" requires players to spell
a keyword by rotating a circular ring.

Given:
    ring : circular string engraved on the ring.
    key  : string to spell.

Operations:
    - Rotate ring clockwise or counter-clockwise by one position = 1 step.
    - Press the center button to select a character = 1 step.

Return the minimum number of steps to spell the entire key.

Example 1:
    Input:
        ring = "godding"
        key = "gd"

    Output:
        4

Example 2:
    Input:
        ring = "godding"
        key = "godding"

    Output:
        13

Constraints:
    1 <= ring.length, key.length <= 100
    ring and key contain lowercase English letters.
'''

# Dynamic Programming + Memoization

from typing import List
from functools import lru_cache
from collections import defaultdict


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)

        # Store all positions for each character.
        positions = defaultdict(list)
        for index, char in enumerate(ring):
            positions[char].append(index)

        @lru_cache(None)
        def dp(ring_pos: int, key_pos: int) -> int:
            if key_pos == len(key):
                return 0

            answer = float("inf")

            for target in positions[key[key_pos]]:
                distance = abs(target - ring_pos)
                rotate = min(distance, n - distance)

                answer = min(
                    answer,
                    rotate + 1 + dp(target, key_pos + 1)
                )

            return answer

        return dp(0, 0)


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------

solution = Solution()

# Example 1
print(solution.findRotateSteps("godding", "gd"))
# Output: 4

# Example 2
print(solution.findRotateSteps("godding", "godding"))
# Output: 13

# Example 3
print(solution.findRotateSteps("abcde", "ade"))
# Output: 6

# Example 4
print(solution.findRotateSteps("aaa", "aa"))
# Output: 2

# Example 5
print(solution.findRotateSteps("iotfo", "fioot"))
# Output: 11

# Example 6
print(solution.findRotateSteps("ababcab", "acba"))
# Output: 8
