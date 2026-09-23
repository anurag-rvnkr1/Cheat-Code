'''
506. Relative Ranks

You are given an integer array score where score[i] is the score of the ith athlete.

Return an array answer where:
    - answer[i] is the rank of the ith athlete.
    - Top 3 athletes receive medals instead of numeric ranks:
        1st -> "Gold Medal"
        2nd -> "Silver Medal"
        3rd -> "Bronze Medal"

Example 1:
    Input:
        score = [5,4,3,2,1]

    Output:
        ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

Example 2:
    Input:
        score = [10,3,8,9,4]

    Output:
        ["Gold Medal","5","Bronze Medal","Silver Medal","4"]

Constraints:
    1 <= score.length <= 10^4
    0 <= score[i] <= 10^6
    All scores are unique.
'''

# Sorting + Array

from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)

        # Pair each score with its original index.
        athletes = sorted(
            enumerate(score),
            key=lambda athlete: athlete[1],
            reverse=True
        )

        answer = [""] * n

        for rank, (index, _) in enumerate(athletes):
            if rank == 0:
                answer[index] = "Gold Medal"
            elif rank == 1:
                answer[index] = "Silver Medal"
            elif rank == 2:
                answer[index] = "Bronze Medal"
            else:
                answer[index] = str(rank + 1)

        return answer


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------

solution = Solution()

# Example 1
score1 = [5,4,3,2,1]
print(solution.findRelativeRanks(score1))
# Output:
# ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

# Example 2
score2 = [10,3,8,9,4]
print(solution.findRelativeRanks(score2))
# Output:
# ["Gold Medal","5","Bronze Medal","Silver Medal","4"]

# Example 3
score3 = [100]
print(solution.findRelativeRanks(score3))
# Output:
# ["Gold Medal"]

# Example 4
score4 = [50,80,70,90]
print(solution.findRelativeRanks(score4))
# Output:
# ["4","Silver Medal","Bronze Medal","Gold Medal"]

# Example 5
score5 = [20,10,30]
print(solution.findRelativeRanks(score5))
# Output:
# ["Silver Medal","Bronze Medal","Gold Medal"]

# Example 6
score6 = [1,2,3,4,5,6]
print(solution.findRelativeRanks(score6))
# Output:
# ["6","5","4","Bronze Medal","Silver Medal","Gold Medal"]
