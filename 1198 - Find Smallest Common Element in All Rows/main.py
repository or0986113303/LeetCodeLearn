import collections
class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        if mat is None:
            return -1
        capacity = len(mat)
        sourcetmp = []
        for part in mat:
            sourcetmp += part
        
        sourcecollect = collections.Counter(sourcetmp)
        result = float('inf')
        for index, key in enumerate(sourcecollect):
            if sourcecollect[key] >= capacity:
                result = min(result, key)
        return result if result != float('inf') else -1
            
        