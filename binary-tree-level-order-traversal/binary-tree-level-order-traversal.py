# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        elements = []
        
        if not root:
            return elements
        
        queue = [root]
        next_queue = []
        level = []
        while queue != []: 
            for root in queue:
                level.append(root.val)
                if root.left is not None:
                    next_queue.append(root.left)
                if root.right is not None:
                    next_queue.append(root.right)
            elements.append(level)
            level = []
            queue = next_queue
            next_queue = []
        
        return elements