class Solution(object):
    def test(self, source, target):
        headindex, tailindex = 0, 0
        capacity = len(source)
        result = float('-inf')
        while headindex < capacity and tailindex < capacity:
            tailindex = 0
            while tailindex < capacity:
                if headindex != tailindex:
                    sumtmp = source[headindex] + source[tailindex]
                    if sumtmp < target:
                        result = max(result, sumtmp)
                tailindex += 1
            headindex += 1
        return result if result != float('-inf') else -1

    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if A is None:
            return -1
        elif K is None:
            return -1
        '''
        result = float('-inf')
        for index, part in enumerate(A):
            for index2, part2 in enumerate(A):
                if part != part2 and index != index2:
                    sumtmp = part + part2
                    if sumtmp < K:
                        result = max(result, sumtmp)
        return result if result != float('-inf') else -1
        '''
        return self.test(A, K)

if __name__ == "__main__":
    A = [34,23,1,24,75,33,54,8]
    K = 60
    idealresult = 58
    result = Solution().twoSumLessThanK(A, K)
    print(result)
    assert result == idealresult, False

