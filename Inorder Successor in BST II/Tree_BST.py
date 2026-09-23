'''
510. Inorder Successor in BST II

Given a node in a Binary Search Tree where each node has a parent pointer,
return its inorder successor.

The inorder successor of a node is the node with the smallest key greater
than the given node.

Return None if no successor exists.

Example 1:
    Input:
        root = [2,1,3]
        node = 1

    Output:
        2

Example 2:
    Input:
        root = [5,3,6,2,4,null,null,1]
        node = 6

    Output:
        None

Constraints:
    Number of nodes is in the range [1,10^4]
    -10^5 <= Node.val <= 10^5
'''

# Binary Search Tree + Parent Pointer


class Node:
    def __init__(
        self,
        val=0,
        left=None,
        right=None,
        parent=None
    ):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class Solution:
    def inorderSuccessor(self, node: "Node") -> "Node":
        # Case 1: Right subtree exists.
        if node.right:
            current = node.right

            while current.left:
                current = current.left

            return current

        # Case 2: Move upward until node becomes a left child.
        current = node

        while current.parent and current.parent.right == current:
            current = current.parent

        return current.parent


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------

solution = Solution()

# Example 1
root1 = Node(2)
root1.left = Node(1, parent=root1)
root1.right = Node(3, parent=root1)

print(solution.inorderSuccessor(root1.left).val)
# Output: 2

# Example 2
root2 = Node(5)
root2.left = Node(3, parent=root2)
root2.right = Node(6, parent=root2)
root2.left.left = Node(2, parent=root2.left)
root2.left.right = Node(4, parent=root2.left)
root2.left.left.left = Node(1, parent=root2.left.left)

print(solution.inorderSuccessor(root2.right))
# Output: None

# Example 3
print(solution.inorderSuccessor(root2.left).val)
# Output: 4

# Example 4
print(solution.inorderSuccessor(root2.left.right).val)
# Output: 5

# Example 5
print(solution.inorderSuccessor(root2.left.left).val)
# Output: 3

# Example 6
print(solution.inorderSuccessor(root2.left.left.left).val)
# Output: 2
