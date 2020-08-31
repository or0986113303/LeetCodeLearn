class Solution(object):
    def mergesort(self, source):
        if len(source) <= 1:
            return source
        middle = len(source) >> 1
        leftpart = self.mergesort(source[:middle])
        rightpart = self.mergesort(source[middle:])
        return self.merge(leftpart, rightpart)

    def merge(self, leftpart, rightpart):
        result = []
        leftindex = 0
        rightindex = 0
        while len(leftpart) > leftindex and len(rightpart) > rightindex:
            if leftpart[leftindex] > rightpart[rightindex]:
                result.append(rightpart[rightindex])
                rightindex += 1
            else :
                result.append(leftpart[leftindex])
                leftindex += 1
        result += leftpart[leftindex:]
        result += rightpart[rightindex:]

        return result
    
    def binarysearch(self, source, target):
        leftindex, rightindex = 0, len(source) - 1
        
        while leftindex < rightindex:
            middle = leftindex + ((rightindex - leftindex) >> 1)
            if abs(middle) > len(source):
                return -1
            elif source[middle] > target :
                rightindex -= 1
            elif source[middle] < target :
                leftindex -= 1
            elif source[middle] == target :
                return middle
        return -1
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix :
            return False
        sourcetmp = []
        for parts in matrix:
            sourcetmp += parts
        if len(sourcetmp) == 0:
            return False
        elif len(sourcetmp) == 1:
            return target in sourcetmp
        elif len(sourcetmp) == 2:
            return target in sourcetmp
        sortedsource = self.mergesort(sourcetmp)
        result = self.binarysearch(sortedsource, target)
        return result >= 0 
        
if __name__ == "__main__":
    source = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 20
    idealresult = False
    result = Solution().searchMatrix(source,target)
    print(result)
    assert result == idealresult, False