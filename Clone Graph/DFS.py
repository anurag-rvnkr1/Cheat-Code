'''
133. Clone Graph

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

Example 1:
    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]

Example 2:
    Input: adjList = [[]]
    Output: [[]]

Example 3:
    Input: adjList = []
    Output: []

Constraints:
    The number of nodes in the graph is in the range [0, 100].
    1 <= Node.val <= 100
    Node.val is unique for each node.
    There are no repeated edges and no self-loops.
    The graph is connected.
'''

# Depth-First Search (DFS)

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}

        def dfs(current):
            if current in visited:
                return visited[current]

            clone = Node(current.val)
            visited[current] = clone

            for neighbor in current.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)


# Helper function to print graph using DFS
def printGraph(node):
    visited = set()

    def dfs(current):
        if current in visited:
            return

        visited.add(current)

        print(f"Node {current.val}: {[n.val for n in current.neighbors]}")

        for neighbor in current.neighbors:
            dfs(neighbor)

    if node:
        dfs(node)
    else:
        print(None)


# Example usage
solution = Solution()

# Example 1
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

cloned_graph = solution.cloneGraph(node1)
printGraph(cloned_graph)
# Output:
# Node 1: [2, 4]
# Node 2: [1, 3]
# Node 3: [2, 4]
# Node 4: [1, 3]

# Example 2
single_node = Node(1)
cloned_single = solution.cloneGraph(single_node)
printGraph(cloned_single)
# Output:
# Node 1: []

# Example 3
print(solution.cloneGraph(None))
# Output: None
