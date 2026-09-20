'''
117. Populating Next Right Pointers in Each Node II

Given a binary tree, populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to None.

Initially, all next pointers are set to None.

Unlike Problem 116, the tree is not necessarily a perfect binary tree.

Example 1:
    Input: root = [1,2,3,4,5,null,7]
    Output: [1,#,2,3,#,4,5,7,#]

Example 2:
    Input: root = []
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 6000].
    -100 <= Node.val <= 100
'''

# Breadth-First Search (Level Order Traversal)

from typing import Optional
from collections import deque


class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
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
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if i < level_size - 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root


# Helper function to print next pointers level by level
def printNextPointers(root):
    if not root:
        print(None)
        return

    queue = deque([root])

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            if node.next:
                print(f"{node.val}->{node.next.val}", end="  ")
            else:
                print(f"{node.val}->None", end="  ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        print()


# Example usage
solution = Solution()

# Example 1
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.right = Node(7)

solution.connect(root1)
printNextPointers(root1)

# Output:
# 1->None
# 2->3  3->None
# 4->5  5->7  7->None

# Example 2
root2 = None
solution.connect(root2)
printNextPointers(root2)

# Output:
# None
