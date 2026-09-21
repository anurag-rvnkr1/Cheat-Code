'''
253. Meeting Rooms II

Given an array of meeting time intervals intervals where
intervals[i] = [starti, endi], return the minimum number of conference rooms
required.

Example 1:
    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: 2

Explanation:
    Two meetings overlap, so two conference rooms are required.

Example 2:
    Input: intervals = [[7,10],[2,4]]
    Output: 1

Explanation:
    Meetings do not overlap.

Constraints:
    1 <= intervals.length <= 10^4
    intervals[i].length == 2
    0 <= starti < endi <= 10^6
'''

# Heap + Intervals

from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort meetings by start time.
        intervals.sort(key=lambda interval: interval[0])

        # Min heap stores ending times of ongoing meetings.
        min_heap = [intervals[0][1]]

        for start, end in intervals[1:]:

            # Reuse a room if the earliest meeting has ended.
            if start >= min_heap[0]:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, end)

        return len(min_heap)


# Example usage
solution = Solution()

# Example 1
intervals1 = [[0, 30], [5, 10], [15, 20]]
print(solution.minMeetingRooms(intervals1))
# Output: 2

# Example 2
intervals2 = [[7, 10], [2, 4]]
print(solution.minMeetingRooms(intervals2))
# Output: 1

# Example 3
intervals3 = [[1, 5], [2, 6], [4, 8], [9, 10]]
print(solution.minMeetingRooms(intervals3))
# Output: 3

# Example 4
intervals4 = [[1, 3], [3, 5], [5, 7]]
print(solution.minMeetingRooms(intervals4))
# Output: 1
