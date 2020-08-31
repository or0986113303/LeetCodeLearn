class Solution(object):
    fibonaccinumbers = []
    result = []
    hashofsum = {}
    def fibonaccigenerater(self, target):
        fiboprev1 = 1
        fiboprev2 = 1
        fibosum = fiboprev1 + fiboprev2
        self.fibonaccinumbers.append(fiboprev1)
        self.fibonaccinumbers.append(fiboprev2)
        self.fibonaccinumbers.append(fibosum)
        while target > fibosum:
            fiboprev2 = fiboprev1
            fiboprev1 = fibosum
            fibosum = fiboprev1 + fiboprev2
            self.fibonaccinumbers.append(fibosum)
    
    def dfsoffibonacci(self, target, prev, count):
        result = count
        isresult = False
        for parts in self.fibonaccinumbers:
            if target - parts in self.fibonaccinumbers and not parts in prev:
                result += 1
                return result
        if not isresult :
            for parts in self.fibonaccinumbers:
                prev.append(parts)
                result + self.dfsoffibonacci(target - parts, prev, count)
        return result
                
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        result, fiboprev1, fiboprev2 = 0, 1, 1
        while fiboprev2 <= k:
            fiboprev1, fiboprev2 = fiboprev2, fiboprev1 + fiboprev2

        while fiboprev1:
            if fiboprev1 <= k:
                k -= fiboprev1
                result += 1
            fiboprev1, fiboprev2 = fiboprev2 - fiboprev1, fiboprev1
        return result