class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        result = []
        remaining = []
        for partsinarr2 in arr2:
            for partsinarr1 in arr1:
                if partsinarr2 == partsinarr1:
                    result.append(partsinarr2)
                
        for partsinarr1 in arr1:
            if not partsinarr1 in arr2:
                remaining.append(partsinarr1)
        remaining.sort()
        return result + remaining
        
        '''
        for partsinarr2 in arr2:
            while partsinarr2 in arr1:
                result.append(partsinarr2)
                arr1.remove(partsinarr2)
        if arr1 :
            arr1.sort()
        return result + arr1
        '''
    

        