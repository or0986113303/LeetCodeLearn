class Solution(object):
    def caculateareaofall(self, source, areacollections):
        # assume the operator work from follow two indexes
        leftindex, rightindex = 0, len(source) - 1
        
        # basic follow is make a loop when the rightindex is greater than leftindex
        while leftindex < rightindex:
            areacollections.append(min(source[leftindex], source[rightindex]) * (rightindex - leftindex))
            if source[leftindex] > source[rightindex]:
                rightindex -= 1
            else :
                leftindex += 1

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # the first step must to traversal of all coornidate from data source
        # according to based on the linear search and make speed up, using the two pointer to implement it
        
        if not height :
            return 0
        elif len(height) <= 1:
            return height
        areacollections = []
        self.caculateareaofall(height, areacollections)
        return max(areacollections)
        
        
if __name__ == "__main__":
    source = [1,8,6,2,5,4,8,3,7]
    idealresult = 49
    result = Solution().maxArea(source)
    print(result)
    assert result==idealresult, False