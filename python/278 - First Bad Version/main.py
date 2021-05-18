# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 :
            return 1
        leftindex, rightindex = 0, n - 1
        while rightindex >= leftindex:
            middle = leftindex + ((rightindex - leftindex) >> 1)
            if isBadVersion(middle) :
                rightindex = middle - 1
            else :
                leftindex = middle + 1
        return leftindex
                
        