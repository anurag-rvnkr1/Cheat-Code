'''
502. IPO

Suppose LeetCode wants to maximize its capital before completing at most k projects.

Each project has:
    - profits[i]  -> profit earned after completing the project.
    - capital[i]  -> minimum capital required to start the project.

Initially, you have w capital.

Choose at most k distinct projects to maximize final capital.

Return the maximum capital after finishing at most k projects.

Example 1:
    Input:
        k = 2
        w = 0
        profits = [1,2,3]
        capital = [0,1,1]

    Output:
        4

Explanation:
        Initial capital = 0
        Choose project 0 (profit = 1) → capital = 1
        Choose project 2 (profit = 3) → capital = 4

Example 2:
    Input:
        k = 3
        w = 0
        profits = [1,2,3]
        capital = [0,1,2]

    Output:
        6

Constraints:
    1 <= k <= 10^5
    0 <= w <= 10^9
    1 <= profits.length == capital.length <= 10^5
    0 <= profits[i] <= 10^4
    0 <= capital[i] <= 10^9
'''

# Greedy + Max Heap

from typing import List
import heapq


class Solution:
    def findMaximizedCapital(
        self,
        k: int,
        w: int,
        profits: List[int],
        capital: List[int]
    ) -> int:

        # (capital_required, profit)
        projects = sorted(zip(capital, profits))

        max_heap = []
        index = 0
        total_projects = len(projects)

        # Perform at most k projects.
        for _ in range(k):

            # Add every affordable project to the heap.
            while index < total_projects and projects[index][0] <= w:
                heapq.heappush(max_heap, -projects[index][1])
                index += 1

            # No project can be started.
            if not max_heap:
                break

            # Choose the most profitable affordable project.
            w += -heapq.heappop(max_heap)

        return w


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------

solution = Solution()

# Example 1
print(solution.findMaximizedCapital(
    k=2,
    w=0,
    profits=[1,2,3],
    capital=[0,1,1]
))
# Output: 4

# Example 2
print(solution.findMaximizedCapital(
    k=3,
    w=0,
    profits=[1,2,3],
    capital=[0,1,2]
))
# Output: 6

# Example 3
print(solution.findMaximizedCapital(
    k=1,
    w=2,
    profits=[1,2,3],
    capital=[1,1,2]
))
# Output: 5

# Example 4
print(solution.findMaximizedCapital(
    k=4,
    w=1,
    profits=[2,4,6,8],
    capital=[0,1,3,5]
))
# Output: 21

# Example 5
print(solution.findMaximizedCapital(
    k=2,
    w=5,
    profits=[10,20,30],
    capital=[6,7,8]
))
# Output: 5

# Example 6
print(solution.findMaximizedCapital(
    k=5,
    w=3,
    profits=[5,6,1,8,9],
    capital=[0,2,4,3,10]
))
# Output: 31
