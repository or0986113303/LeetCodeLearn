class Solution(object):
    def fibonacci(self, source, target):
        if not source :
            return -1

        length = len(source)
        fiboprev1 = 1
        fiboprev2 = 0
        fibosum =  fiboprev1 + fiboprev2
        indexoffset = -1

        while fibosum < length:
            fiboprev2, fiboprev1 = fiboprev1, fibosum
            fibosum = fiboprev1 + fiboprev2
        
        while fibosum > 1:
            operatorindex = min(fiboprev2 + indexoffset, length - 1)
        
            if source[operatorindex] > target:
                fibosum = fiboprev1
                fiboprev1 = fiboprev2
                fiboprev2 = fibosum - fiboprev1
            elif source[operatorindex] < target:
                fiboprev2 = fiboprev1
                fiboprev1 = fibosum
                fibosum = fiboprev1 + fiboprev2
                indexoffset = operatorindex
            else :
                return operatorindex

        if(fibosum and source[indexoffset + 1] == target): 
            return indexoffset + 1

        return -1

if __name__ == "__main__":
    source = [3,6,7,8,9,10,11,12,23,34,45,56,67,78,89,90]
    target = 23
    idealresult = 8
    result = Solution().fibonacci(source, target)
    print(result)
    assert result == idealresult, False