'''
517. Super Washing Machines

You have n washing machines arranged in a row.

machines[i] = number of dresses in the ith machine.

In one move, any subset of machines can simultaneously pass one dress
to one adjacent machine.

Return the minimum number of moves required to make every machine have
the same number of dresses. Return -1 if impossible.

Example 1:
    Input: machines = [1,0,5]
    Output: 3

Example 2:
    Input: machines = [0,3,0]
    Output: 2

Example 3:
    Input: machines = [0,2,0]
    Output: -1

Constraints:
    1 <= machines.length <= 10^4
    0 <= machines[i] <= 10^5
'''

# Greedy + Prefix Sum

from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        n = len(machines)

        # Impossible to balance.
        if total % n != 0:
            return -1

        target = total // n
        balance = 0
        answer = 0

        for dresses in machines:
            diff = dresses - target
            balance += diff

            answer = max(answer, abs(balance), diff)

        return answer


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------

solution = Solution()

# Example 1
print(solution.findMinMoves([1,0,5]))
# Output: 3

# Example 2
print(solution.findMinMoves([0,3,0]))
# Output: 2

# Example 3
print(solution.findMinMoves([0,2,0]))
# Output: -1

# Example 4
print(solution.findMinMoves([4,0,0,4]))
# Output: 2

# Example 5
print(solution.findMinMoves([2,2,2]))
# Output: 0

# Example 6
print(solution.findMinMoves([9,1,8,8,9]))
# Output: 4
