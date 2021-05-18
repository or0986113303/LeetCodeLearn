class Solution(object):
    def reverse(self, source, startindex, endindex):
        middle = (startindex + endindex) // 2 + 1
        for index in range(startindex, middle, 1):
            self.swap(source, index, startindex + endindex - index)
            
    def swap(self, source, sourceindex, targetindex):
        source[sourceindex], source[targetindex] = source[targetindex], source[sourceindex]
        
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # the next premutation means if find the element which is greater than next one, just swap them
        # and then keep to find where be occured nexty premutation
        # for the edge case, there is no input just return empty array or null
        # if length of source is no need to to reverse or swap just return itself
        
        if not nums:
            return []
        elif len(nums) <= 1:
            return nums
        
        length = len(nums)
        counter = length - 1
        while counter > 0 and nums[counter] <= nums[counter - 1]:
            counter -= 1
        self.reverse(nums, counter, length - 1)
        
        if counter > 0:
            for index in range(counter, length, 1):
                if nums[index] > nums[counter - 1]:
                    self.swap(nums, counter - 1, index)
                    break
        print(nums)
        
    
        