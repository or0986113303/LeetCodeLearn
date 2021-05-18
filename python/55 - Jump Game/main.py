class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = 0
        for index, part in enumerate(nums):
            if index > target:
                return False
            target = max(target, index + part)
        return True
    
if __name__ == "__main__":
    source = [2,3,1,1,4]
    idealresult = True
    result = Solution().canJump(source)
    print(result)
    assert result == idealresult, False