'''
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

Implement the MinStack class:

    - MinStack() initializes the stack object.
    - void push(int val) pushes the element val onto the stack.
    - void pop() removes the element on the top of the stack.
    - int top() gets the top element of the stack.
    - int getMin() retrieves the minimum element in the stack.

Example 1:
    Input:
        ["MinStack","push","push","push","getMin","pop","top","getMin"]
        [[],[-2],[0],[-3],[],[],[],[]]

    Output:
        [null,null,null,null,-3,null,0,-2]

Explanation:
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin(); // return -3
    minStack.pop();
    minStack.top();    // return 0
    minStack.getMin(); // return -2

Constraints:
    -2^31 <= val <= 2^31 - 1
    Methods pop, top, and getMin operations will always be called on non-empty stacks.
    At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
'''

# Stack


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Example usage
minStack = MinStack()

# Example 1
minStack.push(-2)
minStack.push(0)
minStack.push(-3)

print(minStack.getMin())  # Output: -3

minStack.pop()

print(minStack.top())     # Output: 0
print(minStack.getMin())  # Output: -2

# Example 2
stack2 = MinStack()
stack2.push(5)
stack2.push(2)
stack2.push(8)

print(stack2.getMin())    # Output: 2

stack2.pop()

print(stack2.top())       # Output: 2
print(stack2.getMin())    # Output: 2
