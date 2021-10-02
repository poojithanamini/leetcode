# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        i = 0
        while p1 and i < n:
            p1 = p1.next
            i += 1
        prev, p2 = None, head
        while p1:
            p1 = p1.next
            prev, p2 = p2, p2.next
        if prev:
            prev.next = p2.next
        else:
            head = head.next
        return head