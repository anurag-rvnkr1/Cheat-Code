'''
103. Binary Tree Zigzag Level Order Traversal

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.

(Zigzag traversal visits nodes level by level, alternating between left-to-right and right-to-left.)

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[20,9],[15,7]]

Example 2:
    Input: root = [1]
    Output: [[1]]

Example 3:
    Input: root = []
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100
'''

# BFS with Alternating Level Direction
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level = deque()

            for _ in range(len(queue)):
                node = queue.popleft()

                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(list(level))
            left_to_right = not left_to_right

        return result


# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

print(solution.zigzagLevelOrder(root1))  # Output: [[3],[20,9],[15,7]]

# Example 2
root2 = TreeNode(1)
print(solution.zigzagLevelOrder(root2))  # Output: [[1]]

# Example 3
print(solution.zigzagLevelOrder(None))  # Output: []
```
