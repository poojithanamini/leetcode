# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.ismirror(root, root)
    def ismirror(self, root1:TreeNode, root2: TreeNode)-> bool:
        if(root1 is None and root2 is None):
            return True
        if(root1 is not None and root2 is not None):
            if(root1.val==root2.val):
                return (self.ismirror(root1.left, root2.right) and self.ismirror(root1.right, root2.left))
        return False