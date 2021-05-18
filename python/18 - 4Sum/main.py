class Solution:
    def twosum(self, source, target):
        result = []
        capacity = len(source) 
        headindex, tailindex = 0, capacity - 1
        while headindex < tailindex:
            sumtmp = source[headindex] + source[tailindex]
            if sumtmp < target or (headindex > 0 and source[headindex] == source[headindex - 1]):
                headindex += 1
            elif sumtmp > target or (tailindex < capacity - 1 and source[tailindex] == source[tailindex + 1]):
                tailindex -= 1
            else:
                result.append([source[headindex], source[tailindex]])
                headindex += 1
                tailindex -= 1
        return result
    
    def kstepsum(self, source, target, kstep):
        result = []
        capacity = len(source)
        if capacity == 0 or source[0] * kstep > target or source[-1] * kstep < target or kstep == 1:
            return result
        if kstep == 2 :
            return self.twosum(source, target)
        for index in range(0, capacity, 1):
            if index == 0 or source[index] != source[index - 1]:
                for _, part in enumerate(self.kstepsum(source[index + 1 :], target - source[index], kstep - 1)):
                    result.append([source[index]] + part)
        return result
    def fourSum(self, nums, target):
        if nums is None:
            return []
        elif len(nums) < 4:
            return []
        # rearrange the source, because of assume there are a binary tree likely
        nums.sort()
        result = self.kstepsum(nums, target, 4)
        print(result)
        return result
        

if __name__ == "__main__":
    source = [1, 0, -1, 0, -2, 2]
    target = 0
    idealresult = [[-1,  0, 0, 1],[-2, -1, 1, 2],[-2,  0, 0, 2]]
    result = Solution().fourSum(source, target)
    print(result)
    assert result == idealresult, False