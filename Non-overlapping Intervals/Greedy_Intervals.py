'''
435. Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove to make the rest
of the intervals non-overlapping.

Intervals that only touch at the endpoint are considered non-overlapping.

Example 1:
    Input:
        intervals = [[1,2],[2,3],[3,4],[1,3]]

    Output:
        1

Explanation:
        Remove [1,3].

Example 2:
    Input:
        intervals = [[1,2],[1,2],[1,2]]

    Output:
        2

Example 3:
    Input:
        intervals = [[1,2],[2,3]]

    Output:
        0

Constraints:
    1 <= intervals.length <= 10^5
    intervals[i].length == 2
    -5 * 10^4 <= starti < endi <= 5 * 10^4
'''

# Greedy + Interval Scheduling

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])

        removals = 0
        previous_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < previous_end:
                removals += 1
            else:
                previous_end = end

        return removals


# Example usage
solution = Solution()

# Example 1
intervals1 = [[1,2],[2,3],[3,4],[1,3]]
print(solution.eraseOverlapIntervals(intervals1))
# Output: 1

# Example 2
intervals2 = [[1,2],[1,2],[1,2]]
print(solution.eraseOverlapIntervals(intervals2))
# Output: 2

# Example 3
intervals3 = [[1,2],[2,3]]
print(solution.eraseOverlapIntervals(intervals3))
# Output: 0

# Example 4
intervals4 = [[1,100],[11,22],[1,11],[2,12]]
print(solution.eraseOverlapIntervals(intervals4))
# Output: 2

# Example 5
intervals5 = [[0,2],[1,3],[2,4],[3,5],[4,6]]
print(solution.eraseOverlapIntervals(intervals5))
# Output: 2

# Example 6
intervals6 = [[-5,-3],[-4,-2],[-2,0],[1,2]]
print(solution.eraseOverlapIntervals(intervals6))
# Output: 1
