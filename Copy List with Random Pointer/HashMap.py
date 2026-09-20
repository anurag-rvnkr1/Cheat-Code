'''
138. Copy List with Random Pointer

A linked list of length n is given such that each node contains an additional
random pointer, which could point to any node in the list, or None.

Construct a deep copy of the list.

The deep copy should consist of exactly n brand new nodes, where each new node
has its value set to the value of its corresponding original node.

Both the next and random pointers of the new nodes should point to new nodes in
the copied list such that the pointers in the original list and copied list
represent the same list state.

Example 1:
    Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
    Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
    Input: head = [[1,1],[2,1]]
    Output: [[1,1],[2,1]]

Example 3:
    Input: head = [[3,null],[3,0],[3,null]]
    Output: [[3,null],[3,0],[3,null]]

Constraints:
    0 <= n <= 1000
    -10^4 <= Node.val <= 10^4
    Node.random is None or points to some node in the linked list.
'''

# Hash Map

from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        old_to_new = {}

        # Step 1: Create copies of all nodes.
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        # Step 2: Assign next and random pointers.
        current = head
        while current:
            copy = old_to_new[current]
            copy.next = old_to_new.get(current.next)
            copy.random = old_to_new.get(current.random)
            current = current.next

        return old_to_new[head]


# Helper function to print copied list
def printList(head):
    current = head

    while current:
        random_val = current.random.val if current.random else None
        print(f"[{current.val}, Random:{random_val}]", end=" -> ")
        current = current.next

    print("None")


# Example usage
solution = Solution()

# Example 1
node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node2.random = node1
node3.random = node5
node4.random = node3
node5.random = node1

copied_head = solution.copyRandomList(node1)
printList(copied_head)
# Output:
# [7, Random:None] -> [13, Random:7] -> [11, Random:1] ->
# [10, Random:11] -> [1, Random:7] -> None

# Example 2
head2 = None
copied_head2 = solution.copyRandomList(head2)
print(copied_head2)
# Output: None
