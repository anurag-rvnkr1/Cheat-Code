'''
465. Optimal Account Balancing

You are given transactions where:

    transactions[i] = [from, to, amount]

Person "from" gives "amount" money to person "to".

Return the minimum number of transactions required to settle all debts.

Example 1:
    Input:
        transactions = [[0,1,10],[2,0,5]]

    Output:
        2

Explanation:
        Person 1 receives 10.
        Person 2 owes 5.
        Person 0 owes 5.

Example 2:
    Input:
        transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]

    Output:
        1

Constraints:
    1 <= transactions.length <= 8
    0 <= from, to < 12
    from != to
    1 <= amount <= 100
'''

# Backtracking + Graph + Debt Settlement

from typing import List
from collections import defaultdict


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = defaultdict(int)

        # Calculate net balance for each person.
        for sender, receiver, amount in transactions:
            balance[sender] -= amount
            balance[receiver] += amount

        debts = []

        for amount in balance.values():
            if amount != 0:
                debts.append(amount)

        def dfs(index: int) -> int:
            # Skip settled debts.
            while index < len(debts) and debts[index] == 0:
                index += 1

            if index == len(debts):
                return 0

            minimum_transactions = float("inf")

            for next_index in range(index + 1, len(debts)):
                # Only settle opposite signs.
                if debts[index] * debts[next_index] < 0:
                    debts[next_index] += debts[index]

                    minimum_transactions = min(
                        minimum_transactions,
                        1 + dfs(index + 1)
                    )

                    debts[next_index] -= debts[index]

                    # Optimization.
                    if debts[next_index] + debts[index] == 0:
                        break

            return minimum_transactions

        return dfs(0)


# Example usage
solution = Solution()

# Example 1
transactions1 = [
    [0,1,10],
    [2,0,5]
]
print(solution.minTransfers(transactions1))
# Output: 2

# Example 2
transactions2 = [
    [0,1,10],
    [1,0,1],
    [1,2,5],
    [2,0,5]
]
print(solution.minTransfers(transactions2))
# Output: 1

# Example 3
transactions3 = [
    [0,1,5],
    [1,2,5],
    [2,0,5]
]
print(solution.minTransfers(transactions3))
# Output: 0

# Example 4
transactions4 = [
    [0,1,10],
    [1,2,5],
    [2,3,5]
]
print(solution.minTransfers(transactions4))
# Output: 2

# Example 5
transactions5 = [
    [0,1,20],
    [2,0,10],
    [1,2,5]
]
print(solution.minTransfers(transactions5))
# Output: 2

# Example 6
transactions6 = [
    [0,3,2],
    [1,3,7],
    [2,1,5],
    [2,0,4]
]
print(solution.minTransfers(transactions6))
# Output: 2
