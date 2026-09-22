'''
430. Flatten a Multilevel Doubly Linked List

You are given a doubly linked list where each node contains:

    val
    prev
    next
    child

The child pointer may point to another doubly linked list.

Flatten the list so that all nodes appear in a single-level doubly linked list.

The child pointers should become None after flattening.

Example 1:
    Input:
        1---2---3---4---5---6
                |
                7---8---9---10
                    |
                    11--12

    Output:
        1-2-3-7-8-11-12-9-10-4-5-6

Example 2:
    Input:
        1---2
        |
        3

    Output:
        1-3-2

Example 3:
    Input:
        []

    Output:
        []

Constraints:
    Number of nodes <= 1000.
    1 <= Node.val <= 10^5
'''

# DFS + Linked List

from typing import Optional


class Node:
    def __init__(
        self,
        val=0,
        prev=None,
        next=None,
        child=None
    ):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        def dfs(node: Node) -> Node:
            current = node
            last = node

            while current:
                next_node = current.next

                if current.child:
                    child_head = current.child
                    child_tail = dfs(child_head)

                    current.next = child_head
                    child_head.prev = current

                    current.child = None

                    if next_node:
                        child_tail.next = next_node
                        next_node.prev = child_tail

                    last = child_tail
                else:
                    last = current

                current = next_node

            return last

        dfs(head)
        return head


# -----------------------------
# Helper Function for Testing
# -----------------------------

def print_list(head: Optional[Node]):
    result = []
    current = head

    while current:
        result.append(current.val)
        current = current.next

    print(result)


# Example usage
solution = Solution()

# Example 1
head1 = Node(1)
head1.next = Node(2, prev=head1)
head1.next.next = Node(3, prev=head1.next)
head1.next.next.next = Node(4, prev=head1.next.next)

head1.next.next.child = Node(7)
head1.next.next.child.next = Node(8, prev=head1.next.next.child)
head1.next.next.child.next.next = Node(9, prev=head1.next.next.child.next)

flattened1 = solution.flatten(head1)
print_list(flattened1)
# Output: [1,2,3,7,8,9,4]

# Example 2
head2 = Node(1)
head2.child = Node(3)
head2.next = Node(2, prev=head2)

flattened2 = solution.flatten(head2)
print_list(flattened2)
# Output: [1,3,2]

# Example 3
head3 = None
flattened3 = solution.flatten(head3)
print(flattened3)
# Output: None

# Example 4
head4 = Node(10)
flattened4 = solution.flatten(head4)
print_list(flattened4)
# Output: [10]

# Example 5
head5 = Node(1)
head5.next = Node(2, prev=head5)
head5.next.child = Node(4)
head5.next.child.child = Node(5)

flattened5 = solution.flatten(head5)
print_list(flattened5)
# Output: [1,2,4,5]

# Example 6
head6 = Node(1)
head6.next = Node(2, prev=head6)
head6.next.next = Node(3, prev=head6.next)
head6.next.child = Node(7)
head6.next.child.next = Node(8, prev=head6.next.child)

flattened6 = solution.flatten(head6)
print_list(flattened6)
# Output: [1,2,7,8,3]
