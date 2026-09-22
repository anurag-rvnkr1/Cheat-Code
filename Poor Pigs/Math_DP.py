'''
458. Poor Pigs

There are buckets buckets, exactly one of which is poisonous.

A pig dies minutesToDie minutes after drinking poison.

You have minutesToTest minutes total to determine the poisonous bucket.

Return the minimum number of pigs needed to guarantee identifying the poisonous bucket.

Example 1:
    Input:
        buckets = 4
        minutesToDie = 15
        minutesToTest = 15

    Output:
        2

Explanation:
        Each pig has 2 possible states (alive/dead).

Example 2:
    Input:
        buckets = 4
        minutesToDie = 15
        minutesToTest = 30

    Output:
        2

Explanation:
        Each pig has 3 possible states because there are 2 rounds.

Example 3:
    Input:
        buckets = 1
        minutesToDie = 1
        minutesToTest = 1

    Output:
        0

Constraints:
    1 <= buckets <= 1000
    1 <= minutesToDie <= minutesToTest <= 100
'''

# Math + Dynamic Programming (Combinatorics)


class Solution:
    def poorPigs(
        self,
        buckets: int,
        minutesToDie: int,
        minutesToTest: int
    ) -> int:

        if buckets == 1:
            return 0

        rounds = minutesToTest // minutesToDie
        states = rounds + 1

        pigs = 0
        capacity = 1

        while capacity < buckets:
            pigs += 1
            capacity *= states

        return pigs


# Example usage
solution = Solution()

# Example 1
buckets1 = 4
die1 = 15
test1 = 15
print(solution.poorPigs(buckets1, die1, test1))
# Output: 2

# Example 2
buckets2 = 4
die2 = 15
test2 = 30
print(solution.poorPigs(buckets2, die2, test2))
# Output: 2

# Example 3
buckets3 = 1
die3 = 1
test3 = 1
print(solution.poorPigs(buckets3, die3, test3))
# Output: 0

# Example 4
buckets4 = 1000
die4 = 15
test4 = 60
print(solution.poorPigs(buckets4, die4, test4))
# Output: 5

# Example 5
buckets5 = 25
die5 = 15
test5 = 45
print(solution.poorPigs(buckets5, die5, test5))
# Output: 2

# Example 6
buckets6 = 125
die6 = 10
test6 = 30
print(solution.poorPigs(buckets6, die6, test6))
# Output: 3
