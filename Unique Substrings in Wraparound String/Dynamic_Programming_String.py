'''
467. Unique Substrings in Wraparound String

Consider the infinite wraparound string:

    "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd..."

Given a string p, return the number of unique non-empty substrings of p that
exist in the infinite wraparound string.

Example 1:
    Input:
        p = "a"

    Output:
        1

Example 2:
    Input:
        p = "cac"

    Output:
        2

Explanation:
        Unique substrings are "a" and "c".

Example 3:
    Input:
        p = "zab"

    Output:
        6

Explanation:
        Unique substrings are:
        "z","a","b","za","ab","zab"

Constraints:
    1 <= p.length <= 10^5
    p consists of lowercase English letters.
'''

# Dynamic Programming + String

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        # max_length[i] = longest valid wraparound substring ending with letter i.
        max_length = [0] * 26

        current_length = 0

        for index in range(len(p)):
            if (
                index > 0 and
                (
                    ord(p[index]) - ord(p[index - 1]) == 1 or
                    (p[index - 1] == "z" and p[index] == "a")
                )
            ):
                current_length += 1
            else:
                current_length = 1

            character_index = ord(p[index]) - ord("a")

            max_length[character_index] = max(
                max_length[character_index],
                current_length
            )

        return sum(max_length)


# Example usage
solution = Solution()

# Example 1
p1 = "a"
print(solution.findSubstringInWraproundString(p1))
# Output: 1

# Example 2
p2 = "cac"
print(solution.findSubstringInWraproundString(p2))
# Output: 2

# Example 3
p3 = "zab"
print(solution.findSubstringInWraproundString(p3))
# Output: 6

# Example 4
p4 = "abcdefghijklmnopqrstuvwxyz"
print(solution.findSubstringInWraproundString(p4))
# Output: 351

# Example 5
p5 = "abczabc"
print(solution.findSubstringInWraproundString(p5))
# Output: 10

# Example 6
p6 = "zzabcz"
print(solution.findSubstringInWraproundString(p6))
# Output: 10
