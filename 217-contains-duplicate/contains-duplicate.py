class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = {}
        for i in nums:
            if i not in x:
                x[i] = 1
            else:
                return True
        return False
        