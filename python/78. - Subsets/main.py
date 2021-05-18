# That method was implement to restore all of th depth first search traversal path
# or you can image it to collections of this depth first search for source
class Solution(object):
    def dfs(self, source, start, result, tmp):
        result.append(tmp)
        for index in range(start, len(source), 1):
            self.dfs(source, index + 1, result, tmp + [source[index]])
        
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        result = []
        tmp = []
        self.dfs(nums, 0, result, tmp)
        return result
        
if __name__ == "__main__":
    source = [1,2,3,4,5,6]
    idealresult = [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4],
    [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 6], 
    [1, 2, 3, 5], [1, 2, 3, 5, 6], [1, 2, 3, 6], [1, 2, 4], 
    [1, 2, 4, 5], [1, 2, 4, 5, 6], [1, 2, 4, 6], [1, 2, 5], 
    [1, 2, 5, 6], [1, 2, 6], [1, 3], [1, 3, 4], [1, 3, 4, 5], 
    [1, 3, 4, 5, 6], [1, 3, 4, 6], [1, 3, 5], [1, 3, 5, 6], 
    [1, 3, 6], [1, 4], [1, 4, 5], [1, 4, 5, 6], [1, 4, 6], 
    [1, 5], [1, 5, 6], [1, 6], [2], [2, 3], [2, 3, 4], 
    [2, 3, 4, 5], [2, 3, 4, 5, 6], [2, 3, 4, 6], [2, 3, 5], 
    [2, 3, 5, 6], [2, 3, 6], [2, 4], [2, 4, 5], [2, 4, 5, 6], 
    [2, 4, 6], [2, 5], [2, 5, 6], [2, 6], [3], [3, 4], [3, 4, 5], 
    [3, 4, 5, 6], [3, 4, 6], [3, 5], [3, 5, 6], [3, 6], [4], [4, 5], 
    [4, 5, 6], [4, 6], [5], [5, 6], [6]]
    result = Solution().subsets(source)
    print(result)
    assert result == idealresult, False