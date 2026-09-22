'''
436. Find Right Interval

You are given an array of intervals where intervals[i] = [starti, endi].

For each interval i, find the interval j such that:
    startj >= endi

and startj is the smallest possible value.

Return an array of indices representing the right interval for every interval.
Return -1 if no right interval exists.

Example 1:
    Input:
        intervals = [[1,2]]

    Output:
        [-1]

Example 2:
    Input:
        intervals = [[3,4],[2,3],[1,2]]

    Output:
        [-1,0,1]

Example 3:
    Input:
        intervals = [[1,4],[2,3],[3,4]]

    Output:
        [-1,2,-1]

Constraints:
    1 <= intervals.length <= 2 * 10^4
    intervals[i].length == 2
    -10^6 <= starti <= endi <= 10^6
    The start point of each interval is unique.
'''

# Binary Search + Sorting

from typing import List
import bisect


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted(
            (interval[0], index)
            for index, interval in enumerate(intervals)
        )

        sorted_starts = [start for start, _ in starts]
        result = []

        for _, end in intervals:
            position = bisect.bisect_left(sorted_starts, end)

            if position == len(starts):
                result.append(-1)
            else:
                result.append(starts[position][1])

        return result


# Example usage
solution = Solution()

# Example 1
intervals1 = [[1,2]]
print(solution.findRightInterval(intervals1))
# Output: [-1]

# Example 2
intervals2 = [[3,4],[2,3],[1,2]]
print(solution.findRightInterval(intervals2))
# Output: [-1,0,1]

# Example 3
intervals3 = [[1,4],[2,3],[3,4]]
print(solution.findRightInterval(intervals3))
# Output: [-1,2,-1]

# Example 4
intervals4 = [[1,1],[3,4]]
print(solution.findRightInterval(intervals4))
# Output: [0,-1]

# Example 5
intervals5 = [[5,7],[1,2],[2,4],[8,9]]
print(solution.findRightInterval(intervals5))
# Output: [3,2,0,-1]

# Example 6
intervals6 = [[0,2],[3,5],[6,8],[2,3]]
print(solution.findRightInterval(intervals6))
# Output: [1,2,-1,1]
