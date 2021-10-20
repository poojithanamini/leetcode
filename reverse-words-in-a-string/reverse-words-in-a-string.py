class Solution:
    def reverseWords(self, s: str) -> str:
        a=[x for x in s.split(' ')]
        i=[x for x in a if(len(x)>0)]
        p=' '.join(reversed(i))
        return p