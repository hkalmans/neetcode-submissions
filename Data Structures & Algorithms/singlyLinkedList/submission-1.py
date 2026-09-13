from typing import List

class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        # Use a dummy head node to simplify operations
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val, self.head.next)
        self.head.next = new_node
        # If the list was empty before insertion, the tail needs updating
        if self.tail == self.head:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        # Iterate to the node *before* the one to remove
        while i < index and curr:
            i += 1
            curr = curr.next
        
        # Check if the node to remove exists
        if curr and curr.next:
            # If removing the tail, update the tail to the previous node
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

