class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        elements = []
        
        if not root:
            return []
        
        def in_order(node):
            if node:
                in_order(node.left)
                elements.append(node.val)
                in_order(node.right)
        
        in_order(root)
        
        return elements
