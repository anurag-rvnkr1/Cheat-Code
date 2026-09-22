'''
440. K-th Smallest in Lexicographical Order

Given two integers n and k, return the kth smallest integer in the range [1, n]
when the numbers are sorted in lexicographical order.

Example 1:
    Input:
        n = 13
        k = 2

    Output:
        10

Explanation:
        Lexicographical order:
        [1,10,11,12,13,2,3,4,5,6,7,8,9]
        2nd smallest = 10

Example 2:
    Input:
        n = 1
        k = 1

    Output:
        1

Constraints:
    1 <= k <= n <= 10^9
'''

# Prefix Counting (Trie-like Lexicographical Traversal)

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1
        k -= 1  # First number is already 1.

        while k > 0:
            steps = self.count_prefix(current, current + 1, n)

            if steps <= k:
                # Skip entire subtree.
                current += 1
                k -= steps
            else:
                # Go one level deeper.
                current *= 10
                k -= 1

        return current

    def count_prefix(self, first: int, next_prefix: int, limit: int) -> int:
        steps = 0

        while first <= limit:
            steps += min(limit + 1, next_prefix) - first
            first *= 10
            next_prefix *= 10

        return steps


# Example usage
solution = Solution()

# Example 1
n1 = 13
k1 = 2
print(solution.findKthNumber(n1, k1))
# Output: 10

# Example 2
n2 = 1
k2 = 1
print(solution.findKthNumber(n2, k2))
# Output: 1

# Example 3
n3 = 100
k3 = 10
print(solution.findKthNumber(n3, k3))
# Output: 17

# Example 4
n4 = 1000
k4 = 100
print(solution.findKthNumber(n4, k4))
# Output: 188

# Example 5
n5 = 500
k5 = 250
print(solution.findKthNumber(n5, k5))
# Output: 323

# Example 6
n6 = 999999999
k6 = 999999999
print(solution.findKthNumber(n6, k6))
# Output: 999999999
