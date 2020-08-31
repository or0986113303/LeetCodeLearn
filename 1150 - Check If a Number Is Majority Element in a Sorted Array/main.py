import collections
class Solution(object):
    def isMajorityElement(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        sourcetmp = collections.Counter(nums)
        condition = len(nums) // 2
        result = False
        if target in sourcetmp :
            if sourcetmp[target] > condition:
                result = True
        return result
        