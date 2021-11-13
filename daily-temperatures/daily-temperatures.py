class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        n = len(temperatures)
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            t = temperatures[i]
            while st and temperatures[st[-1]] <= t:
                st.pop()
            if st:
                ans[i] = (st[-1] - i)
            st.append(i)

        return ans