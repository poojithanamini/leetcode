class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        t.sort()
        s.sort()
        if(t==s):
            return True
        else:
            return False