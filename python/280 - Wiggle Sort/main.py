class Solution(object):
    def mergesort(self, source):
        if len(source) <= 1 :
            return source
        middle = len(source) >> 1
        leftpart = self.mergesort(source[:middle])
        rightpart = self.mergesort(source[middle:])
        return self.merge(leftpart, rightpart)
    def merge(self, leftpart, rightpart):
        leftindex, rightindex = 0, 0
        result = []
        while len(leftpart) > leftindex and len(rightpart) > rightindex:
            if leftpart[leftindex] > rightpart[rightindex]:
                result.append(rightpart[rightindex])
                rightindex += 1
            else :
                result.append(leftpart[leftindex])
                leftindex += 1
        result += leftpart[leftindex:]
        result += rightpart[rightindex:]
        return result
        
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        numssorted = self.mergesort(nums)
        for index in range(1, len(nums)-1, 2):
            nums[index], nums[index + 1] = nums[index + 1], nums[index]
        print(nums)
        print(numssorted)
            