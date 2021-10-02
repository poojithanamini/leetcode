class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        begin = end = 0
        low = high = 0
        while high < len(s):
            if window.get(s[high]):
                while s[low] != s[high]:
                    window[s[low]] = False
                    low = low + 1

                low = low + 1 
            else:
                window[s[high]] = True
                if end - begin < high - low:
                    begin = low
                    end = high

            high = high + 1
        return len(s[begin:end + 1])