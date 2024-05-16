class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)
        for i in range(len(haystack) - needle_length + 1):
            sub_string = haystack[i: i+needle_length]
            if(needle == sub_string):
                return i
        return -1
        