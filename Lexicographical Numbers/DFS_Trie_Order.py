'''
386. Lexicographical Numbers

Given an integer n, return all the numbers in the range [1, n]
sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1)
extra space (excluding the output list).

Example 1:
    Input:
        n = 13

    Output:
        [1,10,11,12,13,2,3,4,5,6,7,8,9]

Example 2:
    Input:
        n = 2

    Output:
        [1,2]

Constraints:
    1 <= n <= 5 * 10^4
'''

# DFS / Lexicographical Traversal

from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        current = 1

        for _ in range(n):
            result.append(current)

            if current * 10 <= n:
                current *= 10
            else:
                while current % 10 == 9 or current + 1 > n:
                    current //= 10

                current += 1

        return result


# Example usage
solution = Solution()

# Example 1
n1 = 13
print(solution.lexicalOrder(n1))
# Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

# Example 2
n2 = 2
print(solution.lexicalOrder(n2))
# Output: [1,2]

# Example 3
n3 = 20
print(solution.lexicalOrder(n3))
# Output:
# [1,10,11,12,13,14,15,16,17,18,19,2,20,3,4,5,6,7,8,9]

# Example 4
n4 = 25
print(solution.lexicalOrder(n4))
# Output:
# [1,10,11,12,13,14,15,16,17,18,19,2,20,21,22,23,24,25,3,4,5,6,7,8,9]

# Example 5
n5 = 5
print(solution.lexicalOrder(n5))
# Output: [1,2,3,4,5]

# Example 6
n6 = 35
print(solution.lexicalOrder(n6))
# Output:
# [1,10,11,12,13,14,15,16,17,18,19,2,20,21,22,23,24,25,26,27,28,29,
#  3,30,31,32,33,34,35,4,5,6,7,8,9]
