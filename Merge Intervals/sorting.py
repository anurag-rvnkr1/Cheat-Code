"""
56. Merge Intervals
Solved
Medium
Topics
premium lock icon
Companies
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

#sorting method

class Solution:
    def merge(self, intervals):

        # Sort by starting time
        intervals.sort(key=lambda x: x[0])

        result = []

        for start, end in intervals:

            # No overlap
            if not result or start > result[-1][1]:
                result.append([start, end])

            # Overlap
            else:
                result[-1][1] = max(result[-1][1], end)

        return result
