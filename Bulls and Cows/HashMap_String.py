'''
299. Bulls and Cows

You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess it.

A hint is generated with:
    - Bulls: Digits that are correct in both value and position.
    - Cows: Digits that are correct in value but in the wrong position.

Return the hint as:
    "<bulls>A<cows>B"

Example 1:
    Input:
        secret = "1807"
        guess = "7810"

    Output:
        "1A3B"

Explanation:
    Bulls:
        8

    Cows:
        1, 0, 7

Example 2:
    Input:
        secret = "1123"
        guess = "0111"

    Output:
        "1A1B"

Constraints:
    1 <= secret.length == guess.length <= 1000
    secret and guess consist of digits only.
'''

# HashMap + String

from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        balance = defaultdict(int)

        for secret_digit, guess_digit in zip(secret, guess):

            if secret_digit == guess_digit:
                bulls += 1

            else:
                # Guess digit previously appeared in secret.
                if balance[secret_digit] < 0:
                    cows += 1

                # Secret digit previously appeared in guess.
                if balance[guess_digit] > 0:
                    cows += 1

                balance[secret_digit] += 1
                balance[guess_digit] -= 1

        return f"{bulls}A{cows}B"


# Example usage
solution = Solution()

# Example 1
secret1 = "1807"
guess1 = "7810"
print(solution.getHint(secret1, guess1))
# Output: "1A3B"

# Example 2
secret2 = "1123"
guess2 = "0111"
print(solution.getHint(secret2, guess2))
# Output: "1A1B"

# Example 3
secret3 = "1234"
guess3 = "1234"
print(solution.getHint(secret3, guess3))
# Output: "4A0B"

# Example 4
secret4 = "1234"
guess4 = "4321"
print(solution.getHint(secret4, guess4))
# Output: "0A4B"

# Example 5
secret5 = "1111"
guess5 = "1111"
print(solution.getHint(secret5, guess5))
# Output: "4A0B"

# Example 6
secret6 = "987654"
guess6 = "456789"
print(solution.getHint(secret6, guess6))
# Output: "0A6B"
