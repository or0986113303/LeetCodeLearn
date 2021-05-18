class Solution(object):
    def mergesort(self, source):
        if len(source) <= 1:
            return source
        middle = len(source) // 2
        leftpart = self.mergesort(source[:middle])
        rightpart = self.mergesort(source[middle:])
        return self.merge(leftpart, rightpart)
    
    def merge(self, leftpart, rightpart):
        leftindex, rightindex = 0, 0
        result = []
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
        
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        
        sortedsource = self.mergesort(A)
        print(sortedsource)
        for index in range(len(sortedsource) - 3, -1, -1):
            if sortedsource[index] + sortedsource[index + 1] > sortedsource[index + 2]:
                return sum(sortedsource[index:index+3])
        return 0