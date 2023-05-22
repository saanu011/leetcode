# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev = head
        temp = head.next
        head.next = None
        if temp is None:
            return head

        while temp.next:
            t1 = temp.next
            temp.next = prev
            prev = temp
            temp = t1
        temp.next = prev
        return temp

