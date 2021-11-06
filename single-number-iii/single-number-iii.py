class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a=[x for x in nums if nums.count(x)==1]
        return a