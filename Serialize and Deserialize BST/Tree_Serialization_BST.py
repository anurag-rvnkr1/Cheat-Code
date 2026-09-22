'''
449. Serialize and Deserialize BST

Design an algorithm to serialize and deserialize a Binary Search Tree (BST).

Serialization converts a BST into a string.
Deserialization reconstructs the original BST from the string.

The encoded string should be compact.

Example 1:
    Input:
        root = [2,1,3]

    Output:
        Serialized string and reconstructed BST.

Example 2:
    Input:
        root = []

    Output:
        ""

Constraints:
    Number of nodes is in the range [0, 10^4].
    0 <= Node.val <= 10^4
    The tree is guaranteed to be a valid BST.
'''

# Tree Serialization + BST Reconstruction (Preorder + Bounds)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    # Serialize using preorder traversal.
    def serialize(self, root: Optional[TreeNode]) -> str:
        values = []

        def preorder(node: Optional[TreeNode]):
            if not node:
                return

            values.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return ",".join(values)

    # Deserialize using BST bounds.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        preorder_values = list(map(int, data.split(",")))
        index = 0

        def build(lower: int, upper: int) -> Optional[TreeNode]:
            nonlocal index

            if index == len(preorder_values):
                return None

            value = preorder_values[index]

            if value < lower or value > upper:
                return None

            index += 1

            node = TreeNode(value)
            node.left = build(lower, value)
            node.right = build(value, upper)

            return node

        return build(float("-inf"), float("inf"))


# -----------------------------
# Helper Function for Testing
# -----------------------------

def preorder(node: Optional[TreeNode]):
    if not node:
        return []

    return (
        [node.val] +
        preorder(node.left) +
        preorder(node.right)
    )


# Example usage
codec = Codec()

# Example 1
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)

serialized1 = codec.serialize(root1)
print(serialized1)
# Output: "2,1,3"

deserialized1 = codec.deserialize(serialized1)
print(preorder(deserialized1))
# Output: [2,1,3]

# Example 2
root2 = None

serialized2 = codec.serialize(root2)
print(serialized2)
# Output: ""

deserialized2 = codec.deserialize(serialized2)
print(deserialized2)
# Output: None

# Example 3
root3 = TreeNode(8)
root3.left = TreeNode(5)
root3.left.left = TreeNode(1)
root3.left.right = TreeNode(7)
root3.right = TreeNode(10)
root3.right.right = TreeNode(12)

serialized3 = codec.serialize(root3)
print(serialized3)

deserialized3 = codec.deserialize(serialized3)
print(preorder(deserialized3))
# Output: [8,5,1,7,10,12]

# Example 4
root4 = TreeNode(1)

serialized4 = codec.serialize(root4)
print(serialized4)
# Output: "1"

deserialized4 = codec.deserialize(serialized4)
print(preorder(deserialized4))
# Output: [1]

# Example 5
root5 = TreeNode(50)
root5.left = TreeNode(30)
root5.right = TreeNode(70)
root5.left.left = TreeNode(20)
root5.left.right = TreeNode(40)
root5.right.left = TreeNode(60)
root5.right.right = TreeNode(80)

serialized5 = codec.serialize(root5)
print(serialized5)

deserialized5 = codec.deserialize(serialized5)
print(preorder(deserialized5))
# Output: [50,30,20,40,70,60,80]

# Example 6
root6 = TreeNode(5)
root6.right = TreeNode(9)
root6.right.left = TreeNode(8)

serialized6 = codec.serialize(root6)
print(serialized6)

deserialized6 = codec.deserialize(serialized6)
print(preorder(deserialized6))
# Output: [5,9,8]
