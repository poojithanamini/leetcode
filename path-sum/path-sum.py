# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(node, cur):
            cur += node.val
            if node.left and node.right:
                return dfs(node.left, cur) or dfs(node.right, cur)
            elif node.left:
                return dfs(node.left, cur)
            elif node.right:
                return dfs(node.right, cur)
            elif not node.left and not node.right and cur == targetSum:
                return True
            
        return dfs(root, 0)