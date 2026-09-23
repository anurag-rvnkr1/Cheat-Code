'''
501. Find Mode in Binary Search Tree

Given the root of a Binary Search Tree (BST) with duplicates, return all the
mode(s) (the most frequently occurring element(s)).

Assume a BST is defined as follows:
    - Left subtree values <= current node value.
    - Right subtree values >= current node value.

Example 1:
    Input:
        root = [1,null,2,2]

    Output:
        [2]

Example 2:
    Input:
        root = [0]

    Output:
        [0]

Constraints:
    Number of nodes is in the range [1, 10^4].
    -10^5 <= Node.val <= 10^5

Follow-up:
    Could you do it without using any extra space?
'''

# Tree + Inorder Traversal (O(1) extra space except recursion stack)

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.previous = None
        self.count = 0
        self.maximum_frequency = 0
        self.answer = []

        def inorder(node: Optional[TreeNode]):
            if not node:
                return

            inorder(node.left)

            # Count frequency of current value.
            if self.previous == node.val:
                self.count += 1
            else:
                self.previous = node.val
                self.count = 1

            # Update modes.
            if self.count > self.maximum_frequency:
                self.maximum_frequency = self.count
                self.answer = [node.val]
            elif self.count == self.maximum_frequency:
                self.answer.append(node.val)

            inorder(node.right)

        inorder(root)
        return self.answer


# -------------------------------------------------------
# Helper Functions (For Testing)
# -------------------------------------------------------

def build_tree(values):
    if not values:
        return None

    nodes = [
        TreeNode(value) if value is not None else None
        for value in values
    ]

    child_index = 1

    for index in range(len(values)):
        if nodes[index]:
            if child_index < len(values):
                nodes[index].left = nodes[child_index]
                child_index += 1

            if child_index < len(values):
                nodes[index].right = nodes[child_index]
                child_index += 1

    return nodes[0]


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------

solution = Solution()

# Example 1
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(2)

print(solution.findMode(root1))
# Output: [2]

# Example 2
root2 = TreeNode(0)
print(solution.findMode(root2))
# Output: [0]

# Example 3
root3 = TreeNode(2)
root3.left = TreeNode(1)
root3.right = TreeNode(2)

print(solution.findMode(root3))
# Output: [2]

# Example 4
root4 = TreeNode(5)
root4.left = TreeNode(3)
root4.right = TreeNode(7)
root4.left.left = TreeNode(3)
root4.left.right = TreeNode(4)
root4.right.left = TreeNode(7)
root4.right.right = TreeNode(8)

print(solution.findMode(root4))
# Output: [3,7]

# Example 5
root5 = TreeNode(1)
root5.left = TreeNode(1)
root5.right = TreeNode(1)

print(solution.findMode(root5))
# Output: [1]

# Example 6
root6 = TreeNode(6)
root6.left = TreeNode(2)
root6.right = TreeNode(8)
root6.left.left = TreeNode(2)
root6.left.right = TreeNode(4)
root6.right.left = TreeNode(8)
root6.right.right = TreeNode(9)

print(solution.findMode(root6))
# Output: [2,8]
