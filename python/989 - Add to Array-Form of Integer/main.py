class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        if not A:
            result = []
            for parts in str(K):
                result.append(parts)
            return result
        
        sourcetmp = ''
        result = []
        for parts in A:
            sourcetmp += str(parts)
        sourcetmp = int(sourcetmp)
        resulttmp = str(sourcetmp + K)
        for parts in resulttmp :
            result.append(parts)
        return result
        
        