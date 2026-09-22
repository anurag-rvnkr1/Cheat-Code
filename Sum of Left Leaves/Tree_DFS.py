'''
404. Sum of Left Leaves

Given the root of a binary tree, return the sum of all left leaves.

A left leaf is a leaf node that is the left child of another node.

Example 1:
    Input:
        root = [3,9,20,null,null,15,7]

    Output:
        24

Explanation:
        Left leaves are 9 and 15.
        Sum = 9 + 15 = 24

Example 2:
    Input:
        root = [1]

    Output:
        0

Constraints:
    The number of nodes is in the range [1, 1000].
    -1000 <= Node.val <= 1000
'''

# Tree DFS

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], is_left: bool) -> int:
            if not node:
                return 0

            # Leaf node.
            if not node.left and not node.right:
                return node.val if is_left else 0

            return (
                dfs(node.left, True) +
                dfs(node.right, False)
            )

        return dfs(root, False)


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

print(solution.sumOfLeftLeaves(root1))
# Output: 24

# Example 2
root2 = TreeNode(1)

print(solution.sumOfLeftLeaves(root2))
# Output: 0

# Example 3
root3 = TreeNode(5)
root3.left = TreeNode(2)
root3.right = TreeNode(8)
root3.left.left = TreeNode(1)
root3.left.right = TreeNode(3)
root3.right.left = TreeNode(6)

print(solution.sumOfLeftLeaves(root3))
# Output: 7

# Example 4
root4 = TreeNode(10)
root4.left = TreeNode(20)
root4.left.left = TreeNode(30)

print(solution.sumOfLeftLeaves(root4))
# Output: 30

# Example 5
root5 = TreeNode(1)
root5.right = TreeNode(2)
root5.right.left = TreeNode(3)
root5.right.right = TreeNode(4)

print(solution.sumOfLeftLeaves(root5))
# Output: 3

# Example 6
root6 = TreeNode(7)
root6.left = TreeNode(5)
root6.right = TreeNode(9)
root6.left.left = TreeNode(4)
root6.left.right = TreeNode(6)
root6.right.left = TreeNode(8)
root6.right.right = TreeNode(10)

print(solution.sumOfLeftLeaves(root6))
# Output: 12
