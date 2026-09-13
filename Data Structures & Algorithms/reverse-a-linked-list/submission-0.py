# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # store reference to rest of list
            curr.next = prev        # reverse pointer
            prev = curr             # advance prev
            curr = next_node        # advance curr

        return prev

