class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        if not arr1 or not arr2 or not arr3:
            return []
        
        recordhash = {}
        result = []
        sourcetmp = arr1 + arr2 + arr3
        
        for _, part in enumerate(sourcetmp):
            if part not in recordhash:
                recordhash[part] = 1
            else :
                recordhash[part] += 1
                
        for _, part in enumerate(recordhash):
            if recordhash[part] == 3:
                result.append(part)
        return result