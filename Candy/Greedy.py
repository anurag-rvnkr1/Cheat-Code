'''
135. Candy

There are n children standing in a line. Each child is assigned a rating value
given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

    - Each child must have at least one candy.
    - Children with a higher rating get more candies than their immediate neighbors.

Return the minimum number of candies you need to distribute the candies to the children.

Example 1:
    Input: ratings = [1,0,2]
    Output: 5

Explanation:
    You can allocate candies as [2,1,2].

Example 2:
    Input: ratings = [1,2,2]
    Output: 4

Explanation:
    You can allocate candies as [1,2,1].
    The third child gets 1 candy because it satisfies the conditions.

Constraints:
    n == ratings.length
    1 <= n <= 2 * 10^4
    0 <= ratings[i] <= 2 * 10^4
'''

# Greedy (Two Pass)

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # Left to Right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right to Left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


# Example usage
solution = Solution()

# Example 1
ratings1 = [1, 0, 2]
print(solution.candy(ratings1))  # Output: 5

# Example 2
ratings2 = [1, 2, 2]
print(solution.candy(ratings2))  # Output: 4

# Example 3
ratings3 = [1, 3, 4, 5, 2]
print(solution.candy(ratings3))  # Output: 11
