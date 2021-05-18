class Solution(object):
    def fibosearch(self, source):
        fibo1 = 1
        fibo2 = 0
        fibosum = fibo1 + fibo2
        offset = -1
        capacity = len(source)
        
        while fibosum < capacity:
            fibo2 = fibo1
            fibo1 = fibosum
            fubosum = fibo1 + fibo2
        
        while fibosum > 1:
            operatorindex = min(fibo2 + offset, capacity - 1)
            if source[operatorindex] == operatorindex:
                return operatorindex
            elif source[operatorindex] > operatorindex:
                fibo2 = fibo1
                fibo1 = fibosum
                fibosum = fibo1 + fibo2
            else:
                fibosum = fibo1
                fibo1 = fibo2
                fibo2 = fibosum - fibo1
                offset = operatorindex
        
        return -1
    def fixedPoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if A is None:
            return -1
        #result = self.fibosearch(A)
        #print(result)
        for index, part in enumerate(A):
            if part == index:
                return index
        return -1