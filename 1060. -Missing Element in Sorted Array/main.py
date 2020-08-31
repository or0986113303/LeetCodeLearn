class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return -1
        elif len(nums) < 1:
            return -1
        elif len(nums) == 1:
            return nums[0] + 1
        subnums = []
        nthnumber = 0
        for index in range(1, len(nums), 1):
            nthnumber += nums[index] - nums[index - 1] - 1
            if nthnumber >= k:
                subnums = [x for x in range(nums[index - 1] + 1, nums[index] + 1, 1)]
                print(subnums)
                return subnums[k - (nums[index] - nums[index - 1]) - 1]
        print(nums[-1] + k - nthnumber)
        return nums[-1] + k - nthnumber
        
        '''
        startpoint = nums[0]
        endpoint = nums[-1]
        subnumstmp = [x for x in range(startpoint, endpoint + 1, 1)]
        for parts in subnumstmp:
            if not parts in nums:
                subnums.append(parts)
        if k > len(subnums):
            for index in range(1, k - len(subnums) + 1, 1):
                subnums.append(nums[-1] + index)
        print(subnums)
        '''
        #return subnums[k - 1]

if __name__ == "__main__":
    source = [4,7,9,10]
    K = 1
    idealresult = 5
    result = Solution().missingElement(source, K)
    assert result == idealresult, False