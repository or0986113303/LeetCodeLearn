class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        result = []
        for parts in nums:
            result.append(a*parts**2 + b*parts + c)
        result.sort()
        return result

if __name__ == "__main__":
    source = [-4,-2,2,4]
    a = 1
    b = 3
    c = 5
    idealresult = [3, 9, 15, 33]
    result = Solution().sortTransformedArray(source, a, b, c)
    print(result)
    assert result == idealresult, False