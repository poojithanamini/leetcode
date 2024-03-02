class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = {}
        result = []
        sorted_list = sorted(nums)
        for i in range(len(sorted_list)):
            if sorted_list[i] not in res:
                res[sorted_list[i]] = i
        for i in nums:
            result.append(res[i])

        return result
        