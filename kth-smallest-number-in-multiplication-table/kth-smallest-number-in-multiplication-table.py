class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        l = 1
        r = m*n
        
        while l < r:
            mid = l + (r-l) // 2
            if self.enough(mid,m,n,k):
                r = mid
            else:
                l = mid + 1
        return l
        
		
    def enough(self,num,row,col,k):
        count = 0
        for i in range(1,row+1):
            add = min(num // i, col)
            if add == 0:
                break
            else:
                count += add        
        return count >= k