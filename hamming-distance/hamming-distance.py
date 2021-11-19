class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return self.dec2binary(x,y,0)
        
    def dec2binary(self,x,y,hdist):
        if x==0 and y==0:
            return hdist
        if x%2!=y%2:
            hdist+=1
        return self.dec2binary(x//2,y//2,hdist)