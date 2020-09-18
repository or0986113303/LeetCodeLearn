class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        if candies is None:
            return []
        
        maxofkids = max(candies)
        
        result = []
        
        for part in candies:
            if part == maxofkids:
                result.append(True)
            elif part + extraCandies >= maxofkids:
                result.append(True)
            else :
                result.append(False)
        return result
                