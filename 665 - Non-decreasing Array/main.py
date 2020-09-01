class Solution(object):
    def mergesort(self, source):
        if len(source) <= 1:
            return source
        middle = len(source) >> 1
        leftpart = self.mergesort(source[:middle])
        rightpart = self.mergesort(source[middle:])
        return self.merge(leftpart, rightpart)
    def merge(self, leftpart, rightpart):
        result = []
        leftindex, rightindex = 0, 0
        
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
        
        return result
    def checkisdescending(self, source):
        targettmp = source[0]
        result = []
        for index in range(1, len(source), 1):
            if targettmp > source[index]:
                result.append(False)
            else :
                result.append(True)
            targettmp = source[index]
        print(result)
        return result
            
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        resulttmp = None
        for index in range(len(nums) - 1):
            if nums[index] > nums[index+1]:
                if resulttmp is not None:
                    return False
                resulttmp = index

        return (resulttmp is None or resulttmp == 0 or resulttmp == len(nums)-2 or
                nums[resulttmp-1] <= nums[resulttmp+1] or nums[resulttmp] <= nums[resulttmp+2])
        