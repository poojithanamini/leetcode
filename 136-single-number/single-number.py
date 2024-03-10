class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        memo = {}
        for i in nums:
            if i not in memo:
                memo[i] = 1
            else:
                memo[i] = memo[i] + 1
        for key, val in memo.items():
            if val == 1:
                return key
        