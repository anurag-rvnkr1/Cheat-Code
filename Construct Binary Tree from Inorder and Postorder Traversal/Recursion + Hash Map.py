'''
106. Construct Binary Tree from Inorder and Postorder Traversal

Given two integer arrays inorder and postorder where inorder is the inorder traversal
of a binary tree and postorder is the postorder traversal of the same tree, construct
and return the binary tree.

Example 1:
    Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
    Output: [3,9,20,null,null,15,7]

Example 2:
    Input: inorder = [-1], postorder = [-1]
    Output: [-1]

Constraints:
    1 <= inorder.length <= 3000
    postorder.length == inorder.length
    -3000 <= inorder[i], postorder[i] <= 3000
    inorder and postorder consist of unique values.
    Each value of postorder also appears in inorder.
'''

# Recursion + Hash Map
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        inorder_index = {value: index for index, value in enumerate(inorder)}
        postorder_index = len(postorder) - 1

        def build(left, right):
            nonlocal postorder_index

            if left > right:
                return None

            root_value = postorder[postorder_index]
            postorder_index -= 1

            root = TreeNode(root_value)

            mid = inorder_index[root_value]

            # Build right subtree first because postorder is processed backwards
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)


# Example usage
def level_order(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    return result


solution = Solution()

root1 = solution.buildTree([9,3,15,20,7], [9,15,7,20,3])
print(level_order(root1))  # Output: [3,9,20,None,None,15,7]

root2 = solution.buildTree([-1], [-1])
print(level_order(root2))  # Output: [-1]
```
