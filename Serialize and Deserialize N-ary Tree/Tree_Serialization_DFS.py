'''
428. Serialize and Deserialize N-ary Tree

Design an algorithm to serialize and deserialize an N-ary tree.

Serialization is the process of converting a tree into a string so it can be
stored or transmitted.

Deserialization reconstructs the original tree from that string.

Example 1:
    Input:
        root = [1,null,3,2,4,null,5,6]

    Output:
        Serialized string and reconstructed tree.

Example 2:
    Input:
        root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10]

    Output:
        Serialized string and reconstructed tree.

Constraints:
    Number of nodes is in the range [0, 10^4].
    0 <= Node.val <= 10^4
    Maximum depth <= 1000.
'''

# Tree Serialization + DFS

from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Codec:
    def serialize(self, root: "Node") -> str:
        values = []

        def dfs(node: "Node"):
            if not node:
                return

            values.append(str(node.val))
            values.append(str(len(node.children)))

            for child in node.children:
                dfs(child)

        dfs(root)

        return ",".join(values)

    def deserialize(self, data: str) -> "Node":
        if not data:
            return None

        tokens = data.split(",")
        index = 0

        def dfs():
            nonlocal index

            value = int(tokens[index])
            index += 1

            child_count = int(tokens[index])
            index += 1

            node = Node(value)

            for _ in range(child_count):
                node.children.append(dfs())

            return node

        return dfs()


# -----------------------------
# Helper Function for Testing
# -----------------------------

def level_order(root: Node):
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


# Example usage
codec = Codec()

# Example 1
root1 = Node(1, [
    Node(3, [Node(5), Node(6)]),
    Node(2),
    Node(4)
])

serialized1 = codec.serialize(root1)
print(serialized1)

deserialized1 = codec.deserialize(serialized1)
print(level_order(deserialized1))
# Output: [1,3,2,4,5,6]

# Example 2
root2 = Node(10, [
    Node(20),
    Node(30, [Node(40), Node(50)])
])

serialized2 = codec.serialize(root2)
print(serialized2)

deserialized2 = codec.deserialize(serialized2)
print(level_order(deserialized2))
# Output: [10,20,30,40,50]

# Example 3
root3 = Node(7)

serialized3 = codec.serialize(root3)
print(serialized3)

deserialized3 = codec.deserialize(serialized3)
print(level_order(deserialized3))
# Output: [7]

# Example 4
root4 = None

serialized4 = codec.serialize(root4)
print(serialized4)
# Output: ""

deserialized4 = codec.deserialize(serialized4)
print(deserialized4)
# Output: None

# Example 5
root5 = Node(1, [Node(2), Node(3), Node(4)])

serialized5 = codec.serialize(root5)
print(serialized5)

deserialized5 = codec.deserialize(serialized5)
print(level_order(deserialized5))
# Output: [1,2,3,4]

# Example 6
root6 = Node(100, [
    Node(200, [
        Node(300),
        Node(400)
    ]),
    Node(500)
])

serialized6 = codec.serialize(root6)
print(serialized6)

deserialized6 = codec.deserialize(serialized6)
print(level_order(deserialized6))
# Output: [100,200,500,300,400]
