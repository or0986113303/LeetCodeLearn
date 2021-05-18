class Solution(object):
    def getRange(self, lower, upper):
        if lower == upper:
            return "{}".format(lower)
        else:
            return "{}->{}".format(lower, upper)
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        result = []
        preval = lower - 1
        for i in range(len(nums) + 1):
            if i == len(nums):
                curval = upper + 1
            else:
                curval = nums[i]
            if curval - preval >= 2:
                result.append(self.getRange(preval + 1, curval - 1))
            preval = curval
        return result
        
if __name__ == "__main__":
    nums = [1]
    lower = 0
    upper = 9
    idealresult = ["1"]
    result = Solution().findMissingRanges(nums, lower, upper)
    print(result)
    assert result == idealresult, False