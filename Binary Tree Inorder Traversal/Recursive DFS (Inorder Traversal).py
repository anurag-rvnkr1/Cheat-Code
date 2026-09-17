'''
94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Inorder traversal visits nodes in the order:
Left → Root → Right.

Example 1:
    Input: root = [1,null,2,3]
    Output: [1,3,2]

Example 2:
    Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
    Output: [4,2,6,5,7,1,3,9,8]

Example 3:
    Input: root = []
    Output: []

Example 4:
    Input: root = [1]
    Output: [1]

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
'''

# Recursive DFS (Inorder Traversal)
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)

        return result


# Example usage
solution = Solution()

# Example 1: [1,null,2,3]
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
print(solution.inorderTraversal(root1))  # Output: [1,3,2]

# Example 2: [1,2,3,4,5,null,8,null,null,6,7,9]
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.left.right.left = TreeNode(6)
root2.left.right.right = TreeNode(7)
root2.right.right = TreeNode(8)
root2.right.right.left = TreeNode(9)
print(solution.inorderTraversal(root2))  # Output: [4,2,6,5,7,1,3,9,8]

# Example 3: Empty tree
print(solution.inorderTraversal(None))  # Output: []

# Example 4: Single node
root4 = TreeNode(1)
print(solution.inorderTraversal(root4))  # Output: [1]
