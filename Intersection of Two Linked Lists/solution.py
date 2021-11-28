class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        nodeSet = set()

        while headA:
            nodeSet.add(headA)
            headA = headA.next

        while headB:
            if headB in nodeSet:
                return headB

            headB = headB.next

        return None