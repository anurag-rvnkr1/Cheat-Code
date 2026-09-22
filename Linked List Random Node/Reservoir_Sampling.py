'''
382. Linked List Random Node

Given a singly linked list, return a random node's value from the linked list.
Each node must have the same probability of being chosen.

Implement the Solution class:

    Solution(ListNode head)
        Initializes the object with the head of the linked list.

    int getRandom()
        Returns a random node's value. Every node must have an equal chance
        of being selected.

Example 1:
    Input:
        head = [1,2,3]

    Output:
        [1,2,3]
        (Each value has probability 1/3.)

Example 2:
    Input:
        head = [10]

    Output:
        10

Constraints:
    The number of nodes is in the range [1, 10^4].
    -10^4 <= Node.val <= 10^4

Follow-up:
    What if the linked list is extremely large and its length is unknown?
'''

# Reservoir Sampling

from typing import Optional
import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        result = self.head.val
        current = self.head.next
        count = 2

        while current:
            if random.randrange(count) == 0:
                result = current.val

            current = current.next
            count += 1

        return result


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


# Example usage
head1 = build_linked_list([1,2,3])
solution1 = Solution(head1)

print(solution1.getRandom())
# Output: 1 or 2 or 3

print(solution1.getRandom())
# Output: 1 or 2 or 3

print(solution1.getRandom())
# Output: 1 or 2 or 3

head2 = build_linked_list([10])
solution2 = Solution(head2)

print(solution2.getRandom())
# Output: 10

head3 = build_linked_list([5,15,25,35,45])
solution3 = Solution(head3)

print(solution3.getRandom())
# Output: Random value from the list

print(solution3.getRandom())
# Output: Random value from the list
