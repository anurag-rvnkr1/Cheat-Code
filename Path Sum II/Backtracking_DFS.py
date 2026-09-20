'''
113. Path Sum II

Given the root of a binary tree and an integer targetSum, return all root-to-leaf
paths where the sum of the node values in the path equals targetSum.

A leaf is a node with no children.

Example 1:
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    Output: [[5,4,11,2],[5,8,4,5]]

Example 2:
    Input: root = [1,2,3], targetSum = 5
    Output: []

Example 3:
    Input: root = [1,2], targetSum = 0
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000
'''

# Backtracking + Depth-First Search (DFS)

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, remaining_sum, path):
            if not node:
                return

            path.append(node.val)
            remaining_sum -= node.val

            # Leaf node with required sum
            if not node.left and not node.right and remaining_sum == 0:
                result.append(path[:])
            else:
                dfs(node.left, remaining_sum, path)
                dfs(node.right, remaining_sum, path)

            # Backtrack
            path.pop()

        dfs(root, targetSum, [])
        return result


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(5)
root1.left = TreeNode(4)
root1.right = TreeNode(8)
root1.left.left = TreeNode(11)
root1.left.left.left = TreeNode(7)
root1.left.left.right = TreeNode(2)
root1.right.left = TreeNode(13)
root1.right.right = TreeNode(4)
root1.right.right.left = TreeNode(5)
root1.right.right.right = TreeNode(1)

print(solution.pathSum(root1, 22))
# Output: [[5,4,11,2], [5,8,4,5]]

# Example 2
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

print(solution.pathSum(root2, 5))
# Output: []

# Example 3
root3 = TreeNode(1)
root3.left = TreeNode(2)

print(solution.pathSum(root3, 0))
# Output: []
