class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans = 1
        prev = 1
        for i in nums:
            if i + prev < 1:
                ans += 1 - ( i + prev )
                prev = 1
            else:
                prev = i + prev
        return ans