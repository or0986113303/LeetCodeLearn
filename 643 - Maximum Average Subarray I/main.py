class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if not nums :
            return 0.0
        elif len(nums) == 0:
            return 0.0
        elif len(nums) == 1:
            return float(nums[0])
        elif k > len(nums):
            return 0.0
        else :
            sumofpart = 0
            largest = float('-inf')
            for index, part in enumerate(nums):
                sumofpart += part
                if index >= k:
                    sumofpart -= nums[index - k]
                if index >= k - 1:
                    largest = max(sumofpart, largest)
            return float(largest) / k
        