class Solution(object):
    def __stepscaculator__(self, source):
        resultvalue = source
        result = 0
        while resultvalue != 1:
            if resultvalue %2 == 0:
                resultvalue = resultvalue // 2
            else :
                resultvalue = 3 * resultvalue + 1
            result += 1
        return result
        
    def __makesourcelist__(self, lo, hi):
        tmp = [0]*(hi -lo + 1)
        for index in range(0, len(tmp), 1):
            tmp[index] = lo + index
        return tmp
    
    def __makestepsource__(self, source):
        result = [0] *len(source)
        for index, parts in enumerate(source):
            result[index] = self.__stepscaculator__(parts)
        return result
    
    def __maketuplesource__(self, steps, original):
        result = []
        for index in range(0, len(steps), 1):
            result.append([steps[index], original[index]])
        return result
    
    def __mergesort__(self, source):
        if len(source) <= 1:
            return source
        middle = len(source) >> 1
        leftpart = self.__mergesort__(source[:middle])
        rightpart = self.__mergesort__(source[middle:])
        result = self.__merge__(leftpart, rightpart)
        return result

    def __merge__(self, leftpart, rightpart):
        result = []
        leftindex = 0
        rightindex = 0
        while len(leftpart) > leftindex and len(rightpart) > rightindex:
            if leftpart[leftindex][0] > rightpart[rightindex][0]:
                result.append(rightpart[rightindex])
                rightindex += 1
            else:
                result.append(leftpart[leftindex])
                leftindex += 1
        result += leftpart[leftindex:]
        result += rightpart[rightindex:]
        return result

    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        sourcetmp = self.__makesourcelist__(lo, hi)
        steptmp = self.__makestepsource__(sourcetmp)
        tulpgroup = self.__maketuplesource__(steptmp, sourcetmp)
        result = self.__mergesort__(tulpgroup)
        print(result)
        #tulpgroup.sort()
        return result[k - 1][1]
        
if __name__ == "__main__":
    lo = 10
    hi = 20
    k = 5
    result = Solution().getKth(lo, hi, k)
    print(result)
    