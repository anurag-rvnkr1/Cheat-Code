'''
362. Design Hit Counter

Design a hit counter that counts the number of hits received
in the past 5 minutes (300 seconds).

Implement the HitCounter class:

    HitCounter()
        Initializes the hit counter.

    void hit(int timestamp)
        Records a hit at the given timestamp.

    int getHits(int timestamp)
        Returns the number of hits in the past 300 seconds
        (including the current timestamp).

Example 1:
    Input:
        ["HitCounter","hit","hit","hit","getHits","hit","getHits","getHits"]

        [[],[1],[2],[3],[4],[300],[300],[301]]

    Output:
        [null,null,null,null,3,null,4,3]

Explanation:
        Hits at timestamps 1, 2, 3, and 300.
        At timestamp 301, the hit at timestamp 1 expires.

Constraints:
    1 <= timestamp <= 2 * 10^9
    All timestamps are passed in non-decreasing order.
    At most 3 * 10^4 calls will be made.
'''

# Queue + Sliding Window Design

from collections import deque


class HitCounter:

    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()

        return len(self.hits)


# Example usage
counter = HitCounter()

counter.hit(1)
counter.hit(2)
counter.hit(3)

print(counter.getHits(4))
# Output: 3

counter.hit(300)

print(counter.getHits(300))
# Output: 4

print(counter.getHits(301))
# Output: 3

counter.hit(302)
counter.hit(303)

print(counter.getHits(303))
# Output: 5

print(counter.getHits(601))
# Output: 0
