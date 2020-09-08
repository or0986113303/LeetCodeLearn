class Solution(object):
    maxint = (2 ** 31) - 1
    minint = - (2 ** 31)
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            sourcetmp = str(x)
            sourcetmp = sourcetmp[::-1]
        else :
            sourcetmp = str(x)
            signal = sourcetmp[0]
            sourcetmp = sourcetmp[1:]
            sourcetmp = signal + sourcetmp[::-1]
            
        result = int(sourcetmp)
        if result > self.maxint:
            result = 0
        elif result < self.minint:
            result = 0
        return result
        
if __name__ == "__main__":
    source = -123
    idealresult = -321
    result = Solution().reverse(source)
    print(result)
    assert result == idealresult, False