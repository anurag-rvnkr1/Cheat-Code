'''
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

Example 2:
    Input: list1 = [], list2 = []
    Output: []
Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]
 
Constraints:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
'''
#Create New List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:

            if list1.val <= list2.val:
                tail.next = ListNode(list1.val)
                list1 = list1.next
            else:
                tail.next = ListNode(list2.val)
                list2 = list2.next

            tail = tail.next

        # Add remaining nodes
        while list1:
            tail.next = ListNode(list1.val)
            list1 = list1.next
            tail = tail.next

        while list2:
            tail.next = ListNode(list2.val)
            list2 = list2.next
            tail = tail.next

        return dummy.next

#Example Usage
sol=Solution()
print(sol.mergeTwoLists([1,2,4], [1,3,4]))
print(sol.mergeTwoLists([], []))
print(sol.mergeTwoLists([], [0]))