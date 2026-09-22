'''
466. Count The Repetitions

We define:
    str1 = s1 repeated n1 times.
    str2 = s2 repeated n2 times.

Return the maximum integer M such that:

    str2 repeated M times

can be obtained from str1 by deleting some characters without changing order.

Example 1:
    Input:
        s1 = "acb"
        n1 = 4
        s2 = "ab"
        n2 = 2

    Output:
        2

Example 2:
    Input:
        s1 = "acb"
        n1 = 1
        s2 = "acb"
        n2 = 1

    Output:
        1

Constraints:
    1 <= s1.length, s2.length <= 100
    s1 and s2 consist of lowercase English letters.
    1 <= n1, n2 <= 10^6
'''

# String + Dynamic Programming (Cycle Detection)


class Solution:
    def getMaxRepetitions(
        self,
        s1: str,
        n1: int,
        s2: str,
        n2: int
    ) -> int:

        if n1 == 0:
            return 0

        index_in_s2 = 0
        completed_s2 = 0

        seen = {}

        block = 0

        while block < n1:
            block += 1

            for character in s1:
                if character == s2[index_in_s2]:
                    index_in_s2 += 1

                    if index_in_s2 == len(s2):
                        completed_s2 += 1
                        index_in_s2 = 0

            # Cycle detected.
            if index_in_s2 in seen:
                previous_block, previous_completed = seen[index_in_s2]

                cycle_length = block - previous_block
                cycle_completed = completed_s2 - previous_completed

                remaining_blocks = n1 - block

                cycles = remaining_blocks // cycle_length

                completed_s2 += cycles * cycle_completed
                block += cycles * cycle_length

            else:
                seen[index_in_s2] = (block, completed_s2)

        return completed_s2 // n2


# Example usage
solution = Solution()

# Example 1
print(solution.getMaxRepetitions("acb", 4, "ab", 2))
# Output: 2

# Example 2
print(solution.getMaxRepetitions("acb", 1, "acb", 1))
# Output: 1

# Example 3
print(solution.getMaxRepetitions("abc", 4, "abc", 2))
# Output: 2

# Example 4
print(solution.getMaxRepetitions("aaa", 3, "aa", 1))
# Output: 4

# Example 5
print(solution.getMaxRepetitions("abcd", 2, "acd", 1))
# Output: 2

# Example 6
print(solution.getMaxRepetitions("baba", 11, "baab", 1))
# Output: 7
