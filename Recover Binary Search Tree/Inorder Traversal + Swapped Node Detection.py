'''
99. Recover Binary Search Tree

You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake.

Recover the tree without changing its structure.

Example 1:
    Input: root = [1,3,null,null,2]
    Output: [3,1,null,null,2]
    Explanation:
    Swapping the values 1 and 3 restores the BST.

Example 2:
    Input: root = [3,1,4,null,null,2]
    Output: [2,1,4,null,null,3]
    Explanation:
    Swapping the values 2 and 3 restores the BST.

Constraints:
    The number of nodes in the tree is in the range [2, 1000].
    -2^31 <= Node.val <= 2^31 - 1

Follow up:
    A solution using O(n) space is straightforward.
    Can you solve it using constant O(1) extra space?
'''

# Inorder Traversal + Swapped Node Detection
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:

        first = None
        second = None
        prev = TreeNode(float('-inf'))

        def inorder(node):
            nonlocal first, second, prev

            if not node:
                return

            inorder(node.left)

            # Detect swapped nodes
            if prev.val > node.val:
                if first is None:
                    first = prev
                second = node

            prev = node

            inorder(node.right)

        inorder(root)

        # Swap the values of the misplaced nodes
        first.val, second.val = second.val, first.val


# Example usage
def inorder_values(root):
    result = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)

    dfs(root)
    return result


solution = Solution()

# Example 1
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.left.right = TreeNode(2)

solution.recoverTree(root1)
print(inorder_values(root1))  # Output: [1,2,3]

# Example 2
root2 = TreeNode(3)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(2)

solution.recoverTree(root2)
print(inorder_values(root2))  # Output: [1,2,3,4]
