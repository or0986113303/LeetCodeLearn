import collections
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        sourcetmp = collections.Counter(nums)
        condition = len(nums) // 3
        for index, key in enumerate(sourcetmp):
            if sourcetmp[key] > condition:
                result.append(key)
        return result
        
        