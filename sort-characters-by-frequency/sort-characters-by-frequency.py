class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        cnt = dict(sorted(cnt.items(), key=lambda item: (item[1], item[0]), reverse=True))
        ans = ''
        
        for k, v in cnt.items():
            ans += k * v
        
        return ans