'''
149. Max Points on a Line

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
return the maximum number of points that lie on the same straight line.

Example 1:
    Input: points = [[1,1],[2,2],[3,3]]
    Output: 3

Explanation:
    All three points lie on the same line.

Example 2:
    Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    Output: 4

Explanation:
    The maximum number of points on the same line is 4.

Constraints:
    1 <= points.length <= 300
    points[i].length == 2
    -10^4 <= xi, yi <= 10^4
    All the points are unique.
'''

# HashMap + Slope Counting

from typing import List
from collections import defaultdict
from math import gcd


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        if n <= 2:
            return n

        answer = 2

        for i in range(n):
            slopes = defaultdict(int)

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                divisor = gcd(dx, dy)
                dx //= divisor
                dy //= divisor

                # Normalize slope representation.
                if dx < 0:
                    dx *= -1
                    dy *= -1
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1

                slopes[(dx, dy)] += 1
                answer = max(answer, slopes[(dx, dy)] + 1)

        return answer


# Example usage
solution = Solution()

# Example 1
points1 = [[1, 1], [2, 2], [3, 3]]
print(solution.maxPoints(points1))  # Output: 3

# Example 2
points2 = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
print(solution.maxPoints(points2))  # Output: 4

# Example 3
points3 = [[1, 1]]
print(solution.maxPoints(points3))  # Output: 1

# Example 4
points4 = [[0, 0], [1, 1], [2, 2], [3, 3], [3, 4]]
print(solution.maxPoints(points4))  # Output: 4
