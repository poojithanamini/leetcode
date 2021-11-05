class Solution:
    def arrangeCoins(self, n: int) -> int:
        answer = 0
        count = 0
        if(n==1):
            return 1
        for i in range(1,n+1):
            count+=i
            if(count<=n):
                answer+=1
            else:
                return answer