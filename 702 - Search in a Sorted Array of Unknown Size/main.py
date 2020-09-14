# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

class Solution(object):
    def fibosearch(self, source, target):
        fibo1 = 1
        fibo2 = 0
        fibosum = fibo1 + fibo2
        offset = -1
        capacity = 0
        resulttmp = float('-inf')
        while resulttmp < target:
            fibo2 = fibo1
            fibo1 = fibosum
            fibosum = fibo1 + fibo2
            resulttmp = source.get(fibosum)
            capacity = fibosum + 1
            
        print(capacity)
        
        while fibosum > 1:
            operatorindex = min(fibo2 + offset, capacity - 1)
            if source.get(operatorindex) == target:
                return operatorindex
            elif source.get(operatorindex) > target:
                fibosum = fibo1
                fibo1 = fibo2
                fibo2 = fibosum - fibo1
            else :
                fibo2 = fibo1
                fibo1 = fibosum
                fibosum = fibo1 + fibo2
                offset = operatorindex
        return -1
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader is None:
            return -1
        elif reader.get(0) == target:
            return 0
        result = self.fibosearch(reader, target)
        print(result)
        return result
        
        