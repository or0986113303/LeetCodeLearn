class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1, -1]
        else :
            first = nums.index(target)
            nums = nums[::-1]
            last = len(nums) - nums.index(target) - 1
            return [first, last]

if __name__ == "__main__":
    source = [1,2,3,4,5,6,6,7,8,9,10,10]
    target = 6
    idealresult = [5,6]
    result = Solution().searchRange(source, target)
    print(result)
    assert result == idealresult, False