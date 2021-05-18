class Solution(object):
    def threeSumClosest2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        nums.sort()
        res = float('inf') # sum of 3 number
        for t in range(N):
            i, j = t + 1, N - 1
            while i < j:
                _sum = nums[t] + nums[i] + nums[j]
                if abs(_sum - target) < abs(res - target):
                    res = _sum
                if _sum > target:
                    j -= 1
                elif _sum < target:
                    i += 1
                else:
                    return target
        return res

    def threeSumClosest(self, nums, target):
        if nums is None:
            return -1
        elif len(nums) < 3:
            return -1
        
        # assume the source is a binary tree
        nums.sort()
        capacity = len(nums)
        result = float('inf')
        for index in range(0, capacity, 1):
            headindex, tailindex = index + 1, capacity - 1
            while headindex < tailindex:
                sumtmp = source[headindex] + source[index] + source[tailindex]
                if abs(result - target) > abs(sumtmp - target):
                    result = sumtmp
                if sumtmp > target :
                    tailindex -= 1
                elif sumtmp < target:
                    headindex += 1
                else :
                    return target
        return result

if __name__ == '__main__':
    source = [-1,2,1,-4]
    target = 1
    result = Solution().threeSumClosest(source, target)
    print(result)