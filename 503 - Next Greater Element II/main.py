class Solution(object):
    def findnextgreater(self, target, source, startindex):
        result = -1
        for _, parts in enumerate(source[startindex : -1]):
            if parts > target:
                result = parts
                return result
        return result
    
    def makecircular(self, source):
        return source + source
    
    def dfsiterate(self, target, source, result):
        for parts in target:
            if parts in source:
                startindex = source.index(parts)
                source = source[:startindex] + source[startindex + 1 : ]
                result.append(self.findnextgreater(parts, source, startindex))
            else :
                result.append(-1)
    
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        result = []
        target = self.makecircular(nums)
        self.dfsiterate(nums, target, result)
        return result
        '''
        result = [-1] * len(nums)
        stack = []
        for index in range(len(nums)) * 2:
            while stack and (nums[stack[-1]] < nums[index]):
                result[stack.pop()] = nums[index]
            stack.append(index)
        return result
        
if __name__ == '__main__':
    source = [100,1,11,1,120,111,123,1,-1,-100]
    result = Solution().nextGreaterElements(source)
    print(result)