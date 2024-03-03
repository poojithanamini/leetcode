class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sum = 0
        n = len(nums)
        nums = [None] + nums
        for i in range(1, len(nums)):
            if(n%i == 0):
                sum += nums[i] * nums[i]
        return sum
        