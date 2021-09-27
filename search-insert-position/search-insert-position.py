class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if(nums[i]>target or nums[i] == target):
                return i
        if(nums[0]>target):
            return 0
        if(nums[-1]<target):
            return i+1