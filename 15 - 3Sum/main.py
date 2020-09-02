import collections
class Solution(object):
    def dfscollectioncaculator(self, source, start, end, result, tmp, comparetmp):
        if len(tmp) == 3 and sum(tmp) == 0:
            tmp2 = collections.Counter(tmp)
            if not tmp2 in comparetmp:
                result.append(tmp)
                comparetmp.append(tmp2)
        for index in range(start, end, 1):
            self.dfscollectioncaculator(source, index + 1, end, result, tmp + [source[index]] , comparetmp)
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dfscollectioncaculator(nums, 0, len(nums), result, [], [])
        return result

if __name__ == "__main__":
    source = [6,-5,-6,-1,-2,8,-1,4,-10,-8,-10,-2,-4,-1,-8,-2,8,9,-5,-2,-8,-9,-3,-5]
    result = Solution().threeSum(source)
    print(result)
        