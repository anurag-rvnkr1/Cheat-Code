'''
237. Delete Node in a Linked List

There is a singly linked list, and you are given the node to be deleted.

You are NOT given access to the head of the list.

Delete the given node from the linked list.

You may assume:
    - The given node is not the last node.
    - All values in the linked list are unique.
    - The node to be deleted exists in the list.

Example 1:
    Input: head = [4,5,1,9], node = 5
    Output: [4,1,9]

Explanation:
    Delete node with value 5.

Example 2:
    Input: head = [4,5,1,9], node = 1
    Output: [4,5,9]

Explanation:
    Delete node with value 1.

Constraints:
    The number of nodes in the list is in the range [2, 1000].
    -1000 <= Node.val <= 1000
    The value of each node in the list is unique.
    The node to be deleted is not the last node in the list.
'''

# Linked List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        # Copy the next node's value into the current node.
        node.val = node.next.val

        # Skip the next node.
        node.next = node.next.next


# Helper function to print linked list
def printList(head):
    current = head

    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next

    print()


# Example usage
solution = Solution()

# Example 1
head1 = ListNode(4)
head1.next = ListNode(5)
head1.next.next = ListNode(1)
head1.next.next.next = ListNode(9)

# Delete node with value 5
solution.deleteNode(head1.next)

printList(head1)  # Output: 4 -> 1 -> 9

# Example 2
head2 = ListNode(4)
head2.next = ListNode(5)
head2.next.next = ListNode(1)
head2.next.next.next = ListNode(9)

# Delete node with value 1
solution.deleteNode(head2.next.next)

printList(head2)  # Output: 4 -> 5 -> 9

# Example 3
head3 = ListNode(1)
head3.next = ListNode(2)

# Delete node with value 1
solution.deleteNode(head3)

printList(head3)  # Output: 2
