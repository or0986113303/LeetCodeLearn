class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return -1
        elif k > len(nums):
            return -1
        nums.sort()
        nums = nums[::-1]
        return nums[k-1]
        
if __name__ == "__main__":
    source = [3,2,3,1,2,4,5,5,6]
    k = 4
    idealresult = 4
    result = Solution().findKthLargest(source, k)
    print(result)
    assert result == idealresult