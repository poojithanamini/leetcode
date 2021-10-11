class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        currentmax = 0
            
        def dfs(root):
            if not root:
                return 0
            nonlocal currentmax
            
            left = 1+dfs(root.left) if root.left else 0
            right = 1+dfs(root.right) if root.right else 0
            currentmax = max(currentmax, left+right)
            return max(left,right)
        
        dfs(root)
        
        return currentmax