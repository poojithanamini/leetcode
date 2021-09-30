class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i, n = 0, len(nums)
        while i < n:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                # swap
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return [nums[i], i + 1]
        return [-1, -1]