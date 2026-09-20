'''
160. Intersection of Two Linked Lists

Given the heads of two singly linked lists headA and headB, return the node at which
the two lists intersect. If the two linked lists have no intersection at all, return None.

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note:
    The linked lists must retain their original structure after the function returns.

Example 1:
    Input: intersectVal = 8,
           listA = [4,1,8,4,5],
           listB = [5,6,1,8,4,5],
           skipA = 2,
           skipB = 3
    Output: Node with value 8

Example 2:
    Input: intersectVal = 2,
           listA = [1,9,1,2,4],
           listB = [3,2,4],
           skipA = 3,
           skipB = 1
    Output: Node with value 2

Example 3:
    Input: intersectVal = 0,
           listA = [2,6,4],
           listB = [1,5]
    Output: None

Constraints:
    The number of nodes in listA is in the range [1, 3 * 10^4].
    The number of nodes in listB is in the range [1, 3 * 10^4].
    1 <= Node.val <= 10^5
'''

# Two Pointers

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self,
        headA: Optional[ListNode],
        headB: Optional[ListNode]
    ) -> Optional[ListNode]:

        pointerA = headA
        pointerB = headB

        # Both pointers traverse equal total distance.
        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

        return pointerA


# Example usage
solution = Solution()

# Example 1
common = ListNode(8)
common.next = ListNode(4)
common.next.next = ListNode(5)

headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = common

headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = common

intersection = solution.getIntersectionNode(headA, headB)
print(intersection.val if intersection else None)  # Output: 8

# Example 2
common2 = ListNode(2)
common2.next = ListNode(4)

headA2 = ListNode(1)
headA2.next = ListNode(9)
headA2.next.next = ListNode(1)
headA2.next.next.next = common2

headB2 = ListNode(3)
headB2.next = common2

intersection2 = solution.getIntersectionNode(headA2, headB2)
print(intersection2.val if intersection2 else None)  # Output: 2

# Example 3
headA3 = ListNode(2)
headA3.next = ListNode(6)
headA3.next.next = ListNode(4)

headB3 = ListNode(1)
headB3.next = ListNode(5)

intersection3 = solution.getIntersectionNode(headA3, headB3)
print(intersection3)  # Output: None
