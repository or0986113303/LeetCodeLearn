class Solution(object):
    def recursion(self, source, start, result, target, targetindex):
        if source is None:
            return
        elif start == len(source):
            return
        if source[start] == target:
            result.append([targetindex, start])
        self.recursion(source, start + 1, result, target, targetindex)
        
        
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None: 
            return 0
        
        collects = []
        
        for index, part in enumerate(nums):
            self.recursion(nums, index + 1, collects, part, index)
        print(collects)
        return len(collects)