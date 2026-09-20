'''
173. Binary Search Tree Iterator

Implement the BSTIterator class that represents an iterator over the in-order
traversal of a Binary Search Tree (BST).

The iterator should support:
    - BSTIterator(TreeNode root) Initializes the iterator.
    - next() Returns the next smallest number in the BST.
    - hasNext() Returns True if there exists a next number.

Example 1:
    Input:
        ["BSTIterator","next","next","hasNext","next","hasNext",
         "next","hasNext","next","hasNext"]
        [[[7,3,15,null,null,9,20]],[],[],[],[],[],[],[],[],[]]

    Output:
        [null,3,7,true,9,true,15,true,20,false]

Explanation:
    In-order traversal of the BST is [3,7,9,15,20].

Constraints:
    The number of nodes in the tree is in the range [1, 10^5].
    0 <= Node.val <= 10^6
    At most 10^5 calls will be made to next() and hasNext().
'''

# Stack (Inorder Traversal)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.pushLeft(root)

    def pushLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()

        if node.right:
            self.pushLeft(node.right)

        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Example usage

# Example BST:
#        7
#      /   \
#     3     15
#          /  \
#         9   20

root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

iterator = BSTIterator(root)

print(iterator.next())      # Output: 3
print(iterator.next())      # Output: 7
print(iterator.hasNext())   # Output: True
print(iterator.next())      # Output: 9
print(iterator.hasNext())   # Output: True
print(iterator.next())      # Output: 15
print(iterator.hasNext())   # Output: True
print(iterator.next())      # Output: 20
print(iterator.hasNext())   # Output: False
