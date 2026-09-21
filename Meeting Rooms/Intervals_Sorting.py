'''
252. Meeting Rooms

Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings.

Example 1:
    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: False

Explanation:
    Meetings [0,30] and [5,10] overlap.

Example 2:
    Input: intervals = [[7,10],[2,4]]
    Output: True

Explanation:
    The meetings do not overlap.

Constraints:
    0 <= intervals.length <= 10^4
    intervals[i].length == 2
    0 <= starti < endi <= 10^6
'''

# Intervals + Sorting

from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sort meetings by start time.
        intervals.sort(key=lambda interval: interval[0])

        # Check for overlapping meetings.
        for i in range(1, len(intervals)):
            previous_end = intervals[i - 1][1]
            current_start = intervals[i][0]

            if current_start < previous_end:
                return False

        return True


# Example usage
solution = Solution()

# Example 1
intervals1 = [[0, 30], [5, 10], [15, 20]]
print(solution.canAttendMeetings(intervals1))
# Output: False

# Example 2
intervals2 = [[7, 10], [2, 4]]
print(solution.canAttendMeetings(intervals2))
# Output: True

# Example 3
intervals3 = [[1, 3], [3, 5], [5, 8]]
print(solution.canAttendMeetings(intervals3))
# Output: True

# Example 4
intervals4 = [[1, 5], [2, 6], [8, 10]]
print(solution.canAttendMeetings(intervals4))
# Output: False
