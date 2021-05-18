class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        if nums is None :
            return nums
        
        xpart = nums[:n + 1]
        ypart = nums[n:]
        print(ypart)
        print(xpart)
        
        result = []
        for index in range(0, n, 1):
            result.append(xpart[index])
            result.append(ypart[index])
        print(result)
        return result
            
        