class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet_set = set()
        for i in range(len(nums)):
            complements = set()
            for j in range(i + 1, len(nums)):
                complement_needed = (nums[i] + nums[j]) * -1
                if complement_needed in complements:
                    triplet_set.add(tuple(sorted((nums[i],nums[j],complement_needed))))
                    complements.remove(complement_needed)
                complements.add(nums[j])
        return list(triplet_set)