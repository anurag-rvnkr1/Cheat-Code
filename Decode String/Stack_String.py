'''
394. Decode String

Given an encoded string, return its decoded string.

Encoding rule:

    k[encoded_string]

where encoded_string inside the square brackets is repeated exactly k times.

Nested encodings are valid.

Example 1:
    Input:
        s = "3[a]2[bc]"

    Output:
        "aaabcbc"

Example 2:
    Input:
        s = "3[a2[c]]"

    Output:
        "accaccacc"

Example 3:
    Input:
        s = "2[abc]3[cd]ef"

    Output:
        "abcabccdcdcdef"

Constraints:
    1 <= s.length <= 30
    s consists of lowercase English letters, digits, and square brackets.
    All integers are in the range [1, 300].
'''

# Stack + String Parsing

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_number = 0
        current_string = ""

        for character in s:

            if character.isdigit():
                current_number = current_number * 10 + int(character)

            elif character == "[":
                stack.append((current_string, current_number))
                current_string = ""
                current_number = 0

            elif character == "]":
                previous_string, repeat = stack.pop()
                current_string = previous_string + current_string * repeat

            else:
                current_string += character

        return current_string


# Example usage
solution = Solution()

# Example 1
s1 = "3[a]2[bc]"
print(solution.decodeString(s1))
# Output: "aaabcbc"

# Example 2
s2 = "3[a2[c]]"
print(solution.decodeString(s2))
# Output: "accaccacc"

# Example 3
s3 = "2[abc]3[cd]ef"
print(solution.decodeString(s3))
# Output: "abcabccdcdcdef"

# Example 4
s4 = "10[a]"
print(solution.decodeString(s4))
# Output: "aaaaaaaaaa"

# Example 5
s5 = "2[ab3[c]]"
print(solution.decodeString(s5))
# Output: "abcccabccc"

# Example 6
s6 = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
print(solution.decodeString(s6))
# Output: "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
