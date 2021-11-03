class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        
        def rec(node=root, prev=0):
            if node.left is None and node.right is None:
                return prev + node.val            
            
            prev = (prev + node.val)*10
            
            left = right = 0
            if node.left:
                left = rec(node.left, prev)
            if node.right:
                right = rec(node.right, prev)
            
            return left + right
        
        return rec()