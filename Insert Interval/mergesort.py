"""
57. Insert Interval

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Two intervals are considered overlapping if they share at least one point.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""

#Mergesort solution method

class Solution:
    def insert(self, intervals, newInterval):

        result = []

        start, end = newInterval

        for current_start, current_end in intervals:

            # Case 1: Current interval is completely before newInterval
            if current_end < start:
                result.append([current_start, current_end])

            # Case 2: Current interval is completely after newInterval
            elif current_start > end:
                result.append([start, end])

                # Add all remaining intervals
                result.append([current_start, current_end])

                # Copy remaining intervals
                index = intervals.index([current_start, current_end]) + 1

                result.extend(intervals[index:])

                return result

            # Case 3: Overlapping intervals
            else:
                start = min(start, current_start)
                end = max(end, current_end)

        # Add newInterval at the end
        result.append([start, end])

        return result
