'''
452. Minimum Number of Arrows to Burst Balloons

There are balloons represented as intervals where:

    points[i] = [x_start, x_end]

An arrow shot at coordinate x bursts every balloon satisfying:

    x_start <= x <= x_end

Return the minimum number of arrows required to burst all balloons.

Example 1:
    Input:
        points = [[10,16],[2,8],[1,6],[7,12]]

    Output:
        2

Explanation:
        Shoot one arrow at x = 6 and another at x = 11.

Example 2:
    Input:
        points = [[1,2],[3,4],[5,6],[7,8]]

    Output:
        4

Example 3:
    Input:
        points = [[1,2],[2,3],[3,4],[4,5]]

    Output:
        2

Constraints:
    1 <= points.length <= 10^5
    points[i].length == 2
    -2^31 <= x_start < x_end <= 2^31 - 1
'''

# Greedy + Interval Scheduling

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Sort balloons by ending coordinate.
        points.sort(key=lambda interval: interval[1])

        arrows = 1
        arrow_position = points[0][1]

        for start, end in points[1:]:
            if start > arrow_position:
                arrows += 1
                arrow_position = end

        return arrows


# Example usage
solution = Solution()

# Example 1
points1 = [[10,16],[2,8],[1,6],[7,12]]
print(solution.findMinArrowShots(points1))
# Output: 2

# Example 2
points2 = [[1,2],[3,4],[5,6],[7,8]]
print(solution.findMinArrowShots(points2))
# Output: 4

# Example 3
points3 = [[1,2],[2,3],[3,4],[4,5]]
print(solution.findMinArrowShots(points3))
# Output: 2

# Example 4
points4 = [[1,5],[2,3],[4,6]]
print(solution.findMinArrowShots(points4))
# Output: 2

# Example 5
points5 = [[1,10],[2,9],[3,8],[4,7]]
print(solution.findMinArrowShots(points5))
# Output: 1

# Example 6
points6 = [[-5,-1],[-3,2],[1,4],[5,8]]
print(solution.findMinArrowShots(points6))
# Output: 3
