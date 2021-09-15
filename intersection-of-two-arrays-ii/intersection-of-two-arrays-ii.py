class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=[]
        if(len(nums1)<=len(nums2)):
            small=nums1
            big=nums2
        else:
            big=nums1
            small=nums2
        for i in small:
            if(i in big):
                s.append(i)
                big.remove(i)
        return s