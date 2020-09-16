class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # assume there is only pair or not of the result
        
        if nums is None:
            return []
        elif target is None:
            return []
        
        sumhash = {}
        for index, part in enumerate(nums):
            if target - part in sumhash:
                return [sumhash[target - part], index]
            else :
                sumhash[part] = index
        return []