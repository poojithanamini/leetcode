class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        b= str(bin(n)[2:])
        if b[0]=='1' and b[1:].count('1')==0:
            return True
        else:
            return False