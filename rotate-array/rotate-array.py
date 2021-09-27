class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)-1
        while k > 0:
            nums.insert(0, nums[l])
            nums.pop(l+1)
            k -= 1