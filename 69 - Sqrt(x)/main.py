import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.sqrt(x))

if __name__ == "__main__":
    source = 8
    idealresult = 2
    result = Solution().mySqrt(8)
    print(result)
    assert result == idealresult, False