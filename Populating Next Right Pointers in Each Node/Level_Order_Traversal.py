'''
116. Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level,
and every parent has two children.

Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to None.

Initially, all next pointers are set to None.

Example 1:
    Input: root = [1,2,3,4,5,6,7]
    Output: [1,#,2,3,#,4,5,6,7,#]

Example 2:
    Input: root = []
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 2^12 - 1].
    -1000 <= Node.val <= 1000
'''

# Level Order Traversal (Breadth-First Search)

from typing import Optional
from collections import deque


class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None

        queue = deque([root])

        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.popleft()

                if i < size - 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root


# Helper function to print next pointers level by level
def printNextPointers(root):
    level = root

    while level:
        current = level

        while current:
            print(current.val, end=" -> ")
            current = current.next

        print("None")
        level = level.left


# Example usage
solution = Solution()

# Example 1
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.left = Node(6)
root1.right.right = Node(7)

solution.connect(root1)
printNextPointers(root1)
# Output:
# 1 -> None
# 2 -> 3 -> None
# 4 -> 5 -> 6 -> 7 -> None

# Example 2
root2 = None
print(solution.connect(root2))
# Output: None
