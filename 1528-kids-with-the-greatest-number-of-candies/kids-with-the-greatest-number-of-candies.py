class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highest = max(candies)
        res = []

        for i in candies:
            if(i+extraCandies >= highest):
                res.append(True)
            else:
                res.append(False)
        return res
                