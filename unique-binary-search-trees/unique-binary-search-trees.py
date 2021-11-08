class Solution:
    def numTrees(self, n: int, memo={}) -> int:
        if n in memo:
            return memo[n]
        
        if n == 0 or n == 1:
            memo[n] = 1
            return 1
        elif n == 2:
            memo[n] = 2
            return 2            
        else:
            i = n-1
            total = self.numTrees(i)
            while i > 0:
                total += self.numTrees(i)  * self.numTrees(n-1-i)
                i -= 1
            memo[n] = total
            return total