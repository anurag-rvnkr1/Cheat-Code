'''
346. Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average
of all integers in the sliding window.

Implement the MovingAverage class:

    MovingAverage(int size)
        Initializes the object with the window size.

    double next(int val)
        Adds val to the stream and returns the moving average of the
        last size values.

Example 1:
    Input:
        ["MovingAverage","next","next","next","next"]
        [[3],[1],[10],[3],[5]]

    Output:
        [null,1.0,5.5,4.66667,6.0]

Explanation:
        MovingAverage movingAverage = new MovingAverage(3);

        movingAverage.next(1);   // 1.0
        movingAverage.next(10);  // (1 + 10) / 2 = 5.5
        movingAverage.next(3);   // (1 + 10 + 3) / 3 = 4.66667
        movingAverage.next(5);   // (10 + 3 + 5) / 3 = 6.0

Constraints:
    1 <= size <= 1000
    -10^5 <= val <= 10^5
    At most 10^4 calls will be made to next().
'''

# Queue + Sliding Window Design

from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.window_size = size
        self.queue = deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.window_sum += val

        if len(self.queue) > self.window_size:
            self.window_sum -= self.queue.popleft()

        return self.window_sum / len(self.queue)


# Example usage
movingAverage = MovingAverage(3)

print(movingAverage.next(1))
# Output: 1.0

print(movingAverage.next(10))
# Output: 5.5

print(movingAverage.next(3))
# Output: 4.666666666666667

print(movingAverage.next(5))
# Output: 6.0

print(movingAverage.next(7))
# Output: 5.0

print(movingAverage.next(-2))
# Output: 3.3333333333333335
