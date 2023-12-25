class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels_str = ""
        res = ""
        for i in s:
            if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                vowels_str = vowels_str + i
        for i in s:
            if i not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                res = res + i
            else:
                res = res + vowels_str[-1]
                vowels_str = vowels_str[:-1]
        return res