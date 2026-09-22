'''
352. Data Stream as Disjoint Intervals

Given a data stream input of non-negative integers a1, a2, ..., an,
summarize the numbers seen so far as a list of disjoint intervals.

Implement the SummaryRanges class:

    SummaryRanges()
        Initializes the object with an empty stream.

    void addNum(int value)
        Adds the integer value to the stream.

    int[][] getIntervals()
        Returns the disjoint intervals [start, end] sorted by start.

Example 1:
    Input:
        ["SummaryRanges","addNum","getIntervals","addNum","getIntervals",
         "addNum","getIntervals","addNum","getIntervals","addNum",
         "getIntervals","addNum","getIntervals"]

        [[],[1],[],[3],[],[7],[],[2],[],[6],[],[9],[]]

    Output:
        [null,null,[[1,1]],null,[[1,1],[3,3]],null,
         [[1,1],[3,3],[7,7]],null,[[1,3],[7,7]],
         null,[[1,3],[6,7]],null,[[1,3],[6,7],[9,9]]]

Constraints:
    0 <= value <= 10^4
    At most 3 * 10^4 calls will be made to addNum() and getIntervals().
'''

# Interval Design

from typing import List


class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        new_interval = [value, value]
        merged = []
        inserted = False

        for start, end in self.intervals:

            if end + 1 < new_interval[0]:
                merged.append([start, end])

            elif new_interval[1] + 1 < start:
                if not inserted:
                    merged.append(new_interval)
                    inserted = True

                merged.append([start, end])

            else:
                new_interval[0] = min(new_interval[0], start)
                new_interval[1] = max(new_interval[1], end)

        if not inserted:
            merged.append(new_interval)

        self.intervals = merged

    def getIntervals(self) -> List[List[int]]:
        return self.intervals


# Example usage
summaryRanges = SummaryRanges()

summaryRanges.addNum(1)
print(summaryRanges.getIntervals())
# Output: [[1,1]]

summaryRanges.addNum(3)
print(summaryRanges.getIntervals())
# Output: [[1,1],[3,3]]

summaryRanges.addNum(7)
print(summaryRanges.getIntervals())
# Output: [[1,1],[3,3],[7,7]]

summaryRanges.addNum(2)
print(summaryRanges.getIntervals())
# Output: [[1,3],[7,7]]

summaryRanges.addNum(6)
print(summaryRanges.getIntervals())
# Output: [[1,3],[6,7]]

summaryRanges.addNum(9)
print(summaryRanges.getIntervals())
# Output: [[1,3],[6,7],[9,9]]
