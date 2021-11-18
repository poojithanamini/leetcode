class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=[]
        
        k = set(nums)
        for i in range(1,n+1):
            if i not in k:
                a.append(i)
        return a