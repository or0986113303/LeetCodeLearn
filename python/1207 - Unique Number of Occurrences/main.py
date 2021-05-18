import collections
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        sourcetmp = collections.Counter(arr)
        occurrences = collections.Counter(sourcetmp.values())
        for value in occurrences.values():
            if value > 1 :
                return False
        return True
            
if __name__ == "__main__":
    source = [1,2,2,1,1,3]
    idealresult = True
    result = Solution().uniqueOccurrences(source)
    print(result)
    assert result == idealresult, False