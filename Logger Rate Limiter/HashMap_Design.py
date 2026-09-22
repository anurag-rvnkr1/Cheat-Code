'''
359. Logger Rate Limiter

Design a logger system that receives a stream of messages along with timestamps.

Each unique message should only be printed if it has not been printed in the
last 10 seconds.

Implement the Logger class:

    Logger()
        Initializes the logger.

    bool shouldPrintMessage(int timestamp, string message)
        Returns True if the message should be printed, otherwise False.

Example 1:
    Input:
        ["Logger","shouldPrintMessage","shouldPrintMessage",
         "shouldPrintMessage","shouldPrintMessage",
         "shouldPrintMessage","shouldPrintMessage"]

        [[],
         [1,"foo"],
         [2,"bar"],
         [3,"foo"],
         [8,"bar"],
         [10,"foo"],
         [11,"foo"]]

    Output:
        [null,true,true,false,false,false,true]

Explanation:
        "foo" printed at timestamp 1.
        "foo" cannot be printed again until timestamp 11.

Constraints:
    0 <= timestamp <= 10^9
    Every timestamp is passed in non-decreasing order.
    message consists of lowercase English letters.
    At most 10^4 calls will be made.
'''

# HashMap Design

class Logger:

    def __init__(self):
        # message -> last printed timestamp
        self.last_print_time = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if (
            message not in self.last_print_time or
            timestamp - self.last_print_time[message] >= 10
        ):
            self.last_print_time[message] = timestamp
            return True

        return False


# Example usage
logger = Logger()

print(logger.shouldPrintMessage(1, "foo"))
# Output: True

print(logger.shouldPrintMessage(2, "bar"))
# Output: True

print(logger.shouldPrintMessage(3, "foo"))
# Output: False

print(logger.shouldPrintMessage(8, "bar"))
# Output: False

print(logger.shouldPrintMessage(10, "foo"))
# Output: False

print(logger.shouldPrintMessage(11, "foo"))
# Output: True

print(logger.shouldPrintMessage(21, "foo"))
# Output: True

print(logger.shouldPrintMessage(22, "bar"))
# Output: True

print(logger.shouldPrintMessage(25, "bar"))
# Output: False
