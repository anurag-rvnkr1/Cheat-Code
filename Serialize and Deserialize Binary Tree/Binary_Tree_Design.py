'''
297. Serialize and Deserialize Binary Tree

Serialization is the process of converting a binary tree into a string so that
it can be stored or transmitted.

Deserialization is the process of reconstructing the binary tree from the
serialized string.

Implement the Codec class:

    - serialize(root): Encodes a binary tree into a single string.
    - deserialize(data): Decodes the encoded string back into the original tree.

You may design your own serialization/deserialization algorithm.

Example 1:
    Input:
        root = [1,2,3,null,null,4,5]

    Output:
        [1,2,3,null,null,4,5]

Example 2:
    Input:
        root = []

    Output:
        []

Constraints:
    The number of nodes is in the range [0, 10^4].
    -1000 <= Node.val <= 1000
'''

# Binary Tree Design (Preorder DFS)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        values = []

        def preorder(node):
            if not node:
                values.append("null")
                return

            values.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(values)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        index = 0

        def build():
            nonlocal index

            if values[index] == "null":
                index += 1
                return None

            node = TreeNode(int(values[index]))
            index += 1

            node.left = build()
            node.right = build()

            return node

        return build()


# Example usage
codec = Codec()

# Example 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(5)

serialized = codec.serialize(root1)
print(serialized)
# Output: "1,2,null,null,3,4,null,null,5,null,null"

deserialized = codec.deserialize(serialized)
print(codec.serialize(deserialized))
# Output: "1,2,null,null,3,4,null,null,5,null,null"

# Example 2
root2 = None

serialized2 = codec.serialize(root2)
print(serialized2)
# Output: "null"

deserialized2 = codec.deserialize(serialized2)
print(codec.serialize(deserialized2))
# Output: "null"

# Example 3
root3 = TreeNode(-1)
root3.left = TreeNode(-2)
root3.right = TreeNode(3)

serialized3 = codec.serialize(root3)
print(serialized3)
# Output: "-1,-2,null,null,3,null,null"

print(codec.serialize(codec.deserialize(serialized3)))
# Output: "-1,-2,null,null,3,null,null"
