'''
426. Convert Binary Search Tree to Sorted Doubly Linked List

Convert a Binary Search Tree into a sorted circular doubly linked list in-place.

Each node's left pointer points to its predecessor.
Each node's right pointer points to its successor.

The predecessor of the smallest node is the largest node.
The successor of the largest node is the smallest node.

Return the head of the circular doubly linked list.

Example 1:
    Input:
        root = [4,2,5,1,3]

    Output:
        [1,2,3,4,5]

Example 2:
    Input:
        root = [2,1,3]

    Output:
        [1,2,3]

Example 3:
    Input:
        root = []

    Output:
        []

Constraints:
    Number of nodes is in the range [0, 2000].
    -1000 <= Node.val <= 1000
    The tree is a Binary Search Tree.
'''

# Tree DFS + Inorder Traversal

from typing import Optional


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None

        first = None
        last = None

        def inorder(node: Optional[Node]) -> None:
            nonlocal first, last

            if not node:
                return

            inorder(node.left)

            if last:
                last.right = node
                node.left = last
            else:
                first = node

            last = node

            inorder(node.right)

        inorder(root)

        # Make the list circular.
        first.left = last
        last.right = first

        return first


# -----------------------------
# Helper Functions for Testing
# -----------------------------

def print_circular_list(head: Optional[Node], count: int):
    if not head:
        print([])
        return

    result = []
    current = head

    for _ in range(count):
        result.append(current.val)
        current = current.right

    print(result)


# Example usage

# Example 1
root1 = Node(4)
root1.left = Node(2)
root1.right = Node(5)
root1.left.left = Node(1)
root1.left.right = Node(3)

head1 = Solution().treeToDoublyList(root1)
print_circular_list(head1, 5)
# Output: [1,2,3,4,5]

# Example 2
root2 = Node(2)
root2.left = Node(1)
root2.right = Node(3)

head2 = Solution().treeToDoublyList(root2)
print_circular_list(head2, 3)
# Output: [1,2,3]

# Example 3
root3 = None

head3 = Solution().treeToDoublyList(root3)
print(head3)
# Output: None

# Example 4
root4 = Node(1)

head4 = Solution().treeToDoublyList(root4)
print_circular_list(head4, 1)
# Output: [1]

# Example 5
root5 = Node(3)
root5.left = Node(2)
root5.left.left = Node(1)

head5 = Solution().treeToDoublyList(root5)
print_circular_list(head5, 3)
# Output: [1,2,3]

# Example 6
root6 = Node(1)
root6.right = Node(2)
root6.right.right = Node(3)

head6 = Solution().treeToDoublyList(root6)
print_circular_list(head6, 3)
# Output: [1,2,3]
