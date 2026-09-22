'''
429. N-ary Tree Level Order Traversal

Given the root of an N-ary tree, return the level order traversal of its nodes'
values.

Return the values level by level from left to right.

Example 1:
    Input:
        root = [1,null,3,2,4,null,5,6]

    Output:
        [[1],[3,2,4],[5,6]]

Example 2:
    Input:
        root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10]

    Output:
        [[1],[2,3,4,5],[6,7,8],[9,10]]

Example 3:
    Input:
        root = []

    Output:
        []

Constraints:
    Number of nodes is in the range [0, 10^4].
    0 <= Node.val <= 10^4
    Maximum depth <= 1000.
'''

# Tree BFS

from typing import List
from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                for child in node.children:
                    queue.append(child)

            result.append(current_level)

        return result


# Example usage
solution = Solution()

# Example 1
root1 = Node(1, [
    Node(3, [
        Node(5),
        Node(6)
    ]),
    Node(2),
    Node(4)
])

print(solution.levelOrder(root1))
# Output: [[1],[3,2,4],[5,6]]

# Example 2
root2 = Node(1, [
    Node(2),
    Node(3, [
        Node(6),
        Node(7, [
            Node(11, [
                Node(14)
            ])
        ])
    ]),
    Node(4, [
        Node(8, [
            Node(12)
        ])
    ]),
    Node(5, [
        Node(9, [
            Node(13)
        ]),
        Node(10)
    ])
])

print(solution.levelOrder(root2))
# Output:
# [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

# Example 3
root3 = None
print(solution.levelOrder(root3))
# Output: []

# Example 4
root4 = Node(10)
print(solution.levelOrder(root4))
# Output: [[10]]

# Example 5
root5 = Node(100, [
    Node(200),
    Node(300),
    Node(400),
    Node(500)
])

print(solution.levelOrder(root5))
# Output: [[100],[200,300,400,500]]

# Example 6
root6 = Node(1, [
    Node(2, [
        Node(5),
        Node(6)
    ]),
    Node(3),
    Node(4, [
        Node(7),
        Node(8),
        Node(9)
    ])
])

print(solution.levelOrder(root6))
# Output: [[1],[2,3,4],[5,6,7,8,9]]
