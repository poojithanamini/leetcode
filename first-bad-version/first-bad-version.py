# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        
        knownGood = 1
        knownBad = n

        mid = (knownGood + knownBad) // 2
        while knownGood + 1 != knownBad:
            mid = (knownGood + knownBad) // 2
            if isBadVersion(mid):
                knownBad = mid
            else:
                knownGood = mid
        
        return knownBad