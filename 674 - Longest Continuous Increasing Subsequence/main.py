class Solution(object):
    def windowslide(self, source, capacity):
        headindex, tailindex = 0, 1
        maxdistance = float('-inf')
        while tailindex < capacity:
            maxdistance = max(maxdistance, tailindex - headindex)
            if source[tailindex] <= source[tailindex - 1]:
                headindex = tailindex
            tailindex += 1
        return max(maxdistance, tailindex - headindex) if maxdistance != float('-inf') else 0
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        capacity = len(nums)
        return self.windowslide(nums, capacity)
        
if __name__ == "__main__":
    source = [1,3,5,4,7]
    idealresult = 3
    result = Solution().findLengthOfLCIS(source)
    print(result)
    assert result == idealresult, False