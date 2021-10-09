class Solution:
    def hammingWeight(self, n: int) -> int:
        
        def helper(n, s):
            if n == 0:
                return 0
            if n == 1:
                return s + 1
            return helper(n//2, s + (n % 2))
        
        return helper(n, 0)