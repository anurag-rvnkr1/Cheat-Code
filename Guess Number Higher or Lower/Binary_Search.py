'''
374. Guess Number Higher or Lower

We are playing the Guess Game.

I pick a number from 1 to n.

You have to guess which number I picked.

The pre-defined API guess(num) returns:

    -1 -> My number is lower.
     1 -> My number is higher.
     0 -> Correct guess.

Return the number that I picked.

Example 1:
    Input:
        n = 10
        pick = 6

    Output:
        6

Example 2:
    Input:
        n = 1
        pick = 1

    Output:
        1

Example 3:
    Input:
        n = 2
        pick = 1

    Output:
        1

Constraints:
    1 <= n <= 2^31 - 1
'''

# Binary Search

# The guess API is already defined on LeetCode.
#
# def guess(num: int) -> int:
#     ...


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            middle = left + (right - left) // 2

            response = guess(middle)

            if response == 0:
                return middle

            elif response == -1:
                right = middle - 1

            else:
                left = middle + 1

        return -1


# Example usage on LeetCode:
#
# n = 10
# print(Solution().guessNumber(n))
#
# Output:
# 6
