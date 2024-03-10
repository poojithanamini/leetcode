class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        memo = {}
        res = 0
        for r in range(len(s)):
            if (s[r] not in memo):
                res = max(res, r - l + 1)
            else:
                if(memo[s[r]] < l):
                   res = max(res, r - l + 1)
                else:
                    l = memo[s[r]] + 1
            memo[s[r]] = r
            

        return res
                
            

        