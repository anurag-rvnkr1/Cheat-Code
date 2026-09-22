'''
469. Convex Polygon

Given a list of points that form a polygon in order, determine whether the polygon
is convex.

A polygon is convex if every internal angle is less than 180 degrees, which means
the cross product of every consecutive pair of edges has the same sign.

Return True if the polygon is convex, otherwise False.

Example 1:
    Input:
        points = [[0,0],[0,1],[1,1],[1,0]]

    Output:
        True

Example 2:
    Input:
        points = [[0,0],[0,10],[10,10],[10,0],[5,5]]

    Output:
        False

Constraints:
    3 <= points.length <= 10^4
    points[i].length == 2
    -10^4 <= xi, yi <= 10^4
    All points are unique.
'''

# Geometry + Cross Product

from typing import List


class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        n = len(points)
        previous_cross = 0

        for i in range(n):
            p1 = points[i]
            p2 = points[(i + 1) % n]
            p3 = points[(i + 2) % n]

            x1 = p2[0] - p1[0]
            y1 = p2[1] - p1[1]

            x2 = p3[0] - p2[0]
            y2 = p3[1] - p2[1]

            cross = x1 * y2 - y1 * x2

            if cross != 0:
                if previous_cross != 0 and cross * previous_cross < 0:
                    return False

                previous_cross = cross

        return True


# Example usage
solution = Solution()

# Example 1
points1 = [[0,0],[0,1],[1,1],[1,0]]
print(solution.isConvex(points1))
# Output: True

# Example 2
points2 = [[0,0],[0,10],[10,10],[10,0],[5,5]]
print(solution.isConvex(points2))
# Output: False

# Example 3
points3 = [[0,0],[2,0],[2,2],[0,2]]
print(solution.isConvex(points3))
# Output: True

# Example 4
points4 = [[0,0],[2,1],[1,2],[2,3],[0,4]]
print(solution.isConvex(points4))
# Output: False

# Example 5
points5 = [[1,1],[3,1],[4,3],[2,5],[0,3]]
print(solution.isConvex(points5))
# Output: True

# Example 6
points6 = [[0,0],[1,2],[2,1],[3,3],[1,4]]
print(solution.isConvex(points6))
# Output: False
