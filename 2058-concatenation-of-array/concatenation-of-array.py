class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return [x for x in nums] +  [x for x in nums]
        