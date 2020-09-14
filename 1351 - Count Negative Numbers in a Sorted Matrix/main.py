class Solution(object):
    def firstnegative(self, source):
        fiboprev1 = 1
        fiboprev2 = 0
        fibosum = fiboprev1 + fiboprev2
        capacity = len(source)
        offset = -1
        while fibosum < capacity:
            fiboprev2 = fiboprev1
            fiboprev1 = fibosum
            fibosum = fiboprev1 + fiboprev2
        
        while fibosum > 1:
            operatorindex = min(fiboprev2 + offset, capacity - 1)
            if source[operatorindex] > 0 :
                fiboprev2 = fiboprev1
                fiboprev1 = fibosum
                fibosum = fiboprev1 + fiboprev2
            elif source[operatorindex] < 0 and source[operatorindex - 1] >= 0:
                return capacity - operatorindex
            elif source[operatorindex] < 0 and source[operatorindex - 1] < 0:
                fibosum = fiboprev1
                fiboprev1 = fiboprev2
                fiboprev2 = fibosum - fiboprev1
                offset = operatorindex
        return 0
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None:
            return 0
        elif len(grid) == 0 :
            return 0
        
        sourcetmp = []
        
        for part in grid:
            sourcetmp += part
            
        sourcetmp.sort()
        sourcetmp = sourcetmp[::-1]
        result = 0
        print(sourcetmp)
        for index, part in enumerate(sourcetmp):
            if part < 0:
                result = len(sourcetmp) - index
                print(result)
                return result
        
        #result = self.firstnegative(sourcetmp)
        print(result)
        return result