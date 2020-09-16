class Solution(object):
    def kSum(self, source, target, orderofsumstep):
        result = []
        capacity = len(source)
        if capacity == 0 or source[0] * orderofsumstep > target or target > source[-1] * orderofsumstep:
            return result
        if orderofsumstep == 2:
            return self.twosum(source, target)
        for index in range(0, capacity, 1):
            if index == 0 or source[index - 1] != source[index]:
                for _, part in enumerate(self.kSum(source[index + 1:], target - source[index], orderofsumstep - 1)):
                    result.append([source[index]] + part)
        return result
        
    def twosum(self, source, target):
        capacity = len(source)
        headindex, tailindex = 0, capacity - 1
        result = []
        while tailindex > headindex:
            sumtmp = source[headindex] + source[tailindex]
            if sumtmp > target or (tailindex < capacity - 1 and source[tailindex] == source[tailindex + 1]):
                tailindex -= 1
            elif sumtmp < target or (headindex > 0 and source[headindex] == source[headindex - 1]):
                headindex += 1
            else :
                result.append([source[headindex], source[tailindex]])
                headindex += 1
                tailindex -= 1
        return result        
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        nums.sort()
        result = []
        for index in range(length - 2):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            leftindex, rightindex = index + 1, length - 1
            while leftindex < rightindex:
                _sum = nums[index] + nums[leftindex] + nums[rightindex]
                if _sum == 0:
                    result.append([nums[index], nums[leftindex], nums[rightindex]])
                    leftindex += 1
                    rightindex -= 1
                    while leftindex < rightindex and nums[leftindex] == nums[leftindex - 1]:
                        leftindex += 1
                    while leftindex < rightindex and nums[rightindex] == nums[rightindex + 1]:
                        rightindex -= 1
                elif _sum < 0:
                    leftindex += 1
                else:
                    rightindex -= 1
        return result

    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return[]
        elif len(nums) < 3:
            return []
        
        nums.sort()
        return self.kSum(nums, 0, 3)

if __name__ == '__main__':
    source = [3,2,4]
    idealresult = [[1,2]]
    result = Solution().threeSum2(source)
    print(result)
    assert result == idealresult, False