# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        tail = ListNode(val=head.val)
        while head.next != None:
            head = head.next
            tail = ListNode(val=head.val, next=tail)
        return tail
