'''
284. Peeking Iterator

Design an iterator that supports the peek operation.

Implement the PeekingIterator class:

    - PeekingIterator(iterator) Initializes the object with the given iterator.
    - peek() Returns the next element without advancing the iterator.
    - next() Returns the next element and advances the iterator.
    - hasNext() Returns True if there are more elements.

Example 1:
    Input:
        iterator = [1,2,3]

        peek()
        next()
        peek()
        next()
        next()
        hasNext()

    Output:
        1
        1
        2
        2
        3
        False

Explanation:
    peek() does not move the iterator forward.

Constraints:
    1 <= nums.length <= 1000

Follow-up:
    How would you extend this idea to support multiple peek operations?
'''

# Design + Iterator


class Iterator:
    """
    Mock Iterator class for local testing.
    LeetCode provides this implementation.
    """

    def __init__(self, nums):
        self.nums = nums
        self.index = 0

    def hasNext(self):
        return self.index < len(self.nums)

    def next(self):
        value = self.nums[self.index]
        self.index += 1
        return value


class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator

        # Cache the first element.
        self.next_value = iterator.next() if iterator.hasNext() else None

    def peek(self):
        return self.next_value

    def next(self):
        current = self.next_value

        if self.iterator.hasNext():
            self.next_value = self.iterator.next()
        else:
            self.next_value = None

        return current

    def hasNext(self):
        return self.next_value is not None


# Example usage

# Example 1
iterator1 = Iterator([1, 2, 3])
peek_iterator1 = PeekingIterator(iterator1)

print(peek_iterator1.peek())
# Output: 1

print(peek_iterator1.next())
# Output: 1

print(peek_iterator1.peek())
# Output: 2

print(peek_iterator1.next())
# Output: 2

print(peek_iterator1.next())
# Output: 3

print(peek_iterator1.hasNext())
# Output: False


# Example 2
iterator2 = Iterator([5])
peek_iterator2 = PeekingIterator(iterator2)

print(peek_iterator2.peek())
# Output: 5

print(peek_iterator2.next())
# Output: 5

print(peek_iterator2.hasNext())
# Output: False


# Example 3
iterator3 = Iterator([10, 20])

peek_iterator3 = PeekingIterator(iterator3)

print(peek_iterator3.peek())
# Output: 10

print(peek_iterator3.peek())
# Output: 10

print(peek_iterator3.next())
# Output: 10

print(peek_iterator3.peek())
# Output: 20
