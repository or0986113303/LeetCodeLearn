class Solution(object):
    def mergesort(self, source):
        if len(source) <= 1:
            return source
        middle = len(source) // 2
        leftpart = self.mergesort(source[:middle])
        rightpart = self.mergesort(source[middle:])
        return self.merge(leftpart, rightpart)
    def merge(self, leftpart, rightpart):
        result = []
        leftindex, rightindex = 0, 0
        while len(leftpart) > leftindex and len(rightpart) > rightindex:
            if leftpart[leftindex] > rightpart[rightindex] :
                result.append(rightpart[rightindex])
                rightindex += 1
            else :
                result.append(leftpart[leftindex])
                leftindex += 1
        result += leftpart[leftindex:]
        result += rightpart[rightindex:]
        return result
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix :
            return -1
        sourcetmp = []
        for parts in matrix:
            sourcetmp += parts
        if len(sourcetmp) < k:
            return -1
        print(sourcetmp)
        sortedsourcetmp = self.mergesort(sourcetmp)
        return sortedsourcetmp[k - 1]

if __name__ == "__main__":
    source = [[ 1,  5,  9],[10, 11, 13],[12, 13, 15]]
    k = 8
    idealresult = 13
    result = Solution().kthSmallest(source, k)
    print(result)
    assert result == idealresult, False