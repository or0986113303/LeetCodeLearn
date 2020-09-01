class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A) == 1 :
            return 0
        maxnum = max(A)
        minnum = min(A)
        result = maxnum - K - minnum - K
        return result if result > 0 else 0

if __name__ == "__main__":
    source = [1,4,7]
    k = 3
    idealresult = 0
    result = Solution().smallestRangeI(source, k)
    print(result)
    assert result == idealresult, False