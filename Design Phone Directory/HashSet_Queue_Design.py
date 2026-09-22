'''
379. Design Phone Directory

Design a phone directory that supports:

    - get(): Provide an available number.
    - check(number): Check if a number is available.
    - release(number): Recycle or release a number.

Implement the PhoneDirectory class:

    PhoneDirectory(int maxNumbers)
        Initializes the directory with numbers from 0 to maxNumbers - 1.

    int get()
        Returns an available number.
        Returns -1 if none is available.

    bool check(int number)
        Returns True if the number is available.

    void release(int number)
        Releases the number back to the directory.

Example 1:
    Input:
        ["PhoneDirectory","get","get","check","get",
         "check","release","check"]

        [[3],[],[],[2],[],[2],[2],[2]]

    Output:
        [null,0,1,true,2,false,null,true]

Constraints:
    1 <= maxNumbers <= 10^4
    0 <= number < maxNumbers
    At most 2 * 10^4 calls will be made.
'''

# Queue + HashSet Design

from collections import deque


class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.available = deque(range(maxNumbers))
        self.used = set()
        self.maxNumbers = maxNumbers

    def get(self) -> int:
        if not self.available:
            return -1

        number = self.available.popleft()
        self.used.add(number)

        return number

    def check(self, number: int) -> bool:
        return (
            0 <= number < self.maxNumbers and
            number not in self.used
        )

    def release(self, number: int) -> None:
        if number in self.used:
            self.used.remove(number)
            self.available.append(number)


# Example usage
directory = PhoneDirectory(3)

print(directory.get())
# Output: 0

print(directory.get())
# Output: 1

print(directory.check(2))
# Output: True

print(directory.get())
# Output: 2

print(directory.check(2))
# Output: False

directory.release(2)

print(directory.check(2))
# Output: True

print(directory.get())
# Output: 2

print(directory.get())
# Output: -1
