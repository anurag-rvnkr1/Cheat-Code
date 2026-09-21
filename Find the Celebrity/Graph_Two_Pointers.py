'''
277. Find the Celebrity

Suppose you are at a party with n people labeled from 0 to n - 1.

There may exist one celebrity at the party.

A celebrity is defined as:
    - Everyone knows the celebrity.
    - The celebrity knows nobody else.

You are given access to the helper function:

    knows(a, b)

which returns True if person a knows person b.

Return the label of the celebrity if one exists.
Otherwise, return -1.

Example 1:
    Input:
        n = 3
        knows = [
            [1,1,0],
            [0,1,0],
            [1,1,1]
        ]

    Output: 1

Example 2:
    Input:
        n = 3
        knows = [
            [1,0,1],
            [1,1,0],
            [0,1,1]
        ]

    Output: -1

Constraints:
    2 <= n <= 100
'''

# Graph + Two Pointers

# ------------------------------------------------------------------
# LeetCode provides this API.
# Here it is mocked only for local example testing.
# ------------------------------------------------------------------
KNOWS_MATRIX = []


def knows(a: int, b: int) -> bool:
    return KNOWS_MATRIX[a][b]


class Solution:
    def findCelebrity(self, n: int) -> int:
        # Step 1: Find a potential celebrity.
        candidate = 0

        for person in range(1, n):
            if knows(candidate, person):
                candidate = person

        # Step 2: Verify the candidate.
        for person in range(n):
            if person == candidate:
                continue

            # Celebrity knows nobody.
            if knows(candidate, person):
                return -1

            # Everyone must know the celebrity.
            if not knows(person, candidate):
                return -1

        return candidate


# Example usage
solution = Solution()

# Example 1
KNOWS_MATRIX = [
    [True,  True,  False],
    [False, True,  False],
    [True,  True,  True]
]

print(solution.findCelebrity(3))
# Output: 1

# Example 2
KNOWS_MATRIX = [
    [True,  False, True],
    [True,  True,  False],
    [False, True,  True]
]

print(solution.findCelebrity(3))
# Output: -1

# Example 3
KNOWS_MATRIX = [
    [True,  True,  True,  False],
    [False, True,  True,  False],
    [False, False, True,  False],
    [True,  True,  True,  True]
]

print(solution.findCelebrity(4))
# Output: 2
