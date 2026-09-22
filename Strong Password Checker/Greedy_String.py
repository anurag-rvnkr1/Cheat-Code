'''
420. Strong Password Checker

A password is considered strong if:

    - Length is between 6 and 20 characters.
    - Contains at least one lowercase letter.
    - Contains at least one uppercase letter.
    - Contains at least one digit.
    - Does not contain three repeating characters consecutively.

Return the minimum number of steps required to make the password strong.

Operations allowed:
    - Insert one character.
    - Delete one character.
    - Replace one character.

Example 1:
    Input:
        password = "a"

    Output:
        5

Example 2:
    Input:
        password = "aA1"

    Output:
        3

Example 3:
    Input:
        password = "1337C0d3"

    Output:
        0

Constraints:
    1 <= password.length <= 50
    password consists of letters, digits, '.', or '!'.
'''

# Greedy + String

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        length = len(password)

        missing_lower = 1
        missing_upper = 1
        missing_digit = 1

        for character in password:
            if character.islower():
                missing_lower = 0
            elif character.isupper():
                missing_upper = 0
            elif character.isdigit():
                missing_digit = 0

        missing_types = (
            missing_lower +
            missing_upper +
            missing_digit
        )

        replacements = 0
        one_mod = 0
        two_mod = 0

        index = 0

        while index < length:
            next_index = index

            while (
                next_index < length and
                password[next_index] == password[index]
            ):
                next_index += 1

            repeat_length = next_index - index

            if repeat_length >= 3:
                replacements += repeat_length // 3

                if repeat_length % 3 == 0:
                    one_mod += 1
                elif repeat_length % 3 == 1:
                    two_mod += 1

            index = next_index

        # Case 1: Password too short.
        if length < 6:
            return max(missing_types, 6 - length)

        # Case 2: Password length is valid.
        if length <= 20:
            return max(missing_types, replacements)

        # Case 3: Password too long.
        deletions = length - 20
        remaining_deletions = deletions

        # Remove one character from groups where len % 3 == 0.
        use = min(one_mod, remaining_deletions)
        replacements -= use
        remaining_deletions -= use

        # Remove two characters from groups where len % 3 == 1.
        use = min(two_mod * 2, remaining_deletions)
        replacements -= use // 2
        remaining_deletions -= use

        # Remove three characters from remaining groups.
        use = remaining_deletions // 3
        replacements -= use

        return deletions + max(missing_types, replacements)


# Example usage
solution = Solution()

# Example 1
password1 = "a"
print(solution.strongPasswordChecker(password1))
# Output: 5

# Example 2
password2 = "aA1"
print(solution.strongPasswordChecker(password2))
# Output: 3

# Example 3
password3 = "1337C0d3"
print(solution.strongPasswordChecker(password3))
# Output: 0

# Example 4
password4 = "aaaaaa"
print(solution.strongPasswordChecker(password4))
# Output: 2

# Example 5
password5 = "AAAAAAAAAAAAAAAAAAAAA"
print(solution.strongPasswordChecker(password5))
# Output: 7

# Example 6
password6 = "aaaAAA111bbbBBB222cccCCC333"
print(solution.strongPasswordChecker(password6))
# Output: 9
