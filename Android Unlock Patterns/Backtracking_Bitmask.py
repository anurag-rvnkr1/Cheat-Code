'''
351. Android Unlock Patterns

An Android lock screen consists of a 3x3 grid of dots numbered 1 to 9.

A valid unlock pattern must satisfy:
    - Each pattern connects at least m keys and at most n keys.
    - All keys are distinct.
    - If a line between two keys passes through another key,
      that key must have already been visited.

Return the total number of valid unlock patterns.

Example 1:
    Input:
        m = 1
        n = 1

    Output:
        9

Example 2:
    Input:
        m = 1
        n = 2

    Output:
        65

Constraints:
    1 <= m, n <= 9
'''

# Backtracking + Bitmask

class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = [[0] * 10 for _ in range(10)]

        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = 5
        skip[3][7] = skip[7][3] = 5
        skip[4][6] = skip[6][4] = 5
        skip[2][8] = skip[8][2] = 5
        skip[7][3] = skip[3][7] = 5
        skip[9][1] = skip[1][9] = 5

        visited = [False] * 10

        def dfs(current: int, remaining: int) -> int:
            if remaining == 0:
                return 1

            visited[current] = True
            patterns = 0

            for next_key in range(1, 10):
                middle = skip[current][next_key]

                if (
                    not visited[next_key] and
                    (middle == 0 or visited[middle])
                ):
                    patterns += dfs(next_key, remaining - 1)

            visited[current] = False
            return patterns

        total_patterns = 0

        for length in range(m, n + 1):
            total_patterns += dfs(1, length - 1) * 4
            total_patterns += dfs(2, length - 1) * 4
            total_patterns += dfs(5, length - 1)

        return total_patterns


# Example usage
solution = Solution()

# Example 1
m1, n1 = 1, 1
print(solution.numberOfPatterns(m1, n1))
# Output: 9

# Example 2
m2, n2 = 1, 2
print(solution.numberOfPatterns(m2, n2))
# Output: 65

# Example 3
m3, n3 = 2, 2
print(solution.numberOfPatterns(m3, n3))
# Output: 56

# Example 4
m4, n4 = 3, 3
print(solution.numberOfPatterns(m4, n4))
# Output: 320

# Example 5
m5, n5 = 1, 3
print(solution.numberOfPatterns(m5, n5))
# Output: 385

# Example 6
m6, n6 = 4, 9
print(solution.numberOfPatterns(m6, n6))
# Output: 389112
