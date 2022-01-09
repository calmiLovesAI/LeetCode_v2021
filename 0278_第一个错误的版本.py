# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer

def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid - 1
                if 1 < mid <= n and not isBadVersion(mid-1):
                    return mid
            else:
                l = mid + 1

        if mid == 1 and isBadVersion(mid):
            return 1

            