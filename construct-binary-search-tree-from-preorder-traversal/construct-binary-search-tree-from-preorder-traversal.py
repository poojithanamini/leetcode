class Solution:
    def bstFromPreorder(self, preorder):
        def helper(down, up):
            if self.idx >= len(preorder): return None
            if not down <= preorder[self.idx] <= up: return None
            root = TreeNode(preorder[self.idx])
            self.idx += 1
            root.left = helper(down, root.val)
            root.right = helper(root.val, up)
            return root
        
        self.idx = 0
        return helper(-float("inf"), float("inf"))