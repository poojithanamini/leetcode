class Solution(object):
    def deleteNode(self, root, key):        
        parent = None
        target = root
        while target and target.val != key:
            parent = target
            target = target.left if key < target.val else target.right
            
        def skipTo(node):
            if not parent:
                return node
            
            if target.val < parent.val:
                parent.left = node
            else:
                parent.right = node
                
            return root

        if not target:
            return root
        
        if not target.right:
            return skipTo(target.left)
            
        if not target.left:
            return skipTo(target.right)
        
        leftMost = target.right
        while leftMost.left:
            leftMost = leftMost.left

        leftMost.left = target.left
        
        return skipTo(target.right)