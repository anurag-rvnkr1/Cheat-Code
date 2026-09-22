'''
403. Frog Jump

A frog is crossing a river. The river is divided into units, and at each unit
there may or may not exist a stone.

The frog starts on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump can be:
    - k - 1 units
    - k units
    - k + 1 units

The frog can only jump forward.

Return True if the frog can reach the last stone.

Example 1:
    Input:
        stones = [0,1,3,5,6,8,12,17]

    Output:
        True

Example 2:
    Input:
        stones = [0,1,2,3,4,8,9,11]

    Output:
        False

Constraints:
    2 <= stones.length <= 2000
    0 <= stones[i] <= 2^31 - 1
    stones[0] == 0
    stones is sorted in strictly increasing order.
'''

# Dynamic Programming + HashMap

from typing import List
from collections import defaultdict


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_jumps = defaultdict(set)
        stone_jumps[0].add(0)

        stone_positions = set(stones)
        last_stone = stones[-1]

        for stone in stones:
            for jump in stone_jumps[stone]:
                for next_jump in (jump - 1, jump, jump + 1):

                    if next_jump <= 0:
                        continue

                    next_stone = stone + next_jump

                    if next_stone == last_stone:
                        return True

                    if next_stone in stone_positions:
                        stone_jumps[next_stone].add(next_jump)

        return last_stone == 0


# Example usage
solution = Solution()

# Example 1
stones1 = [0,1,3,5,6,8,12,17]
print(solution.canCross(stones1))
# Output: True

# Example 2
stones2 = [0,1,2,3,4,8,9,11]
print(solution.canCross(stones2))
# Output: False

# Example 3
stones3 = [0,1]
print(solution.canCross(stones3))
# Output: True

# Example 4
stones4 = [0,2]
print(solution.canCross(stones4))
# Output: False

# Example 5
stones5 = [0,1,3,6,10,13,15,18]
print(solution.canCross(stones5))
# Output: True

# Example 6
stones6 = [0,1,3,4,5,7,9,10,12]
print(solution.canCross(stones6))
# Output: True
