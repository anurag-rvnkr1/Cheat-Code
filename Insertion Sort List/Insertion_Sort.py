'''
147. Insertion Sort List

Given the head of a singly linked list, sort the list using insertion sort,
and return the sorted list's head.

The steps of the insertion sort algorithm:

    1. Insertion sort iterates, consuming one input element each repetition.
    2. It grows a sorted output list.
    3. At each iteration, insertion sort removes one element from the input data,
       finds the location it belongs within the sorted list, and inserts it there.
    4. It repeats until no input elements remain.

Example 1:
    Input: head = [4,2,1,3]
    Output: [1,2,3,4]

Example 2:
    Input: head = [-1,5,3,4,0]
    Output: [-1,0,3,4,5]

Constraints:
    The number of nodes in the list is in the range [1, 5000].
    -5000 <= Node.val <= 5000
'''

# Insertion Sort

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = head

        while current:
            prev = dummy

            # Find correct position in sorted list.
            while prev.next and prev.next.val < current.val:
                prev = prev.next

            next_node = current.next
            current.next = prev.next
            prev.next = current
            current = next_node

        return dummy.next


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
head1.next = ListNode(2)
head1.next.next = ListNode(1)
head1.next.next.next = ListNode(3)

sorted_head1 = solution.insertionSortList(head1)
printList(sorted_head1)
# Output: 1 -> 2 -> 3 -> 4

# Example 2
head2 = ListNode(-1)
head2.next = ListNode(5)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(0)

sorted_head2 = solution.insertionSortList(head2)
printList(sorted_head2)
# Output: -1 -> 0 -> 3 -> 4 -> 5

# Example 3
head3 = ListNode(1)

sorted_head3 = solution.insertionSortList(head3)
printList(sorted_head3)
# Output: 1
