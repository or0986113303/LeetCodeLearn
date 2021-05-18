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

if __name__ == "__main__":
    source = [434,2,10,543,3,1,1,9,9,20,34,76,6]
    result = Solution().mergesort(source)
    print(result)