class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def recurs(n):
            if not n:
                return (0, 0)
            
            l, r = n.left, n.right
            
            lSum, lTilt = recurs(l)
            rSum, rTilt = recurs(r)
            
            curTilt = abs(lSum - rSum)
            
            return (lSum + rSum + n.val, lTilt + rTilt + curTilt)

        return recurs(root)[1]