'''
232. Implement Queue using Stacks

Implement a first-in-first-out (FIFO) queue using only two stacks.

Implement the MyQueue class:

    - MyQueue() Initializes the queue.
    - void push(int x) Pushes element x to the back of the queue.
    - int pop() Removes the element from the front of the queue and returns it.
    - int peek() Returns the front element.
    - boolean empty() Returns True if the queue is empty, False otherwise.

Notes:
    - You must use only standard stack operations.
    - All operations should be implemented using stacks only.

Example 1:
    Input:
        ["MyQueue","push","push","peek","pop","empty"]
        [[],[1],[2],[],[],[]]

    Output:
        [null,null,null,1,1,false]

Explanation:
    MyQueue myQueue = new MyQueue();
    myQueue.push(1);
    myQueue.push(2);
    myQueue.peek();    // 1
    myQueue.pop();     // 1
    myQueue.empty();   // False

Constraints:
    1 <= x <= 9
    At most 100 calls will be made to push, pop, peek, and empty.
    All calls to pop and peek are valid.

Follow-up:
    Can you implement the queue so that each operation is amortized O(1)?
'''

# Stack Design (Using Two Stacks)


class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        self._transfer()
        return self.output_stack.pop()

    def peek(self) -> int:
        self._transfer()
        return self.output_stack[-1]

    def empty(self) -> bool:
        return len(self.input_stack) == 0 and len(self.output_stack) == 0

    def _transfer(self) -> None:
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())


# Example usage
queue = MyQueue()

# Example 1
queue.push(1)
queue.push(2)

print(queue.peek())   # Output: 1
print(queue.pop())    # Output: 1
print(queue.empty())  # Output: False

# Example 2
queue.push(3)
queue.push(4)

print(queue.pop())    # Output: 2
print(queue.peek())   # Output: 3

# Example 3
print(queue.pop())    # Output: 3
print(queue.pop())    # Output: 4
print(queue.empty())  # Output: True

# Example 4
queue.push(10)
print(queue.peek())   # Output: 10
print(queue.pop())    # Output: 10
print(queue.empty())  # Output: True
