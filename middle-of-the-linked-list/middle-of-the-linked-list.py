# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_temp = []
        while True:
            list_temp.append(head)
            # print(list_temp)
            if head.next:
                head = head.next
            else:
                break
        return list_temp[len(list_temp) // 2]
    