'''
225. Implement Stack using Queues

Implement a last-in-first-out (LIFO) stack using only two queues.

Implement the MyStack class:

    - MyStack() Initializes the stack.
    - void push(int x) Pushes element x onto the stack.
    - int pop() Removes the element on the top of the stack and returns it.
    - int top() Returns the top element.
    - boolean empty() Returns True if the stack is empty, False otherwise.

Notes:
    - You must use only standard operations of a queue.
    - All operations should be implemented using queues only.

Example 1:
    Input:
        ["MyStack","push","push","top","pop","empty"]
        [[],[1],[2],[],[],[]]

    Output:
        [null,null,null,2,2,false]

Explanation:
    MyStack myStack = new MyStack();
    myStack.push(1);
    myStack.push(2);
    myStack.top();    // 2
    myStack.pop();    // 2
    myStack.empty();  // False

Constraints:
    1 <= x <= 9
    At most 100 calls will be made to push, pop, top, and empty.
    All calls to pop and top are valid.
'''

# Queue Design (Using One Queue)

from collections import deque


class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

        # Rotate the queue so the new element comes to the front.
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Example usage
stack = MyStack()

# Example 1
stack.push(1)
stack.push(2)

print(stack.top())    # Output: 2
print(stack.pop())    # Output: 2
print(stack.empty())  # Output: False

# Example 2
stack.push(3)

print(stack.top())    # Output: 3
print(stack.pop())    # Output: 3
print(stack.pop())    # Output: 1
print(stack.empty())  # Output: True

# Example 3
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.top())    # Output: 30
print(stack.pop())    # Output: 30
print(stack.top())    # Output: 20
