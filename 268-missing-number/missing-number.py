class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summ = (len(nums) * (len(nums) + 1))//2
        res = 0
        for i in range(len(nums)):
            res = res + nums[i]
        return summ - res        