import collections
class Solution(object):
    def windowslide(self, source, target, capacity):
        tailindex= 0
        sumtmp = 0
        lengthtmp = float('-inf')
        sumhash = collections.defaultdict(list)
        '''
        while tailindex < capacity:
            sumtmp += source[tailindex]
            while sumtmp == target or headindex == capacity - 1:
                sumtmp -= source[headindex]
                lengthtmp = max(lengthtmp, tailindex - headindex + 1)
                headindex += 1
            tailindex += 1
        return lengthtmp if lengthtmp != float('-inf') else 0
        '''
        sumhash[0].append(-1)
        while tailindex < capacity:
            sumtmp += source[tailindex]
            if sumtmp not in sumhash:
                sumhash[sumtmp].append(tailindex)
            print(sumhash)
            if sumtmp -target in sumhash:
                lengthtmp = max(lengthtmp, tailindex - sumhash[sumtmp -target][0])
            tailindex += 1
        return lengthtmp if lengthtmp != float('-inf') else 0
        
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums :
            return 0
        elif len(nums) == 0:
            return 0

        return self.windowslide(nums, k, len(nums))

if __name__ == "__main__":
    source = [1,-1,5,-2,3]
    target = 3
    idealresult = 4
    result = Solution().maxSubArrayLen(source, target)
    print(result)
    assert result == idealresult