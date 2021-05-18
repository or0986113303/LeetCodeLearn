class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        if groupSizes is None :
            return []
        result = []
        beusedhash = {}
        capacity = len(groupSizes)
        for index, part in enumerate(groupSizes):
            if index not in beusedhash:
                count, operatorindex = 0, 0
                resulttmp = []
                while count < part and operatorindex < capacity:
                    if part == groupSizes[operatorindex] and operatorindex not in beusedhash:
                        resulttmp.append(operatorindex)
                        beusedhash[operatorindex] = groupSizes[operatorindex]
                        count += 1
                    operatorindex += 1
                result.append(resulttmp)
        return result
                    
        