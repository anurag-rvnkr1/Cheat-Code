'''
114. Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child
points to the next node in the list and the left child is always null.

The "linked list" should be in the same order as a preorder traversal.

Example 1:
    Input: root = [1,2,5,3,4,null,6]
    Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
    Input: root = []
    Output: []

Example 3:
    Input: root = [0]
    Output: [0]

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100
'''

# Reverse Preorder Depth-First Search (DFS)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.prev = None

        def dfs(node):
            if not node:
                return

            dfs(node.right)
            dfs(node.left)

            node.right = self.prev
            node.left = None
            self.prev = node

        dfs(root)


# Helper function to print flattened tree
def printLinkedList(root):
    while root:
        print(root.val, end=" -> " if root.right else "")
        root = root.right
    print()


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(5)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.right = TreeNode(6)

solution.flatten(root1)
printLinkedList(root1)
# Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6

# Example 2
root2 = None
solution.flatten(root2)
print(root2)
# Output: None

# Example 3
root3 = TreeNode(0)
solution.flatten(root3)
printLinkedList(root3)
# Output: 0
