class Solution(object):
    def dfsareacaculator(self, source, result):
        leftindex, rightindex = 0, len(source) - 1

        while rightindex > leftindex:
            if source[rightindex] > source[leftindex]:
                result.append(source[leftindex] * (rightindex - leftindex))
                leftindex += 1
            else:
                result.append(source[rightindex] * (rightindex - leftindex))
                rightindex -= 1

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        elif len(height) == 1:
            return 0
        elif len(height) == 2:
            return min(height)
        
        result = []
        self.dfsareacaculator(height, result)

        return max(result)
        
if __name__ == "__main__":
    source = [1,8,6,2,5,4,8,3,7]
    idealresult = 49
    result = Solution().maxArea(source)
    print(result)
    assert result==idealresult, False