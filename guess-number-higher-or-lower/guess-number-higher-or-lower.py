class Solution:
    def guessNumber(self, n: int) -> int:
        s, e = 1, n
        while True:
            m = (s + e) // 2
            g = guess(m)
            if g == 0:
                return m
            elif g == 1:
                s = m + 1
            else: 
                e = m - 1