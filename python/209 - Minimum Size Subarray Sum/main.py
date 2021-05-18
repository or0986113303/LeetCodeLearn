class Solution(object):                
    def windowslide(self, source, target, capacity):
        # there using the two pointe to implement the window slide operator
        # the first step is declaring these pointers start condition
        
        headindex, tailindex = 0, 0
        # the second step is declare the variable for caculate the value of sum of subarray
        # and restore the length between head index and tail index
        sumtmp = 0
        # declare the length tmp variable is the infinty meaning than will use min function to compare with
        # the other length of sub array
        lengthtmp = float('inf')

        while tailindex < capacity:
            sumtmp += source[tailindex]
            # if feet or over the target, subtract the head element and move head index to the next
            while sumtmp >= target:
                sumtmp -= source[headindex]
                lengthtmp = min(lengthtmp, tailindex - headindex + 1)
                headindex += 1
            # move the tail index to the next
            tailindex += 1
        
        return lengthtmp if lengthtmp != float('inf') else 0


    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # there is using the window slide method to 
        # determining the minimun length of sub array
        # which's sum equal to target
        if not s :
            return 0
        elif s == 0:
            return 0
        elif not nums :
            return 0
        capacity = len(nums)
        return self.windowslide(source, target, capacity)


if __name__ == "__main__":
    target = 7
    source = [2,3,1,2,4,3]
    idealresult = 2
    result = Solution().minSubArrayLen(target, source)
    print(result)
    assert result == idealresult