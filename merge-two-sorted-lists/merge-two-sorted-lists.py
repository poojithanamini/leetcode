class Solution:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
        
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp1 = l1
        tmp2 = l2
        newNode = Solution(float('-inf'))
        tmp = newNode
        while tmp1 and tmp2:
            if tmp1.val <= tmp2.val:
                # tmp = tmp1
                tmp.next = tmp1
                tmp1 = tmp1.next
                # tmp1 = tmp.next
            else:
                tmp.next = tmp2
                tmp2 = tmp2.next
            tmp = tmp.next
        while tmp1:
            tmp.next = tmp1
            tmp1 = tmp1.next
            tmp = tmp.next
        
        while tmp2:
            tmp.next = tmp2
            tmp2 = tmp2.next
            tmp = tmp.next
        return newNode.next