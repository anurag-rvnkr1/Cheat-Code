'''
455. Assign Cookies

Assume you are assigning cookies to children.

Each child has a greed factor g[i].
Each cookie has a size s[j].

A child is satisfied if the cookie size is greater than or equal to the greed factor.

Each cookie can be assigned to at most one child.

Return the maximum number of satisfied children.

Example 1:
    Input:
        g = [1,2,3]
        s = [1,1]

    Output:
        1

Example 2:
    Input:
        g = [1,2]
        s = [1,2,3]

    Output:
        2

Constraints:
    1 <= g.length, s.length <= 3 * 10^4
    1 <= g[i], s[j] <= 2^31 - 1
'''

# Greedy + Two Pointers

from typing import List


class Solution:
    def findContentChildren(
        self,
        g: List[int],
        s: List[int]
    ) -> int:

        g.sort()
        s.sort()

        child = 0
        cookie = 0

        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1

            cookie += 1

        return child


# Example usage
solution = Solution()

# Example 1
g1 = [1,2,3]
s1 = [1,1]
print(solution.findContentChildren(g1, s1))
# Output: 1

# Example 2
g2 = [1,2]
s2 = [1,2,3]
print(solution.findContentChildren(g2, s2))
# Output: 2

# Example 3
g3 = [2,3,4]
s3 = [1,2,2,3]
print(solution.findContentChildren(g3, s3))
# Output: 2

# Example 4
g4 = [5]
s4 = [1,2,3,4]
print(solution.findContentChildren(g4, s4))
# Output: 0

# Example 5
g5 = [1,2,2,3]
s5 = [2,3]
print(solution.findContentChildren(g5, s5))
# Output: 2

# Example 6
g6 = [1,1,1]
s6 = [1,1,1]
print(solution.findContentChildren(g6, s6))
# Output: 3
