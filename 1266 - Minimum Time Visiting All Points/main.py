class Solution(object):
    def sumoftimecost(self, source):
        sumtmp = 0
        for index in range(0, len(source) - 1, 1):
            sumtmp += max(abs(source[index][0] - source[index + 1][0]), abs(source[index][1] - source[index + 1][1]))
            
        return sumtmp
        
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points :
            return 0
        
        result = self.sumoftimecost(points)
        print(result)
        return result