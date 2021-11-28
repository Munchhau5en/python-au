# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        array = []
        flag = True
        while head != None:
            array.append(head.val)
            head = head.next
        for i in range(len(array) // 2):
            if array[i] != array[(len(array) - 1) - i]:
                flag = False
        return flag


