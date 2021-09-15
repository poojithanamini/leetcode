class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for _ in range(numRows-1):
            last = ans[-1]
            ans.append([1]+[last[i]+last[i+1] for i in range(len(last)-1)]+[1])
        return ans