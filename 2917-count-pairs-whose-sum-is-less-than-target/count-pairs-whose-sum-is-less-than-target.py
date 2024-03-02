class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i] + nums[j] < target):
                    res.append([nums[i], nums[j]])
        return len(res)
                     