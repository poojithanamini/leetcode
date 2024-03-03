class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        if(len(set(nums)) == len(nums)): return 0
        res = 0
        dictionary = {}
        for i in nums:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        for i in dictionary:
            if dictionary[i] != 1:
                res += ((dictionary[i]* (dictionary[i]-1))//2)
        return res
        
        