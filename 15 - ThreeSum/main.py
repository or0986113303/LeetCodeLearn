class Solution(object):
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

    def threeSum2(self, source):
        if not source:
            return []
        length = len(source)
        source.sort()
        result = []

        for index in range(0, length -2 ,1):
            if index > 0 and source[index] == source[index - 1]:
                continue
            leftindex, rightindex = index + 1, length -1
            sumofthreepart = source[index] + source[leftindex] + source[rightindex]
            while rightindex > leftindex:
                if sumofthreepart == 0 :
                    result.append([source[index], source[leftindex], source[rightindex]])
                    leftindex += 1
                    rightindex -= 1
                    while leftindex < rightindex and source[leftindex] == source[leftindex + 1]:
                        leftindex += 1
                    while leftindex < rightindex and source[rightindex] == source[rightindex + 1]:
                        rightindex += 1 
                elif sumofthreepart < 0 :
                    leftindex += 1
                else :
                    rightindex -= 1
        return result

if __name__ == '__main__':
    source = [-1,0,1,2,-1,-4]
    result = Solution().threeSum2(source)
    print(result)