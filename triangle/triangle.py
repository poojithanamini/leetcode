class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n=len(triangle)
        
        dp=[]
        p=0
        for i in range(n):
            a=[]
            p+=1 
            for j in range(p):
                a.append(triangle[i][j])
            dp.append(a)
        for i in range(n-2,-1,-1):
            for j in range(p-1):
                dp[i][j]=dp[i][j]+min(dp[i+1][j],dp[i+1][j+1])
            p-=1
        return dp[0][0]