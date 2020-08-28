import collections
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sourcetmp = collections.Counter(nums)
        print(sourcetmp)
        result = 0
        for key in sourcetmp :
            if sourcetmp[key] == 1:
                result = key
        return result