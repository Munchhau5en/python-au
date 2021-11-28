# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def create_single_linked_list(self, values):
        previous_node = ListNode(values[len(values) - 1])
        for i in range(0, len(values) - 1):
            next_node = ListNode(values[len(values) - i - 2], previous_node)
            previous_node = next_node
        return previous_node

    def sortList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        arr = []
        h = head
        while (h != None):
            arr.append(h.val)
            h = h.next
        arr = sorted(arr)
        arr = self.create_single_linked_list(arr)
        return arr
