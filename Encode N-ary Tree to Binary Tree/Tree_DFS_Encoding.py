'''
431. Encode N-ary Tree to Binary Tree

Design an algorithm to encode an N-ary tree into a binary tree and decode it back.

Encoding Rule (Left-Child Right-Sibling Representation):
    - Binary node.left  -> First child of N-ary node.
    - Binary node.right -> Next sibling of N-ary node.

Return the binary tree root after encoding and reconstruct the original N-ary tree
after decoding.

Example 1:
    Input:
        N-ary Tree = [1,null,3,2,4,null,5,6]

    Output:
        Equivalent Binary Tree and reconstructed N-ary Tree.

Example 2:
    Input:
        N-ary Tree = [1,null,2,3,4,5]

    Output:
        Equivalent Binary Tree and reconstructed N-ary Tree.

Constraints:
    Number of nodes <= 10^4
    Maximum depth <= 1000
    Node values are unique.
'''

# Tree DFS Encoding (Left-Child Right-Sibling)

from typing import List


# Definition for an N-ary tree node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    # Encodes an N-ary tree to a binary tree.
    def encode(self, root: "Node") -> TreeNode:
        if not root:
            return None

        binary_root = TreeNode(root.val)

        if root.children:
            binary_root.left = self.encode(root.children[0])

            current = binary_root.left

            for child in root.children[1:]:
                current.right = self.encode(child)
                current = current.right

        return binary_root

    # Decodes the binary tree back to an N-ary tree.
    def decode(self, root: TreeNode) -> "Node":
        if not root:
            return None

        nary_root = Node(root.val, [])

        current = root.left

        while current:
            nary_root.children.append(self.decode(current))
            current = current.right

        return nary_root


# -----------------------------
# Helper Functions for Testing
# -----------------------------

def level_order_nary(root: Node):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        result.append(node.val)

        for child in node.children:
            queue.append(child)

    return result


def preorder_binary(root: TreeNode):
    if not root:
        return []

    return (
        [root.val] +
        preorder_binary(root.left) +
        preorder_binary(root.right)
    )


# Example usage
codec = Codec()

# Example 1
root1 = Node(1, [
    Node(3, [Node(5), Node(6)]),
    Node(2),
    Node(4)
])

binary1 = codec.encode(root1)
print(preorder_binary(binary1))
# Output: Binary preorder traversal.

decoded1 = codec.decode(binary1)
print(level_order_nary(decoded1))
# Output: [1,3,2,4,5,6]

# Example 2
root2 = Node(10, [
    Node(20),
    Node(30, [Node(40), Node(50)]),
    Node(60)
])

binary2 = codec.encode(root2)
print(preorder_binary(binary2))

decoded2 = codec.decode(binary2)
print(level_order_nary(decoded2))
# Output: [10,20,30,60,40,50]

# Example 3
root3 = Node(7)

binary3 = codec.encode(root3)
print(preorder_binary(binary3))
# Output: [7]

decoded3 = codec.decode(binary3)
print(level_order_nary(decoded3))
# Output: [7]

# Example 4
root4 = None

binary4 = codec.encode(root4)
print(binary4)
# Output: None

decoded4 = codec.decode(binary4)
print(decoded4)
# Output: None

# Example 5
root5 = Node(100, [
    Node(200),
    Node(300),
    Node(400)
])

binary5 = codec.encode(root5)
print(preorder_binary(binary5))

decoded5 = codec.decode(binary5)
print(level_order_nary(decoded5))
# Output: [100,200,300,400]

# Example 6
root6 = Node(1, [
    Node(2, [
        Node(5),
        Node(6)
    ]),
    Node(3),
    Node(4, [
        Node(7)
    ])
])

binary6 = codec.encode(root6)
print(preorder_binary(binary6))

decoded6 = codec.decode(binary6)
print(level_order_nary(decoded6))
# Output: [1,2,3,4,5,6,7]
