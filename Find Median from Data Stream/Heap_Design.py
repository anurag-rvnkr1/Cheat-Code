'''
295. Find Median from Data Stream

The median is the middle value in an ordered integer list.

If the size of the list is even, there is no middle value and the median is
the mean of the two middle values.

Implement the MedianFinder class:

    - MedianFinder() Initializes the object.
    - addNum(num) Adds an integer into the data structure.
    - findMedian() Returns the median of all inserted elements.

Example 1:
    Input:
        ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
        [[],[1],[2],[],[3],[]]

    Output:
        [null,null,null,1.5,null,2.0]

Explanation:
    MedianFinder medianFinder = MedianFinder();
    medianFinder.addNum(1);
    medianFinder.addNum(2);
    medianFinder.findMedian(); // 1.5
    medianFinder.addNum(3);
    medianFinder.findMedian(); // 2.0

Constraints:
    -10^5 <= num <= 10^5
    There will be at least one element before calling findMedian().
    At most 5 * 10^4 calls will be made to addNum() and findMedian().

Follow-up:
    - If all numbers are between 0 and 100, how would you optimize it?
    - If 99% of all numbers are between 0 and 100, how would you optimize it?
'''

# Heap + Design

import heapq


class MedianFinder:

    def __init__(self):
        # Max Heap (store negatives)
        self.max_heap = []

        # Min Heap
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # Step 1: Push into max heap.
        heapq.heappush(self.max_heap, -num)

        # Step 2: Largest from max heap goes to min heap.
        heapq.heappush(
            self.min_heap,
            -heapq.heappop(self.max_heap)
        )

        # Step 3: Balance heaps.
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(
                self.max_heap,
                -heapq.heappop(self.min_heap)
            )

    def findMedian(self) -> float:
        # Odd number of elements.
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])

        # Even number of elements.
        return (
            -self.max_heap[0] + self.min_heap[0]
        ) / 2.0


# Example usage

medianFinder = MedianFinder()

# Example 1
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())
# Output: 1.5

medianFinder.addNum(3)
print(medianFinder.findMedian())
# Output: 2.0

# Example 2
medianFinder2 = MedianFinder()

for num in [5, 15, 1, 3]:
    medianFinder2.addNum(num)

print(medianFinder2.findMedian())
# Output: 4.0

# Example 3
medianFinder3 = MedianFinder()

for num in [2, 4, 6, 8, 10]:
    medianFinder3.addNum(num)

print(medianFinder3.findMedian())
# Output: 6.0

# Example 4
medianFinder4 = MedianFinder()

for num in [7]:
    medianFinder4.addNum(num)

print(medianFinder4.findMedian())
# Output: 7.0
