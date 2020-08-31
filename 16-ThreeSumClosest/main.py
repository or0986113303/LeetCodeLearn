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
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        result = float('inf')
        length = len(nums) 
        nums.sort()

        for index in range(0, length , 1):
            leftindex, rightindex = index + 1, length -1
            while rightindex > leftindex:
                sumtmp = nums[index] + nums[leftindex] + nums[rightindex]
                if abs(sumtmp - target) < abs(result - target):
                    result = sumtmp
                if sumtmp > target:
                    rightindex -= 1
                elif sumtmp < target:
                    leftindex += 1
                else:
                    return target
        return result

if __name__ == '__main__':
    source = [-1,2,1,-4]
    target = 1
    result = Solution().threeSumClosest(source, target)
    print(result)