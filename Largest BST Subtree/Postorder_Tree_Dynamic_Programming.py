'''
333. Largest BST Subtree

Given the root of a binary tree, return the size of the largest subtree
which is also a Binary Search Tree (BST).

A subtree must include all descendants of a node.

Example 1:
    Input:
        root = [10,5,15,1,8,null,7]

    Output:
        3

Explanation:
        Largest BST subtree:
            5
           / \
          1   8

Example 2:
    Input:
        root = [4,2,7,2,3,5,null,2,null,null,null,null,null,1]

    Output:
        2

Example 3:
    Input:
        root = [1]

    Output:
        1

Constraints:
    The number of nodes is in the range [0, 10^4].
    -10^4 <= Node.val <= 10^4
'''

# Postorder Traversal + Tree Dynamic Programming

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.maximum_size = 0

        def dfs(node: Optional[TreeNode]):
            # Returns:
            # (is_bst, subtree_size, minimum_value, maximum_value)

            if not node:
                return (True, 0, float("inf"), float("-inf"))

            left_bst, left_size, left_min, left_max = dfs(node.left)
            right_bst, right_size, right_min, right_max = dfs(node.right)

            if left_bst and right_bst and left_max < node.val < right_min:
                current_size = left_size + right_size + 1

                self.maximum_size = max(
                    self.maximum_size,
                    current_size
                )

                return (
                    True,
                    current_size,
                    min(left_min, node.val),
                    max(right_max, node.val)
                )

            return (False, 0, 0, 0)

        dfs(root)

        return self.maximum_size


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(10)
root1.left = TreeNode(5)
root1.right = TreeNode(15)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(8)
root1.right.right = TreeNode(7)

print(solution.largestBSTSubtree(root1))
# Output: 3

# Example 2
root2 = TreeNode(4)
root2.left = TreeNode(2)
root2.right = TreeNode(7)
root2.left.left = TreeNode(2)
root2.left.right = TreeNode(3)
root2.right.left = TreeNode(5)

print(solution.largestBSTSubtree(root2))
# Output: 2

# Example 3
root3 = TreeNode(1)

print(solution.largestBSTSubtree(root3))
# Output: 1

# Example 4
root4 = TreeNode(2)
root4.left = TreeNode(1)
root4.right = TreeNode(3)

print(solution.largestBSTSubtree(root4))
# Output: 3

# Example 5
root5 = TreeNode(5)
root5.left = TreeNode(4)
root5.right = TreeNode(6)
root5.right.left = TreeNode(3)
root5.right.right = TreeNode(7)

print(solution.largestBSTSubtree(root5))
# Output: 3

# Example 6
root6 = TreeNode(8)
root6.left = TreeNode(5)
root6.right = TreeNode(9)
root6.left.left = TreeNode(1)
root6.left.right = TreeNode(7)

print(solution.largestBSTSubtree(root6))
# Output: 5
