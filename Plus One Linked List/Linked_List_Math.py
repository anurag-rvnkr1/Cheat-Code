'''
369. Plus One Linked List

Given the head of a non-empty singly linked list representing a non-negative integer,
add one to the integer and return the head of the resulting linked list.

The digits are stored such that the most significant digit comes first.

Example 1:
    Input:
        head = [1,2,3]

    Output:
        [1,2,4]

Example 2:
    Input:
        head = [0]

    Output:
        [1]

Example 3:
    Input:
        head = [9,9,9]

    Output:
        [1,0,0,0]

Constraints:
    The number of nodes in the linked list is in the range [1, 100].
    0 <= Node.val <= 9
    The list does not contain leading zeros except for the number 0 itself.
'''

# Linked List + Math

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def plusOne(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        last_non_nine = dummy
        current = head

        while current:
            if current.val != 9:
                last_non_nine = current
            current = current.next

        last_non_nine.val += 1

        current = last_non_nine.next

        while current:
            current.val = 0
            current = current.next

        return dummy if dummy.val else dummy.next


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
head1 = build_linked_list([1,2,3])
result1 = solution.plusOne(head1)
print(linked_list_to_list(result1))
# Output: [1,2,4]

# Example 2
head2 = build_linked_list([0])
result2 = solution.plusOne(head2)
print(linked_list_to_list(result2))
# Output: [1]

# Example 3
head3 = build_linked_list([9,9,9])
result3 = solution.plusOne(head3)
print(linked_list_to_list(result3))
# Output: [1,0,0,0]

# Example 4
head4 = build_linked_list([1,9,9])
result4 = solution.plusOne(head4)
print(linked_list_to_list(result4))
# Output: [2,0,0]

# Example 5
head5 = build_linked_list([2,3,9,9])
result5 = solution.plusOne(head5)
print(linked_list_to_list(result5))
# Output: [2,4,0,0]

# Example 6
head6 = build_linked_list([8,9,9,9,9])
result6 = solution.plusOne(head6)
print(linked_list_to_list(result6))
# Output: [9,0,0,0,0]
