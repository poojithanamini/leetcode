# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        a = head
        
        # loop over link and break out links that are duplicates
        while a.next is not None:
            # if the next value is not the same as the current value, just keep looping
            if a.val != a.next.val:
                a=a.next
             # if the next value is the same as the current value, pop the next link out
            else:
                a.next = a.next.next     
                
        return head