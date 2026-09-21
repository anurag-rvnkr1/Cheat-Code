'''
257. Binary Tree Paths

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no left or right child.

Example 1:
    Input: root = [1,2,3,null,5]
    Output: ["1->2->5","1->3"]

Explanation:
        1
       / \
      2   3
       \
        5

    Root-to-leaf paths are:
    1 -> 2 -> 5
    1 -> 3

Example 2:
    Input: root = [1]
    Output: ["1"]

Constraints:
    The number of nodes in the tree is in the range [1, 100].
    -100 <= Node.val <= 100
'''

# Depth-First Search (Binary Tree)

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def dfs(node: Optional[TreeNode], current_path: List[str]):
            if not node:
                return

            # Add current node to the path.
            current_path.append(str(node.val))

            # Leaf node: save the completed path.
            if not node.left and not node.right:
                paths.append("->".join(current_path))

            else:
                dfs(node.left, current_path)
                dfs(node.right, current_path)

            # Backtrack.
            current_path.pop()

        dfs(root, [])
        return paths


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(5)

print(solution.binaryTreePaths(root1))
# Output: ['1->2->5', '1->3']

# Example 2
root2 = TreeNode(1)

print(solution.binaryTreePaths(root2))
# Output: ['1']

# Example 3
root3 = TreeNode(10)
root3.left = TreeNode(20)
root3.right = TreeNode(30)
root3.left.left = TreeNode(40)
root3.left.right = TreeNode(50)

print(solution.binaryTreePaths(root3))
# Output: ['10->20->40', '10->20->50', '10->30']

# Example 4
root4 = TreeNode(-1)
root4.left = TreeNode(-2)

print(solution.binaryTreePaths(root4))
# Output: ['-1->-2']
