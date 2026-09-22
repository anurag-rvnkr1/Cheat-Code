'''
328. Odd Even Linked List

Given the head of a singly linked list, group all nodes with odd indices
together followed by nodes with even indices.

The relative order inside the odd group and the even group must remain the same.

Note:
    - Node position starts from 1 (NOT node value).

Return the reordered linked list.

Example 1:
    Input:
        head = [1,2,3,4,5]

    Output:
        [1,3,5,2,4]

Example 2:
    Input:
        head = [2,1,3,5,6,4,7]

    Output:
        [2,3,6,7,1,5,4]

Constraints:
    The number of nodes is in the range [0, 10^4].
    -10^6 <= Node.val <= 10^6
'''

# Linked List + Two Pointer Reordering

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(
        self,
        head: Optional[ListNode]
    ) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:

            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head


# -----------------------------
# Helper Functions for Testing
# -----------------------------

def build_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def linked_list_to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


# Example usage
solution = Solution()

# Example 1
head1 = build_linked_list([1,2,3,4,5])
result1 = solution.oddEvenList(head1)
print(linked_list_to_list(result1))
# Output: [1,3,5,2,4]

# Example 2
head2 = build_linked_list([2,1,3,5,6,4,7])
result2 = solution.oddEvenList(head2)
print(linked_list_to_list(result2))
# Output: [2,3,6,7,1,5,4]

# Example 3
head3 = build_linked_list([1])
result3 = solution.oddEvenList(head3)
print(linked_list_to_list(result3))
# Output: [1]

# Example 4
head4 = build_linked_list([1,2])
result4 = solution.oddEvenList(head4)
print(linked_list_to_list(result4))
# Output: [1,2]

# Example 5
head5 = build_linked_list([10,20,30,40,50,60])
result5 = solution.oddEvenList(head5)
print(linked_list_to_list(result5))
# Output: [10,30,50,20,40,60]
