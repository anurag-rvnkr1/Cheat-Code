'''
447. Number of Boomerangs

Given n points in the plane, where points[i] = [xi, yi], return the number of
boomerangs.

A boomerang is a tuple of points (i, j, k) such that:

    - The distance between i and j equals the distance between i and k.
    - The order of the tuple matters.

Example 1:
    Input:
        points = [[0,0],[1,0],[2,0]]

    Output:
        2

Explanation:
        The boomerangs are:
        [1,0] -> [0,0] -> [2,0]
        [1,0] -> [2,0] -> [0,0]

Example 2:
    Input:
        points = [[1,1],[2,2],[3,3]]

    Output:
        2

Example 3:
    Input:
        points = [[1,1]]

    Output:
        0

Constraints:
    1 <= points.length <= 500
    points[i].length == 2
    -10^4 <= xi, yi <= 10^4
    All points are unique.
'''

# HashMap + Geometry

from typing import List
from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        boomerangs = 0

        for i in range(len(points)):
            distance_count = defaultdict(int)

            x1, y1 = points[i]

            for j in range(len(points)):
                if i == j:
                    continue

                x2, y2 = points[j]

                distance = (
                    (x1 - x2) ** 2 +
                    (y1 - y2) ** 2
                )

                distance_count[distance] += 1

            for count in distance_count.values():
                boomerangs += count * (count - 1)

        return boomerangs


# Example usage
solution = Solution()

# Example 1
points1 = [[0,0],[1,0],[2,0]]
print(solution.numberOfBoomerangs(points1))
# Output: 2

# Example 2
points2 = [[1,1],[2,2],[3,3]]
print(solution.numberOfBoomerangs(points2))
# Output: 2

# Example 3
points3 = [[1,1]]
print(solution.numberOfBoomerangs(points3))
# Output: 0

# Example 4
points4 = [[0,0],[1,1],[-1,1],[-1,-1],[1,-1]]
print(solution.numberOfBoomerangs(points4))
# Output: 20

# Example 5
points5 = [[0,0],[2,0],[0,2],[2,2]]
print(solution.numberOfBoomerangs(points5))
# Output: 8

# Example 6
points6 = [[0,0],[1,0],[0,1],[-1,0],[0,-1]]
print(solution.numberOfBoomerangs(points6))
# Output: 20
