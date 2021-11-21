# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        
        rootVal = postorder[-1]
        rootIdx = inorder.index(rootVal)
        
        leftInorder, rightInorder = inorder[:rootIdx], inorder[rootIdx+1:]
        leftPostorder, rightPostorder = postorder[:len(leftInorder)], postorder[len(leftInorder):-1]
        
        leftSubtree, rightSubtree = self.buildTree(leftInorder, leftPostorder), \
                                    self.buildTree(rightInorder, rightPostorder)
        
        return TreeNode(rootVal, leftSubtree, rightSubtree)