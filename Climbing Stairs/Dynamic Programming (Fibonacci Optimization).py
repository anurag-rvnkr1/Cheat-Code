'''
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.

Return the number of distinct ways to climb to the top.

Example 1:
    Input: n = 2
    Output: 2
    Explanation:
    There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

Example 2:
    Input: n = 3
    Output: 3
    Explanation:
    There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

Constraints:
    1 <= n <= 45
'''

# Dynamic Programming (Fibonacci Optimization)
class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        prev2 = 1
        prev1 = 2

        for _ in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1


# Example usage
solution = Solution()

print(solution.climbStairs(2))  # Output: 2
print(solution.climbStairs(3))  # Output: 3
print(solution.climbStairs(5))  # Output: 8
print(solution.climbStairs(10))  # Output: 89
