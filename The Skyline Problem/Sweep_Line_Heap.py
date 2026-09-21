'''
218. The Skyline Problem

A city's skyline is the outer contour of the silhouette formed by all the buildings
when viewed from a distance.

You are given an array buildings where buildings[i] = [lefti, righti, heighti]
represents the ith building.

Return the skyline formed by these buildings as a list of key points.

A key point is the left endpoint of a horizontal segment where the skyline height changes.

Example 1:
    Input:
        buildings = [
            [2,9,10],
            [3,7,15],
            [5,12,12],
            [15,20,10],
            [19,24,8]
        ]

    Output:
        [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

Example 2:
    Input: buildings = [[0,2,3],[2,5,3]]
    Output: [[0,3],[5,0]]

Constraints:
    1 <= buildings.length <= 10^4
    0 <= lefti < righti <= 2^31 - 1
    1 <= heighti <= 2^31 - 1
    buildings is sorted by lefti in non-decreasing order.
'''

# Sweep Line + Max Heap

from typing import List
import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Create start and end events.
        events = []

        for left, right, height in buildings:
            events.append((left, -height, right))  # Building starts.
            events.append((right, 0, 0))           # Building ends.

        # Sort events by x-coordinate.
        events.sort()

        result = []
        max_heap = [(0, float("inf"))]  # (-height, right)

        for x, neg_height, right in events:

            # Remove buildings that ended before current x.
            while max_heap and max_heap[0][1] <= x:
                heapq.heappop(max_heap)

            # Add new building starting at x.
            if neg_height != 0:
                heapq.heappush(max_heap, (neg_height, right))

            current_height = -max_heap[0][0]

            # Add key point if skyline height changes.
            if not result or result[-1][1] != current_height:
                result.append([x, current_height])

        return result


# Example usage
solution = Solution()

# Example 1
buildings1 = [
    [2, 9, 10],
    [3, 7, 15],
    [5, 12, 12],
    [15, 20, 10],
    [19, 24, 8]
]

print(solution.getSkyline(buildings1))
# Output:
# [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

# Example 2
buildings2 = [
    [0, 2, 3],
    [2, 5, 3]
]

print(solution.getSkyline(buildings2))
# Output:
# [[0,3],[5,0]]

# Example 3
buildings3 = [
    [1, 5, 3],
    [2, 6, 4],
    [5, 8, 2]
]

print(solution.getSkyline(buildings3))
# Output:
# [[1,3],[2,4],[6,2],[8,0]]
