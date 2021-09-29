class Solution:
    def reverseWords(self, s: str) -> str:
        a=[x for x in s.split()]
        res=[]
        for i in a:
            res.append("".join(reversed(i)))
        return(' '.join(res))    