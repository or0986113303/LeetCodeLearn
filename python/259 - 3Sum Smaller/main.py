class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        sourcelength = len(nums)
        count, thirdindex = 0, 2
        while thirdindex < sourcelength:
            firstindex, secondindex = 0, thirdindex - 1
            while firstindex < secondindex:  # Two Pointers, linear time.
                if nums[firstindex] + nums[secondindex] + nums[thirdindex] >= target:
                    secondindex -= 1
                else:
                    count += secondindex - firstindex
                    firstindex += 1
            thirdindex += 1
        return count

        
if __name__ == '__main__':
    source = [-2,0,1,3]
    target = 2

    result = Solution().threeSumSmaller(source, target)
    print(result)