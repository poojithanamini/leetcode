class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def rec(node):
            if not node:
                return None,None
            if not node.next and not node.child:
                return node,node
            
            child_head, child_tail = rec(node.child)
            next_head, next_tail = rec(node.next)
            if not node.child:
                return node, next_tail
            if not node.next:
                node.next = child_head
                child_head.prev = node
                node.child = None
                return node, child_tail
            
        
            node.next = child_head
            child_head.prev = node
            child_tail.next = next_head
            next_head.prev = child_tail
            node.child = None
            return node, next_tail
        
        _,_ = rec(head)
        return head