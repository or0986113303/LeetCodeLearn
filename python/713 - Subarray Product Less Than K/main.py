class Solution(object):
    def windowslide(self, source, target):
        headindex, tailindex = 0, 0
        capacity = len(source)
        producttmp = source[0]
        count = 0
        while tailindex < capacity:
            if headindex != tailindex:
                producttmp *= source[tailindex]
                while producttmp > target:
                    producttmp /= source[headindex]
                    headindex += 1
                count += tailindex - headindex + 1
            tailindex += 1
        return count

    def determine(self, source, target):
        result = 0
        for part in source:
            producttmp = 1
            for subpart in part:
                producttmp = producttmp * subpart
            if producttmp < target:
                result += 1
        return result
    def subset(self, source, start, result, resulttmp):
        result.append(resulttmp)
        for index in range(start, len(source), 1):
            self.subset(source, index + 1, result, resulttmp + [source[index]])
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        if nums is None:
            return -1
        elif k is None:
            return -1
        
        result = self.windowslide(nums, k)
        return result
        
        '''
        result = []
        self.subset(nums, 0, result, [])
        print(result)
        resultcount = self.determine(result, k)
        return resultcount
        '''
        '''
        capacity = len(nums)
        product = 1
        headindex, tailindex = 0, 0
        result = 0
        while tailindex < capacity:
            product *= nums[tailindex]
            while headindex <= tailindex and product >= k:
                product = product // nums[headindex]
                headindex += 1
            result += tailindex - headindex + 1
            tailindex += 1
        return result
        '''
        
        
if __name__ == "__main__":
    nums = [10, 5, 2, 6]
    k = 100
    idealresult = 8
    result = Solution().numSubarrayProductLessThanK(nums, k)
    print(result)
    assert result == idealresult
    