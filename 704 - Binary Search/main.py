class Solution(object):
    def binarysearch(self, source, target):
        if source is None:
            return -1
        
        result = -1
        leftindex, rightinedx = 0, len(source) - 1
        
        while rightinedx >= leftindex:
            middle = leftindex + ((rightinedx - leftindex) >> 1)
            if source[middle] == target:
                result = middle
                break
            elif source[middle] > target:
                rightinedx -= 1
            else : 
                leftindex += 1
        return result
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None:
            return -1
        elif target is None:
            return -1
        elif len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        #return self.binarysearch(nums, target)
        if target in nums:
            return nums.index(target)
        else :
            return -1
        