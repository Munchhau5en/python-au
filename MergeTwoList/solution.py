class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = l1
        b = l2

        dummy = ListNode()

        c = dummy

        while a or b:
            if a is None:
                c.next = b
                break
            elif b is None:
                c.next = a
                break

            elif a.val <= b.val:
                c.next = a
                a = a.next
            else:
                c.next = b
                b = b.next
            c = c.next

        return dummy.next
