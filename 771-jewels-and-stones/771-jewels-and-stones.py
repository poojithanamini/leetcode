class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        countt = 0
        for i in jewels:
            countt += stones.count(i)
            
        return countt