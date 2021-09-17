class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = collections.Counter(s)
        for i in dict:
            if dict[i]==1:
                return s.index(i)
        return -1
